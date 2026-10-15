---
name: icon-finder
description: "Offline, meaning-based icon search across Lucide 1.33, Tabler 3.49, Phosphor 2.1 and Heroicons 2.2 (9,120 icons, English + Persian queries): search, recommend a consistent set for UI slots, get SVG + import line, local HTML preview, and verify an icon exists in the project's installed package. Manual — invoke with /icon-finder."
disable-model-invocation: true
---

# Icon Finder

Local replacement for hosted icon-search MCP servers. No network, no installs, stdlib Python only.

```bash
python "$HOME/.claude/skills/icon-finder/scripts/icons.py" <command> ...
```
(If `python` is missing try `py -3`.)

## Commands

| Need | Command |
|---|---|
| Find icons by meaning (English or Persian) | `search "settings" --lib lucide -n 8` · `search "سبد خرید"` |
| One consistent icon per UI slot | `recommend "داشبورد, کاربران, سفارش‌ها, گزارش‌ها, تنظیمات, خروج" --lib lucide` |
| SVG + import line for a known icon | `get lucide:house [--size 20] [--color "#111"]` |
| Visual comparison page | `preview "camera scan" --out <project-or-scratch>/icon-preview.html` (or `preview lucide:house phosphor:house ...`) |
| Check names exist in the project's installed package | `verify House LogOut --lib lucide --project <project dir>` |
| Libraries, versions, licences, import style | `libs` |

`--lib`: `lucide`, `tabler`, `phosphor`, `heroicons` (outline+solid), `heroicons-outline`, `heroicons-solid`, comma lists, or `all` (default for search). Add `--json` to search/recommend/get for machine output.

## Rules

1. Library = the one the project already uses (check `package.json`). Default `lucide` (installed in this user's projects as `lucide-react`). One library per surface — `recommend` keeps every slot in one library.
2. Never invent an icon name. Use only names returned here, and run `verify` against the project before writing imports.
3. Show the user: icon id, library, short reason. Paste SVG only when the project uses raw SVG; otherwise use the import line.
4. Accessibility: decorative icon beside text → `aria-hidden="true"`; icon-only button → accessible name on the button (see ui-ux-pro-max `--domain icons`).
5. `preview` writes a local HTML file; open it for the user (or publish as an Artifact only if asked).
6. No good hit → say so and rephrase (synonym, broader word). Persian words not in `data/synonyms.json` fall back to no match — add the word there if it recurs.

## Data and updates

- `data/icons.json.gz` — built by `scripts/build_index.py` from pinned npm tarballs fetched once with `npm pack` (data only, no package scripts run): `lucide-static@1.33.0` (matches `lucide-react` 1.33.0; all 1,776 exports verified), `@tabler/icons@3.49.0` (outline), `@phosphor-icons/core@2.1.1` (regular SVGs; metadata parsed from the JS file with regexes, never executed), `heroicons@2.2.0` (24px outline + solid). Run the builder with the extracted package folders (see `scripts/build_index.py`).
- `data/synonyms.json` — `en` concept synonyms, `fa` Persian → concept map (plurals ‌ها/ات/ان are stripped), `heroicons_tags` (Heroicons ships no tags).
- Export names: Lucide `House`; Tabler `IconHome`; Phosphor `HouseIcon` (2.1+ suffixed names); Heroicons `HomeIcon` from `@heroicons/react/24/outline|solid`.
- Update: `npm pack <pkg>@<new version>` into a review folder, review the diff, extract, adjust versions in `build_index.py`, rebuild, re-run the lucide export check.
- Licences in `data/licenses/` (Lucide ISC; Tabler, Phosphor, Heroicons MIT).
