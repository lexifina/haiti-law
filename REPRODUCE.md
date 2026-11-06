# How this repository was made (Haiti)

This file is written by the build on 2026-11-06, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Digithèque de matériaux juridiques et politiques (MJP), Université de Perpignan: Haïti, Constitution 1987 | <https://mjp.univ-perp.fr/constit/ht1987.htm> | 2026-10-30 | Third-party copy of an official text; see LICENSE (Haiti copyright Decree of 2005, art. 5). |
| Digithèque MJP: Haïti, Constitution 1987 amendée (Moniteur extraordinaire du 19 juin 2012) | <https://mjp.univ-perp.fr/constit/ht2011.htm> | 2026-10-30 | As above. |
| CEPAL, Observatorio de Igualdad de Género: Code du travail haïtien (Décret du 24 février 1984 et Loi du 5 juin 2003) | <https://oig.cepal.org/sites/default/files/2003_codtravail_hti.pdf> | 2026-10-30 | Official legislative text, excluded from copyright protection by Article 5 of the Haitian Decree of 12 October 2005 on copyright (see LICENSE); the host is credited as the source of the bytes. |
| Le Moniteur, no 205, 26 octobre 2015, official PDF hosted by the Ministère de l'Économie et des Finances | <https://www.mef.gouv.ht/storage/app/uploads/public/622/0fc/989/6220fc98951f1364533445.pdf> | 2026-11-05 | Official legislative text; see Haiti LICENSE, 2005 copyright decree, article 5. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution de la République d'Haïti (1987) | 2 | 1987-03-29 to 2012-06-19 |
| `code-du-travail` | Code du travail (Décret du 24 février 1984) | 1 | 2010-08-31 to 2010-08-31 |
| `decret-pension-civile-2015` | Décret du 9 octobre 2015 modifiant celui du 18 février 2011 sur la pension civile de retraite | 1 | 2015-10-26 to 2015-10-26 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 1 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-06.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 6 tags.

## Dates

Each commit is dated at noon (America/Port-au-Prince) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution du 29 mars 1987, art. 298: elle entre en vigueur dès sa publication au Moniteur. https://mjp.univ-perp.fr/constit/ht1987.htm

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `b83a4e8868557b4fe16047d406efd7cec71a731bbabaae88874cd1ddd0ff8c74` (493826 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `3024ff164c261807dfc4d5b7b1b4a2cde4357da1`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

4 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 4 history commits and 6 tags (history tip `d76a583c740d62d4d2d321e33f4de525364ed669`).

## Decisions made by hand

- The text is a third-party copy from the MJP digital library (Université de Perpignan); the national copyright act (Decree of 12 October 2005, art. 5 para. 1) excludes official legislative texts from protection. Titles, chapters and sections headings of the Constitution are left out; each article is a unit.
- The 1987 version is the original text from the host page ht1987.htm, dated 1987-03-29 (ratification by referendum; in force on publication in Le Moniteur, art. 298).
- The amended version is dated 2012-06-19, the Moniteur extraordinaire that published the corrected text of the 2011 constitutional amendment (the first, flawed publication of 13 May 2011 is not used). It is read from the host page ht2011.htm, which marks repealed words with strike-through and new words with underline: struck words are dropped and underlined words kept.
- Articles the host page leaves unmarked keep the 1987 text taken from ht1987.htm, so that small differences between the host's two pages (for example silent spelling corrections) are not credited to the amendment. Articles the 2011 page leaves wholly struck were removed.
- The host notes that the 2012 text leaves articles 63, 68, 78, 90.1, 92, 92.1, 92.3, 95, 218, 264 and 267.2 as in 1987 (mandate lengths of 4 years); the page's own text is followed.
- The host page is itself unofficial; the official source is Le Moniteur, which is not online. Check against Le Moniteur for anything that matters.
- Code du travail: one version, the copy published by CEPAL's Gender Equality Observatory (a third-party copy of the official text, which Le Moniteur does not publish online), credited to that host as "oldest version available" and dated 2010-08-31, the creation date of its PDF. It reflects the Decree of 24 February 1984 and the Loi du 5 juin 2003; later changes, if any, are not applied.
- Code du travail: one unit per article (art-NNN). Some articles open with a bare number ("60.") rather than "Article 60."; a bare number is read as an article only when it is the next in sequence and opens a paragraph. Chapter IX, printed as its heading and "(Abrogé par la loi du 5 juin 2003)", is the single unit art-341-356. The copy prints only a bracketed summary for art-426, art-483, art-505, art-507-510; those units read "[La source ne donne pas le texte de cet article.]". The copy prints "Article 503." a second time after article 506; it is kept as printed, keyed art-503-2. Headings and the closing note on the 2003 law are left out; paragraphs follow the blank lines and sentence ends of the copy.
- The official Gazette PDF states 26 October 2015 in its running heading; Article 41 expressly applies from publication and Article 44 orders publication and execution. No later consolidation date is stated in this source.
- The decree's preamble, headings and Articles 1–44 are transcribed from the official PDF text layer, pages 26–35, as a single-file act. Signature images and a separate following order are outside this act's normative text.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- none
- A model identified document boundaries and source dates; no model-generated or model-corrected words appear in the law text.
