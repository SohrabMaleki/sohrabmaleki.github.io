# Migration notes

## Preserved

- Homepage, CV, Notes, and Talks prose, titles, section order, and content order.
- 23 talk records, 11 notes/paper reviews, and 3 research records.
- Existing archive URLs and `QT11`, `H-Thm-Violation`, `Historical-Papers`,
  `Quantum-Theory`, and `Kinetic-Theory` anchors.
- Custom-domain `CNAME`, Google verification file, all PDFs, images, videos,
  and LaTeX files with their existing paths and bytes.
- Original desktop layout, palette, typography, portrait, card styles, poster sizes,
  and responsive breakpoints. Page-specific inline CSS moved to separate stylesheets.

## Corrected existing defects

- The analogue-gravity review linked to the `files/` directory. It now links to
  the matching existing `files/AnalogBEC.pdf`.
- The Jaynes Information Theory review used `Information THeory...pdf`, which would
  fail on Linux. The link now uses the exact existing filename.
- Quantum Theory lecture 4 displayed `qt4-poster.jpg` but enlarged `qt3-poster.jpg`.
  The shared poster include now uses one image path for both.
- Empty recording URLs no longer reload the page. They display “not yet available”.
- `files/qt4.pdf` is missing from the repository. Its download is explicitly marked
  unavailable. Add the file and a real link when available.
- All existing `#` social links were placeholders. GitHub now links to the repository
  owner; the other social icons are inactive until real profile URLs are supplied.
- The old publication page contained three fabricated template titles and `#` links.
  They are retained in `_publications/example-*.md` with `published: false` and are
  not represented as actual publications on the public archive.
- Email is a functional mail link. Navigation and poster links support keyboard use.
- The obsolete handwritten sitemap is replaced with `jekyll-sitemap` output.
- Narrow screens allow content and download groups to wrap without horizontal scrolling.

## Content needing the author's judgment

Two talks have existing PDF targets that differ from their lecture numbers:
Quantum Theory 5 links to `qt3.pdf`, and Quantum Theory 7 links to `qt6.pdf`.
Those targets have been retained because the original author may have intended
shared notes. Existing `qt5.pdf` and `qt7.pdf` have not been substituted without evidence.

The supplied repository had no dedicated project records and no real publication
records. The collections and archives are ready for new Markdown content.

## Deployment

The migration is implemented in the local repository. It does not change DNS,
GitHub settings, or publish a new version by itself. The existing branch-based
GitHub Pages deployment can build this source after it is committed and pushed.
The added workflow verifies both the custom-domain root build and a subpath build.
