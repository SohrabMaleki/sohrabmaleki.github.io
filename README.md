# Sohrab Maleki's academic website

Jekyll + Markdown, using the original site design and GitHub Pages dependencies.
The custom domain remains **sohrabmaleki.ir**. Existing URLs (`index.html`,
`cv.html`, `notes.html`, `talks.html`, and `publications.html`) remain valid.

## Edit content

| Content | Where to edit | Where it appears |
| --- | --- | --- |
| Home introduction | `index.md` | Homepage |
| Home cards | `_about/*.md` | Homepage, ordered by `order` |
| CV entries | `_cv/*.md` | CV, grouped by `group`, ordered by `order` |
| Talks | `_talks/*.md` | Talks page, grouped by `series`, and individual pages |
| Study-circle introductions | `_talk_series/*.md` | Talks page, ordered by `order` |
| Notes and paper reviews | `_notes/*.md` | Notes page, grouped by `category`, and individual pages |
| Research write-ups | `_research/*.md` | My Insights on Notes, Research archive, and individual pages |
| Publications | `_publications/*.md` | Publications archive and individual pages |
| Projects | `_projects/*.md` | Projects archive and individual pages |
| Identity, email, social profiles | `_data/profile.yml` | Shared sidebar |
| Navigation | `_data/navigation.yml` | Shared header |
| Section names and introductions | `_data/*_sections.yml` | Corresponding archive |

To add content, copy the appropriate example in [docs/content-templates](docs/content-templates),
save it in the collection folder, and edit its front matter and Markdown body.
Templates use `published: false` so unfinished examples cannot appear on the live site.
Remove that line, or set it to `true`, when ready. See [the content guide](docs/content-guide.md).

Existing research is still shown under **My Insights** on `notes.html` to preserve
the existing presentation. The main navigation keeps Home, CV, Notes, and Talks.
Enable Publications, Research, or Projects in `_data/navigation.yml` when desired.
Their archive pages already exist at `/publications.html`, `/research.html`, and
`/projects.html`.

## Preview locally

Install Ruby 3.3 with Bundler (on Windows, use RubyInstaller with Devkit), then:

```sh
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000`. Restart the server after changing `_config.yml`.
Markdown edits rebuild automatically. To inspect unfinished content locally:

```sh
bundle exec jekyll serve --unpublished
```

## Verify before publishing

```sh
bundle exec jekyll build --strict_front_matter --trace
python scripts/check_site.py _site
bundle exec jekyll build --baseurl /preview --destination _site_preview --strict_front_matter
python scripts/check_site.py _site_preview --baseurl /preview
```

The check verifies local links, exact filename case, anchors, images, scripts,
stylesheets, PDF headers, generated sitemap, domain, and required pages. The same
checks run in `.github/workflows/check-site.yml` on pushes and pull requests.
External links require an internet connection and are not checked by this script.

## GitHub Pages and the domain

This repository remains compatible with GitHub Pages' native Jekyll build:

- Keep `CNAME` at the repository root with `sohrabmaleki.ir`.
- Keep `url: https://sohrabmaleki.ir` and `baseurl: ""` in `_config.yml`.
- Do not add `.nojekyll`; Markdown and Liquid must be processed.
- Keep Pages configured to **Deploy from a branch**, **main**, **/ (root)**,
  if that is the existing configuration. The check workflow verifies the site;
  it does not replace the existing Pages deployment.
- Commit and push the source files, including `Gemfile.lock`. Do not commit `_site/`
  or `vendor/`. GitHub builds and publishes the site from those sources.
- Keep existing DNS records and custom-domain settings. No DNS change is needed.
- `jekyll-sitemap` regenerates `sitemap.xml`, including collection pages and PDFs.
- The Google verification HTML remains unchanged.

No custom Jekyll plugins, themes, JavaScript build pipeline, or CMS are required.

## Organization

`_layouts/` contains page layouts. `_includes/` contains the shared head, navigation,
sidebar, footer, poster dialog, and content cards. Original shared styles remain in
`css/style.css`; page-specific styles formerly embedded in HTML are now in
`css/home.css`, `css/cv.css`, and `css/notes.css`. `images/` and `files/` retain all
original filenames and assets so existing download URLs continue to work.

See [migration notes](docs/migration-notes.md) for existing defects corrected and
items that still need real content or a missing asset.

See [the migration verification report](docs/verification.md) for build, content,
browser, asset, and external-link results.
