# Adding and editing content

Content files are UTF-8 Markdown with YAML front matter between `---` lines.
Use stable descriptive filenames: renaming a collection file changes its individual
page URL. Existing archive pages and anchors remain unchanged.

## Common fields

- `title`: displayed title. Quote titles that contain a colon or special YAML characters.
- `order`: a number, sorted ascending within the section. New items appear automatically.
- `links`: optional resource links. Local paths start with `/files/`; external URLs
  start with `https://`. Put filenames with spaces in quotes; the template encodes them.
- `anchor`: optional stable HTML ID. Do not duplicate an ID on the same archive page.
- `published: false`: hides a draft. Remove this line or set it to `true` when ready.

Each resource has a `label` and a `url`; no icon or style configuration is needed.
If the file/recording is not available, omit `url` and set `unavailable: true`.
Never use an empty URL, `#`, or a directory as a download link.

Markdown supports paragraphs, emphasis, headings, lists, and links. For an internal
link in a body, use Jekyll's URL filter so repository-subpath previews also work:

```liquid
[Quantum Theory session 11]({{ '/talks.html#QT11' | relative_url }})
```

## Talks

Use `series: historical-papers`, `quantum-theory`, or `kinetic-theory`.
Use ISO dates (`date: 2026-10-04`), `venue`, `location`, and `poster`.
Upcoming talks are supported. Optional `date_display` overrides the displayed
date label while the ISO `date` remains available for metadata.
The displayed poster is also the enlargement target, preventing mismatched images.
Posters remain normal image links if JavaScript is disabled; with JavaScript they
open a keyboard-accessible dialog. Escape, the close button, or the backdrop closes it.

To add another series, create a file in `_talk_series/` with `title`, `key`, `anchor`,
and `order`; write its description in Markdown. Talks with the matching `series`
appear automatically, including in the series jump menu.

## Notes and research

Notes use `category: my-notes` or `papers-i-ve-found-interesting`.
Research uses `category: my-insights` and also appears on the existing Notes page.
Add another category in `_data/note_sections.yml` with `key`, `title`, `collection`,
and Markdown `description`. `collection` is `notes` or `research`.
Optional `after_links` is Markdown for a postscript shown after download buttons.

## Publications

Use `category: journal-articles`, `conference-proceedings`, or `preprints`, plus
`authors`. Write the bibliographic details in the Markdown body. Add categories in
`_data/publication_sections.yml`. The old template publications are preserved as
unpublished examples; replace them with real work before publishing them.

## Projects

Add a file in `_projects/`. A title, order, Markdown body, and optional resource links
are enough. No projects were invented during migration. Enable Projects navigation
in `_data/navigation.yml` when you add a project.

## CV and homepage

CV entries use the `group` keys in `_data/cv_sections.yml`. Optional `date_display`
and `subtitle` preserve the date and institution formatting. A `skills` list creates
a simple skills list. Body text is ordinary Markdown, including the awards list. Add section definitions in `_data/cv_sections.yml`.

Edit the homepage introduction in `index.md`, and the three homepage sections in
`_about/`. Their titles are optional and ordering uses `order`.

## Profile and navigation

Edit `_data/profile.yml` once to update the homepage profile and the shared footer. GitHub links to
the verified repository owner. Social profiles appear as text links only when a real URL is supplied.

Navigation is shared by every page. Toggle `enabled: true` for the prepared
Publications or Projects links. Research is already enabled, and the site name links to the homepage.

For literal bibliography labels at the beginning of a paragraph, write `\[1\]:`
so Markdown does not treat them as hidden link definitions. Escape literal backticks
in prose with a backslash when they are not intended as code delimiters.
