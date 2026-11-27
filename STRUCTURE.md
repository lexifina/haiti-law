# Structure du dépôt / Repository layout

Un dossier par texte, un fichier par article (`art-001.md`, `art-002.md`, … ; `art-012-bis.md`), plus `README.md`
(source, date, version, couche texte), `visas.md` (visas et considérants) et `signatures.md` quand le texte en a. Un
texte sans articles repérables tient en un fichier, `texte-integral.md`. Au plus 1 000 entrées par dossier.

| Dossier | Contenu |
| --- | --- |
| `constitution/` | Constitution du 29 mars 1987, telle que ratifiée et telle qu’amendée (texte publié le 19 juin 2012) |
| `codes/<code>/` | Codes : `code-du-travail/`, `code-penal/`, `code-d-instruction-criminelle/`, `code-des-investissements/`, … ; chaque nouvelle version d’un code remplace la précédente dans le même dossier (une version = un commit) |
| `lois/<année>/<mm>-<jj>-<objet>/` | Lois, rangées par l’année et le jour de leur date (« Loi du 12 mars 2014 … » → `lois/2014/03-12-…`) |
| `decrets/<année>/<mm>-<jj>-<objet>/` | Décrets |
| `decrets-lois/<année>/<mm>-<jj>-<objet>/` | Décrets-lois (années 1930-1950) |
| `arretes/<année>/<mm>-<jj>-<objet>/` | Arrêtés |
| `corpus.json` | La liste des textes ajoutés par le collecteur (`ht/national/acts`) : dossier, nature, date, intitulé, source, couche texte, nombre d’articles |

Les actes haïtiens ne portent pas de numéro : ils sont désignés par leur nature et leur date (« Décret du 17 mai 2005
portant … »), d’où le jour dans le nom du dossier. `<objet>` reprend les premiers mots de l’intitulé, sans accents.

## Dates

Chaque commit est daté à midi, heure America/Port-au-Prince, du jour retenu dans son trailer `In-force:` ; le trailer
`In-force-basis:` dit pourquoi. Pour les lois, décrets et arrêtés, c’est la date de l’acte dans son intitulé : les
sources ne donnent pas le jour de publication au Moniteur. Pour les codes consolidés par une source tierce, c’est le
jour de la modification la plus récente que le texte cite lui-même. Avant 1970, le commit porte le 1970-01-01 et le
vrai jour figure dans le sujet et dans `In-force:`.

## Sources (ordre de préférence pour un même texte)

1. Copies officielles du Moniteur publiées par le Ministère de l’Économie et des Finances (mef.gouv.ht) et la Direction
   générale du Budget (budget.gouv.ht), rubrique « Cadre réglementaire ».
2. FAOLEX (FAO) : `Source-status: secondary copy (FAOLEX, …)`.
3. haitijustice.com (Centre de recherche et d’information juridiques, CRIJ) : site fermé, copies de la Wayback Machine,
   `Source-status: secondary copy (haitijustice.com …)`.
4. Le Moniteur numérisé par la Digital Library of the Caribbean (University of Florida), 1845–1983 : couche texte OCR de
   la bibliothèque, `Source-status: secondary copy (Digital Library of the Caribbean …)`, `Text-source: publisher OCR`.

Seuls les PDF dont la couche texte est lisible et complète sont repris (pas d’OCR de notre part) ; une couche posée par
l’éditeur sur un scan est signalée `Text-source: publisher OCR`.

---

One folder per text, one file per article; laws, decrees, decree-laws and orders filed by the year and day of their
date (Haitian acts are not numbered); codes in `codes/<code>/`, each new version replacing the last. Commits are dated
noon America/Port-au-Prince on the `In-force:` day (the act's own date; for third-party consolidated codes, the day of
the latest amendment the text cites); pre-1970 days are stamped 1970-01-01 with the real day in the subject.
