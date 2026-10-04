# Academic website redesign

Implemented in `P:\MyWebPage\sohrabmaleki.github.io`.

## Design

- Warm white background, dark serif headings, muted green links, and readable system-font body text.
- A single centered layout with generous spacing and subtle section dividers.
- A compact homepage profile with the original portrait and contact links.
- Reading pages display content directly, with no repeated sidebar.
- Clean CV sections, text resource links, and small optional talk posters.
- Research is directly accessible through the shared navigation.
- Collection titles link to individual pages, which include a link back to the archive.
- One shared stylesheet; no page-specific CSS files, external icon fonts, or inline styles.
- Markdown files need no `styles`, `icon`, or CSS-class annotations.

## Preserved

All 56 existing content records retain their prose and academic metadata.
All 95 original paragraphs and 63 original titles remain visible.
URLs, anchors, Markdown collections, unpublished drafts, CNAME, PDFs, images,
videos, LaTeX files, and Google verification remain intact.

## Verification

- GitHub Pages' Jekyll 3.10 engine builds successfully with strict front matter.
- Root and `/preview` subpath builds pass the local-link checker.
- 46 generated HTML pages, 702 local references, and 45 PDFs; no broken local links.
- 122 browser page/viewport checks at 320, 390, 700, 768, 1024, and 1440 pixels.
- No horizontal overflow, JavaScript errors, failed local responses, or inline styling.
- Every content page has one main heading and one stylesheet.
- Active navigation, title links, back links, skip navigation, and the session 11 anchor work.
- Poster mouse/keyboard interaction, Escape, close button, backdrop, focus restoration,
  and no-JavaScript image fallback work.
- All 45 PDFs download successfully; all 75 visible generated assets retain their source bytes.
- The Markdown-only authoring fixture verifies adding new talks, notes, research,
  publications, and projects without editing templates.

This is a local redesign. It has not been committed, pushed, or published.
Existing missing/unavailable resources remain as documented in the initial migration report.
