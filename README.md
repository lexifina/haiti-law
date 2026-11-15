# Haiti: law history in git

The law of Haiti as a git history: one file per article, one commit per version on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every article; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Haiti's national law, which global-law reads at `haiti/national/acts/`.

**What is in it now:** three acts, with four versions: the Constitution of 29 March 1987, as ratified and as amended in 2011 (the corrected text published on 19 June 2012); the Code du travail, in one version; and the decree of 9 October 2015 on civil pensions, in one version. That is all the law this repository holds today.

Each act has its own folder, with one file per article (`code-du-travail/art-001.md` is Article 1 of the Code du travail; the Constitution's Article 1.1 is `constitution/art-001-01.md` and its preamble `constitution/preambule.md`); the pension decree is one file, `decret-pension-civile-2015/texte-integral.md`. Each folder's `README.md` lists its articles.

The text is in French, as the sources print it. Haitian Creole texts and English translations are not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 1 of the Code du travail | `git log -p --word-diff -- code-du-travail/art-001.md` |
| Which act wrote each line of Article 1? | `git blame code-du-travail/art-001.md` |
| Every version of the Code du travail, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- code-du-travail` |
| Article 1 as in force on 1 January 2015 | `python tools/on.py 2015-01-01 code-du-travail art-001` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Haitian law](https://global-law.lexifina.com/v1/try_claude?country=haiti)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=haiti)**: the same question in ChatGPT.
- **[Search Haitian law on our site](https://lexifina.com/law?country=haiti&q=cong%C3%A9+annuel)**: a search for "congé annuel", with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=cong%C3%A9+annuel&jurisdiction=haiti)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in French or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add haiti/national/acts
python3 tools/law.py show 2026-01-01 haiti/national/acts/code-du-travail/art-001.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/Port-au-Prince, on the day the version took effect, and carries it in its `In-force:` trailer:

- the Constitution: 29 March 1987, the day it was ratified by referendum (Article 298 puts it in force on publication in Le Moniteur; the ratification day is used), then 19 June 2012, the Moniteur extraordinaire that published the corrected text of the 2011 amendment; the first publication of 13 May 2011 differed from what the Assembly approved and is not used;
- the Code du travail: 31 August 2010, the date of the copy used, not a day the law took effect; the copy reflects the Decree of 24 February 1984 and the Loi du 5 juin 2003;
- the pension decree: 26 October 2015, its publication day in Le Moniteur no 205, from which its Article 41 applies it.

The 1987 text is credited to the Constitution itself, and the 2012 version to the 2011 constitutional amendment, and that commit changes only the articles the source marks as amended. The Code du travail and the pension decree, each held in one text, are the "oldest version available", credited to the source that published the text.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and compares it with the corpus: 0 mismatches. A second build from the same corpus gave the same hashes. Both are in `REPRODUCE.md`.
- Each version names its source page and the sha256 of the bytes it was read from (`data/versions.json`).
- No merge commits, no commit dated after the build, and every commit's trailers parse.

## What it does not show

- **The official gazette.** Le Moniteur has no comprehensive online archive; the Constitution and the Code du travail are unofficial third-party copies, so check them against Le Moniteur for anything that matters.
- **Any other Haitian law**, such as the Code civil and the Code pénal. The Loi portant prévention et répression de la corruption (Le Moniteur no 87, 9 May 2014) is prepared but stays outside the record until an independent review is complete.
- **Later changes**: to the Constitution other than the 2011 amendment, and to the Code du travail or the pension decree after the texts used.
- **Headings** of the Constitution and the Code du travail: titles, chapters and sections are left out; each article is a file.
- **Seven articles of the Code du travail** (426, 483, 505 and 507 to 510): the copy prints only a summary, and those files say the source does not give the text.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Digithèque MJP](https://mjp.univ-perp.fr/constit/ht1987.htm), Université de Perpignan | Third-party copy of the Constitution | yes, the 1987 text and the [amended text](https://mjp.univ-perp.fr/constit/ht2011.htm) | Unofficial; the amended page marks repealed and new words |
| [CEPAL, Gender Equality Observatory](https://oig.cepal.org/sites/default/files/2003_codtravail_hti.pdf) | Third-party copy of the Code du travail | no, one copy (2010) | Unofficial |
| [Le Moniteur no 205](https://www.mef.gouv.ht/storage/app/uploads/public/622/0fc/989/6220fc98951f1364533445.pdf) (Ministère de l'Économie et des Finances) | Official gazette | no, as published | The 2015 pension decree |

## Licence

See `LICENSE`. Haiti's Decree of 12 October 2005 on copyright (Article 5) excludes official legislative texts from protection; the third-party hosts are credited as the source of the bytes. The arrangement, tables, commit messages and tools are CC BY 4.0.

No AI model wrote, translated or corrected legal text; the scripts were written by an AI model, and a model identified document boundaries and source dates (see `REPRODUCE.md`).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
