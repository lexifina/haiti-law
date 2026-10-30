# How this repository was made (Haiti)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Digithèque de matériaux juridiques et politiques (MJP), Université de Perpignan: Haïti, Constitution 1987 | <https://mjp.univ-perp.fr/constit/ht1987.htm> | 2026-10-30 | Third-party copy of an official text; see LICENSE (Haiti copyright Decree of 2005, art. 5). |
| Digithèque MJP: Haïti, Constitution 1987 amendée (Moniteur extraordinaire du 19 juin 2012) | <https://mjp.univ-perp.fr/constit/ht2011.htm> | 2026-10-30 | As above. |
| CEPAL, Observatorio de Igualdad de Género: Code du travail haïtien (Décret du 24 février 1984 et Loi du 5 juin 2003) | <https://oig.cepal.org/sites/default/files/2003_codtravail_hti.pdf> | 2026-10-30 | Official legislative text, excluded from copyright protection by Article 5 of the Haitian Decree of 12 October 2005 on copyright (see LICENSE); the host is credited as the source of the bytes. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution de la République d'Haïti (1987) | 2 | 1987-03-29 to 2012-06-19 |
| `code-du-travail` | Code du travail (Décret du 24 février 1984) | 1 | 2010-08-31 to 2010-08-31 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 1 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 5 tags.

## Dates

Each commit is dated at noon (America/Port-au-Prince) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution du 29 mars 1987, art. 298: elle entre en vigueur dès sa publication au Moniteur. https://mjp.univ-perp.fr/constit/ht1987.htm

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `4c57869baf38be2a2bd811c88a8df988f7d84c3addb9d62e9188442a21ad34e4` (463422 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

3 versions of 2 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 3 history commits and 5 tags (history tip `75013638b95dd40e4652f47a3739e6bc630aa3ae`).

## Decisions made by hand

- The text is a third-party copy from the MJP digital library (Université de Perpignan); the national copyright act (Decree of 12 October 2005, art. 5 para. 1) excludes official legislative texts from protection. Titles, chapters and sections headings of the Constitution are left out; each article is a unit.
- The 1987 version is the original text from the host page ht1987.htm, dated 1987-03-29 (ratification by referendum; in force on publication in Le Moniteur, art. 298).
- The amended version is dated 2012-06-19, the Moniteur extraordinaire that published the corrected text of the 2011 constitutional amendment (the first, flawed publication of 13 May 2011 is not used). It is read from the host page ht2011.htm, which marks repealed words with strike-through and new words with underline: struck words are dropped and underlined words kept.
- Articles the host page leaves unmarked keep the 1987 text taken from ht1987.htm, so that small differences between the host's two pages (for example silent spelling corrections) are not credited to the amendment. Articles the 2011 page leaves wholly struck were removed.
- The host notes that the 2012 text leaves articles 63, 68, 78, 90.1, 92, 92.1, 92.3, 95, 218, 264 and 267.2 as in 1987 (mandate lengths of 4 years); the page's own text is followed.
- The host page is itself unofficial; the official source is Le Moniteur, which is not online. Check against Le Moniteur for anything that matters.
- Code du travail: one version, the copy published by CEPAL's Gender Equality Observatory (a third-party copy of the official text, which Le Moniteur does not publish online), credited to that host as "oldest version available" and dated 2010-08-31, the creation date of its PDF. It reflects the Decree of 24 February 1984 and the Loi du 5 juin 2003; later changes, if any, are not applied.
- Code du travail: one unit per article (art-NNN). Some articles open with a bare number ("60.") rather than "Article 60."; a bare number is read as an article only when it is the next in sequence and opens a paragraph. Chapter IX, printed as its heading and "(Abrogé par la loi du 5 juin 2003)", is the single unit art-341-356. The copy prints only a bracketed summary for art-426, art-483, art-505, art-507-510; those units read "[La source ne donne pas le texte de cet article.]". The copy prints "Article 503." a second time after article 506; it is kept as printed, keyed art-503-2. Headings and the closing note on the 2003 law are left out; paragraphs follow the blank lines and sentence ends of the copy.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- none
