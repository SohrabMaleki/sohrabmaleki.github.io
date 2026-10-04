"""Check generated Jekyll pages and local assets, including Linux filename case.

Usage: python scripts/check_site.py _site [--baseurl /preview]
Uses only Python's standard library; remote services are deliberately not required.
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.ids = set()
        self.duplicates = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            if attrs['id'] in self.ids:
                self.duplicates.append(attrs['id'])
            self.ids.add(attrs['id'])
        for attr in ('href', 'src', 'poster'):
            if attr in attrs:
                self.references.append((tag, attr, attrs[attr]))
        if 'srcset' in attrs:
            for source in attrs['srcset'].split(','):
                if source.strip():
                    self.references.append((tag, 'srcset', source.strip().split()[0]))


def check(root, baseurl):
    root = root.resolve()
    baseurl = '/' + baseurl.strip('/') if baseurl.strip('/') else ''
    inventory = {p.relative_to(root).as_posix(): p for p in root.rglob('*') if p.is_file()}
    parsed = {}
    errors = []
    checked = 0
    for relative, path in inventory.items():
        if path.suffix != '.html':
            continue
        text = path.read_text(encoding='utf-8')
        if re.search(r'\{[{%].*?[}%]\}', text):
            errors.append(f'{relative}: unrendered Liquid template')
        page = Page(text)
        parsed[relative] = page
        for duplicate in page.duplicates:
            errors.append(f'{relative}: duplicate id {duplicate}')

    def local_reference(source, tag, attr, value, check_anchor=True):
        nonlocal checked
        if not value.strip():
            errors.append(f'{source}: empty {tag}[{attr}]')
            return
        url = urlsplit(value)
        if url.scheme or url.netloc:
            return
        if value == '#':
            errors.append(f'{source}: placeholder # link')
            return
        current_url = baseurl + '/' + source
        target_url = urlsplit(urljoin(current_url, value))
        raw_path = unquote(target_url.path)
        if baseurl:
            if not raw_path.startswith(baseurl + '/'):
                errors.append(f'{source}: {value} escapes baseurl {baseurl}')
                return
            raw_path = raw_path[len(baseurl):]
        target = posixpath.normpath(raw_path).lstrip('/')
        if raw_path.endswith('/') or not target or target == '.':
            target = (target.rstrip('/') + '/index.html').lstrip('/')
        if target not in inventory:
            errors.append(f'{source}: {value} -> missing or wrong-case {target}')
            return
        checked += 1
        if target_url.fragment and check_anchor and target in parsed:
            anchor = unquote(target_url.fragment)
            if anchor not in parsed[target].ids:
                errors.append(f'{source}: {value} -> missing anchor {anchor}')

    for relative, page in parsed.items():
        for tag, attr, value in page.references:
            local_reference(relative, tag, attr, value)
    for relative, path in inventory.items():
        if path.suffix == '.css':
            for url in re.findall(r'url\(\s*[\'\"]?([^\)\'\"]+)', path.read_text(encoding='utf-8')):
                local_reference(relative, 'css', 'url', url.strip(), False)
        if path.suffix.lower() == '.pdf':
            with path.open('rb') as stream:
                if b'%PDF-' not in stream.read(1024):
                    errors.append(f'{relative}: invalid PDF header')
    for required in ['index.html', 'cv.html', 'notes.html', 'talks.html', 'publications.html',
                     'research.html', 'projects.html', '404.html', 'CNAME', 'sitemap.xml',
                     'google2a79bfa1ab9ebcb0.html']:
        if required not in inventory:
            errors.append(f'Missing required output {required}')
    if 'CNAME' in inventory and inventory['CNAME'].read_text().strip().lower() != 'sohrabmaleki.ir':
        errors.append('Custom domain was changed')
    if 'sitemap.xml' in inventory:
        try:
            tree = ET.parse(inventory['sitemap.xml'])
            urls = [n.text for n in tree.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
            for value in urls:
                if not value.startswith('https://sohrabmaleki.ir' + baseurl + '/'):
                    errors.append(f'Wrong sitemap domain/baseurl: {value}')
                    continue
                local_reference('sitemap.xml', 'sitemap', 'loc', urlsplit(value).path, False)
        except ET.ParseError as exc:
            errors.append(f'Invalid sitemap: {exc}')
    # Jekyll internals and authoring resources should never be published.
    for relative in inventory:
        if relative.startswith(('docs/', 'scripts/', 'vendor/', 'work/')) or relative in ('Gemfile', 'Gemfile.lock', 'README.md'):
            errors.append(f'Authoring/build file leaked into output: {relative}')
    for error in errors:
        print('ERROR:', error)
    print(f'Checked {len(parsed)} HTML pages, {checked} local references, '
          f'{sum(p.suffix.lower() == ".pdf" for p in inventory.values())} PDFs; {len(errors)} errors.')
    return 1 if errors else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--baseurl', default='')
    args = parser.parse_args()
    if not args.site.is_dir():
        parser.error(f'{args.site} is not a generated site directory')
    sys.exit(check(args.site, args.baseurl))
