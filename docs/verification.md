# Jekyll migration and verification report

Implemented on 4 October 2026 in `P:\MyWebPage\sohrabmaleki.github.io`.

## Result

The manually maintained HTML pages have been replaced with Markdown pages,
reusable layouts/includes, and collections. The shared design, original archive
URLs, custom domain, and asset paths are preserved.

- 23 talks in `_talks/`.
- 11 notes/paper reviews in `_notes/`.
- 3 research write-ups in `_research/`, still shown under My Insights on Notes.
- Three old placeholder publications retained as unpublished Markdown drafts.
- `_projects/` and the Projects archive are ready for real content.
- Homepage and CV content also use Markdown collections.
- One shared navigation, sidebar, head, footer, and poster dialog replace duplicated HTML.
- Content templates, a maintenance guide, a reproducible dependency lockfile, and
  a GitHub Actions validation workflow are included in the repository.

## Verification results

| Check | Result |
| --- | --- |
| Production build | Passed with Jekyll 3.10.0, strict front matter, safe mode, and the sitemap plugin |
| Repository-subpath build (`/preview`) | Passed |
| Generated HTML | 46 pages, including the unchanged Google verification page |
| Local links/assets/anchors | 676 references checked per build; zero errors |
| Original paragraphs | All 95 preserved, compared paragraph by paragraph |
| Original titles | All 63 preserved, compared in order |
| Browser checks | 114 page/viewport combinations; zero errors |
| Screen widths | 320, 390, 768, 1024, and 1440 pixels; no horizontal overflow |
| Desktop design | Original header, portrait, sidebar, and content geometry match within 1 pixel; typography and colors match |
| PDF downloads | All 45 served successfully with PDF content and MIME type |
| Generated assets | All 75 visible files/images match the source bytes |
| Original assets | Git comparison confirms all original files/images, `CNAME`, and verification HTML are unchanged |
| Poster interactions | Mouse, keyboard, Escape, close button, backdrop, focus restoration, and no-JavaScript fallback passed |
| Existing anchors | Session 11, H-Theorem review, and all three study-circle anchors preserved |
| Markdown-only additions | Five isolated additions passed: talks, notes, research, publications, projects |
| Future talks and drafts | Upcoming talk generated; unpublished drafts excluded |
| External links | 17 of 21 returned successful HTTP responses; four could not be confirmed in this environment |
| Repository whitespace checks | Passed |

The build engine version matches the [GitHub Pages dependency list](https://pages.github.com/versions/).
Verification used the unmodified Jekyll rendering engine through its Ruby build API.
The temporary portable Windows runtime lacked the compiler needed for optional
live-preview native dependencies, so a full local `bundle install`/`jekyll serve`
was not run. Normal local preview instructions use RubyInstaller with Devkit, and
the committed validation workflow performs the complete Bundler build on Linux.

## Corrected existing defects

- Fixed the analogue-gravity PDF link, which previously pointed to a directory.
- Fixed the Jaynes Information Theory PDF filename case for Linux hosting.
- Fixed the Quantum Theory 4 poster opening the wrong image.
- Empty recording links now say “not yet available” instead of reloading the page.
- Missing `files/qt4.pdf` is marked unavailable; no replacement PDF was invented.
- The GitHub social link uses the verified repository owner; other placeholder
  profiles remain inactive until real URLs are supplied.
- The old example publications remain unpublished so they are not presented as real work.
- The sitemap is generated automatically, and narrow layouts wrap without overflow.

Quantum Theory 5 still links to `qt3.pdf`, and Quantum Theory 7 still links to
`qt6.pdf`, as in the original. These valid existing targets were retained because
the intended use of shared notes requires the author's judgment.

## External links requiring a manual check

These existing URLs were retained. Their automated checks encountered TLS failures,
which do not establish whether the content itself has moved or disappeared:

- [http://ResonanceOly.ir](http://ResonanceOly.ir) — <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1010)>
- [https://mamwad.org](https://mamwad.org) — <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)>
- [https://physics.sharif.edu/~vahid/teachingThermoSM.html](https://physics.sharif.edu/~vahid/teachingThermoSM.html) — <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'physics.sharif.edu'. (_ssl.c:1010)>
- [https://www.damtp.cam.ac.uk/user/tong/kinetic.html](https://www.damtp.cam.ac.uk/user/tong/kinetic.html) — <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>

## Publishing state

The migration is complete in the local working tree. It has not been committed,
pushed, or published. DNS and GitHub Pages settings were not changed.
Keep the existing branch-based Pages deployment pointed at `main` and the repository
root; commit and push the source when ready. `CNAME` remains `sohrabmaleki.ir`,
and `_config.yml` keeps the HTTPS domain with an empty base URL.

See `README.md`, `docs/content-guide.md`, and `docs/content-templates/` in the repository
for maintenance instructions. The validation workflow checks future pushes and PRs.
