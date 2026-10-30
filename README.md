# Haiti: law history in git

The Constitution and the Code du travail of Haiti as a git repository: one file per article, one commit per change, with the text in French (the official language of the Moniteur). It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution de la République d'Haïti, 29 mars 1987 | 2 | The original text of 29 March 1987, then the text as amended, published in Le Moniteur extraordinaire of 19 June 2012 |
| `code-du-travail/` | Code du travail (Décret du 24 février 1984, with the Loi du 5 juin 2003) | 1 | One version, the oldest available: the copy published by CEPAL, dated 31 August 2010 (its file date) |

That is all the law this repository holds today. **No other Haitian law is in it** yet (the Code civil, the Code pénal and other statutes): Le Moniteur is not online.

## Where the text comes from

Haiti's official gazette, Le Moniteur, is not online, so the text is a **third-party copy**: the Digithèque of the Université de Perpignan (mjp.univ-perp.fr), which carries the 1987 text and a marked version of the amended text. Haiti's copyright Decree of 12 October 2005 (Article 5) excludes official legislative texts from protection; the clause is quoted in `LICENSE`. The host is credited as the source of the bytes. Its pages are unofficial, so check them against Le Moniteur for anything that matters.

The Code du travail is likewise a third-party copy, published by the Gender Equality Observatory of the United Nations Economic Commission for Latin America and the Caribbean (CEPAL, oig.cepal.org). It prints only a bracketed summary for articles 426, 483, 505 and 507 to 510; those files say the source does not give the text.

## Dates

- The first version is dated **29 March 1987**: the Constitution was ratified by referendum on that day and came into force on publication in Le Moniteur (Article 298).
- The second is dated **19 June 2012**, the Moniteur extraordinaire that published the corrected text of the 2011 constitutional amendment. The first publication of 13 May 2011 differed from what the Assembly approved and is not used.
- The amendment's commit is credited to "Loi constitutionnelle portant amendement de la Constitution de 1987 (2011)" and holds only articles the host marks as changed. Where the host's two pages differ in unmarked words (for example silent spelling corrections), the 1987 text is kept.
- The host notes that the 2012 text leaves some articles (63, 68, 78, 90.1, 92, 92.1, 92.3, 95, 218, 264, 267.2) as in 1987; this repository follows the host's text.

## What it does not show

- Titles, chapters and sections headings: each article is a file; the preamble is `preambule.md`.
- Any change to the Constitution other than the 2011 amendment. Later changes, if any, are not in the host's text.
- Any other Haitian law, and any change to the Code du travail after the copy used.

## How it is checked

- Every version is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each version names its source page and the sha256 of the bytes it was read from (`data/versions.json`).
