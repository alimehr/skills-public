"""icon-finder: offline, meaning-based icon search over Lucide, Tabler, Phosphor and Heroicons.

Usage:
  icons.py search "<query>" [--lib L] [-n N] [--json]
  icons.py recommend "slot1, slot2, ..." [--lib L] [--json]
  icons.py get <lib:name> [--size PX] [--color C] [--json]
  icons.py preview ("<query>" | lib:name lib:name ...) [--lib L] [-n N] --out FILE.html
  icons.py verify <ExportOrName> [...] --lib L --project DIR
  icons.py libs
Stdlib only, no network. Data: ../data/icons.json.gz (built from pinned npm packages, see SKILL.md).
"""
import argparse, gzip, json, math, pathlib, re, sys
from collections import Counter
from html import escape

HERE = pathlib.Path(__file__).resolve().parent.parent
DATA = HERE / "data"
LIB_ALIASES = {"heroicons": ["heroicons-outline", "heroicons-solid"], "hero": ["heroicons-outline", "heroicons-solid"],
               "ph": ["phosphor"], "tabler": ["tabler"], "lucide": ["lucide"], "phosphor": ["phosphor"],
               "heroicons-outline": ["heroicons-outline"], "heroicons-solid": ["heroicons-solid"]}


def out(text):
    sys.stdout.buffer.write((text + "\n").encode("utf-8"))


def load():
    with gzip.open(DATA / "icons.json.gz", "rt", encoding="utf-8") as f:
        data = json.load(f)
    syn = json.loads((DATA / "synonyms.json").read_text("utf-8"))
    return data, syn


def stems(word):
    w = word.lower()
    forms = {w}
    if len(w) > 3 and w.endswith("ies"):
        forms.add(w[:-3] + "y")
    elif len(w) > 3 and w.endswith("es") and w[-3] in "sxz":
        forms.add(w[:-2])
    elif len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        forms.add(w[:-1])
    return forms


def words(text):
    return [w for w in re.split(r"[^0-9a-z]+", text.lower()) if w]


class Index:
    def __init__(self, data, syn):
        self.libs = data["libs"]
        self.icons = data["icons"]
        for ic in self.icons:
            if ic["lib"].startswith("heroicons") and ic["name"] in syn.get("heroicons_tags", {}):
                ic["tags"] = syn["heroicons_tags"][ic["name"]].split()
        self.syn_en = {k: v for k, v in syn["en"].items()}
        self.syn_fa = sorted(((self.fa_norm(k), v) for k, v in syn["fa"].items()), key=lambda kv: -len(kv[0]))
        self.fa_dict = dict(self.syn_fa)
        self.fields = []
        df = Counter()
        for ic in self.icons:
            name = set().union(*(stems(w) for w in words(ic["name"]))) if words(ic["name"]) else set()
            tagw = set()
            for t in ic["tags"]:
                for w in words(t):
                    tagw |= stems(w)
            cat = set()
            for c in ic["cat"]:
                for w in words(c):
                    cat |= stems(w)
            f = {"name": name, "tags": tagw, "cat": cat, "tagphrases": {t.lower() for t in ic["tags"]}}
            self.fields.append(f)
            for term in name | tagw | cat:
                df[term] += 1
        n = len(self.icons)
        self.idf = {t: math.log(1 + n / c) for t, c in df.items()}
        self.by_id = {f'{ic["lib"]}:{ic["name"]}': i for i, ic in enumerate(self.icons)}

    @staticmethod
    def fa_norm(text):
        text = text.replace("ي", "ی").replace("ك", "ک").replace("ة", "ه")
        return re.sub(r"[ً-ْٰ]", "", text)

    def fa_lookup(self, word):
        w = word.replace("‌", "")
        cands = [word, w]
        for suf in ("‌های", "‌ها", "های", "ها", "ات", "ان", "ی"):
            if word.endswith(suf) and len(word) - len(suf) >= 2:
                cands.append(word[: -len(suf)])
        for c in cands:
            if c in self.fa_dict:
                return self.fa_dict[c]
        return None

    def expand(self, query):
        q = self.fa_norm(query.strip().lower())
        concepts = []
        for fa, en in self.syn_fa:
            if " " in fa and fa in q:
                concepts.append(en)
                q = q.replace(fa, " ")
        rest = []
        for tok in q.split():
            if re.search(r"[؀-ۿ]", tok):
                en = self.fa_lookup(tok)
                if en:
                    concepts.append(en)
            else:
                rest.append(tok)
        q = " ".join(rest)
        base = words(q) + [w for c in concepts for w in words(c)]
        groups = []  # one group per query word: [(weight, [stem-sets of a phrase])]
        for w in dict.fromkeys(base):
            alts = [(1.0, [stems(w)], w)]
            for key in {w} | stems(w):
                for extra in self.syn_en.get(key, []):
                    alts.append((0.45, [stems(ew) for ew in words(extra)], extra))
            groups.append(alts)
        phrase = "-".join(base)
        return groups, phrase, base

    def _term(self, f, forms):
        best = 0.0
        for t in forms:
            idf = self.idf.get(t, 0)
            if t in f["name"]:
                best = max(best, idf * 3)
            elif t in f["tags"]:
                best = max(best, idf * 2)
            elif t in f["cat"]:
                best = max(best, idf * 0.7)
        return best

    def search(self, query, libs=None, n=10):
        groups, phrase, base = self.expand(query)
        if not groups:
            return []
        scored = []
        for i, ic in enumerate(self.icons):
            if libs and ic["lib"] not in libs:
                continue
            f = self.fields[i]
            s = 0.0
            compact = ic["name"].replace("-", "")
            for alts in groups:
                best = 0.0
                for w, phrase_forms, raw in alts:
                    v = w * sum(self._term(f, forms) for forms in phrase_forms) / len(phrase_forms)
                    if raw == ic["name"] or raw.replace("-", "") == compact:
                        v += 10 if w == 1.0 else 6
                    best = max(best, v)
                s += best
            if s <= 0:
                continue
            asked = set().union(*(fs for alts in groups for _, pf, _ in alts for fs in pf))
            s -= sum(0.6 * max(self.idf.get(x, 0) for x in stems(nw)) for nw in words(ic["name"])
                     if not (stems(nw) & asked) and not nw.isdigit())
            if ic["name"] == phrase:
                s += 8
            if " ".join(base) in f["tagphrases"]:
                s += 3
            s -= 0.3 * sum(1 for nw in words(ic["name"]) if nw.isdigit())
            scored.append((s, i))
        scored.sort(key=lambda x: -x[0])
        return [(round(s, 2), self.icons[i]) for s, i in scored[:n]]


def resolve_libs(arg):
    if not arg or arg == "all":
        return None
    libs = []
    for part in arg.split(","):
        part = part.strip().lower()
        if part not in LIB_ALIASES:
            sys.exit(f"unknown --lib {part}; use lucide, tabler, phosphor, heroicons, heroicons-outline, heroicons-solid or all")
        libs += LIB_ALIASES[part]
    return set(libs)


def import_line(idx, ic):
    return idx.libs[ic["lib"]]["import"].format(export=ic["export"])


def fmt_hit(idx, score, ic):
    tags = ", ".join(ic["tags"][:6])
    return f'{ic["lib"]}:{ic["name"]}  ->  {ic["export"]}   ({import_line(idx, ic)})   score {score}' + (f"\n    tags: {tags}" if tags else "")


def svg_with(ic, size=None, color=None):
    svg = ic["svg"]
    if size:
        svg = re.sub(r'\s(width|height)="[^"]*"', "", svg, count=0)
        svg = svg.replace("<svg ", f'<svg width="{int(size)}" height="{int(size)}" ', 1)
    if color:
        svg = svg.replace("currentColor", escape(color, quote=True))
    return svg


def cmd_search(idx, a):
    hits = idx.search(a.query, resolve_libs(a.lib), a.n)
    if a.json:
        out(json.dumps([{"id": f'{h["lib"]}:{h["name"]}', "export": h["export"], "import": import_line(idx, h),
                         "tags": h["tags"], "score": s} for s, h in hits], ensure_ascii=False, indent=1))
        return
    if not hits:
        out(f'No icon found for "{a.query}". Try an English synonym or a broader word; do not invent a name.')
        return
    for s, h in hits:
        out(fmt_hit(idx, s, h))


def cmd_recommend(idx, a):
    libs = resolve_libs(a.lib or "lucide")
    slots = [s.strip() for s in re.split(r"[,|\n،]", a.slots) if s.strip()]
    used, rows = set(), []
    for slot in slots:
        hits = [h for _, h in idx.search(slot, libs, 25)]
        pick = next((h for h in hits if (h["lib"], h["name"]) not in used), None)
        alts = [h for h in hits if h is not pick][:2]
        if pick:
            used.add((pick["lib"], pick["name"]))
        rows.append((slot, pick, alts))
    if a.json:
        out(json.dumps([{"slot": s, "pick": p and {"id": f'{p["lib"]}:{p["name"]}', "export": p["export"], "import": import_line(idx, p)},
                         "alternatives": [f'{x["lib"]}:{x["name"]}' for x in al]} for s, p, al in rows], ensure_ascii=False, indent=1))
        return
    for slot, pick, alts in rows:
        if not pick:
            out(f"{slot}: (no match - rephrase this slot)")
            continue
        alt = ", ".join(x["name"] for x in alts)
        out(f'{slot}: {pick["lib"]}:{pick["name"]} -> {pick["export"]}' + (f"   (alt: {alt})" if alt else ""))
    picked = [p for _, p, _ in rows if p]
    if picked:
        lib = picked[0]["lib"]
        exports = sorted({p["export"] for p in picked})
        source = re.search(r"from '([^']+)'", idx.libs[lib]["import"]).group(1)
        out("\nimport { " + ", ".join(exports) + " } from '" + source + "'")


def find_icon(idx, ident):
    if ":" not in ident:
        sys.exit("use lib:name, e.g. lucide:house")
    lib, name = ident.split(":", 1)
    libs = LIB_ALIASES.get(lib.lower(), [lib.lower()])
    for l in libs:
        i = idx.by_id.get(f"{l}:{name}")
        if i is not None:
            return idx.icons[i]
    return None


def cmd_get(idx, a):
    ic = find_icon(idx, a.id)
    if not ic:
        sys.exit(f"{a.id} does not exist in the index (do not invent icon names; run search)")
    svg = svg_with(ic, a.size, a.color)
    if a.json:
        out(json.dumps({"id": f'{ic["lib"]}:{ic["name"]}', "export": ic["export"], "import": import_line(idx, ic),
                        "license": idx.libs[ic["lib"]]["license"], "svg": svg}, ensure_ascii=False, indent=1))
        return
    out(f'{ic["lib"]}:{ic["name"]}  export {ic["export"]}  license {idx.libs[ic["lib"]]["license"]}\n{import_line(idx, ic)}\n\n{svg}')


def cmd_preview(idx, a):
    items = []
    if all(":" in x for x in a.items):
        for x in a.items:
            ic = find_icon(idx, x)
            if ic:
                items.append(ic)
        title = " ".join(a.items)
    else:
        q = " ".join(a.items)
        libs = resolve_libs(a.lib)
        if libs is None:
            for lib in ["lucide", "tabler", "phosphor", "heroicons-outline"]:
                items += [h for _, h in idx.search(q, {lib}, a.n)]
        else:
            items = [h for _, h in idx.search(q, libs, a.n * 2)]
        title = q
    if not items:
        sys.exit("nothing to preview")
    cells = "\n".join(
        f'<figure><div class="ico">{svg_with(ic, 40)}</div><figcaption><b>{escape(ic["name"])}</b><br>{escape(ic["lib"])}<br><code>{escape(ic["export"])}</code></figcaption></figure>'
        for ic in items)
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Icon preview</title><style>
:root{{--bg:#fafaf9;--fg:#1c1917;--muted:#78716c;--card:#fff;--line:#e7e5e4}}
@media (prefers-color-scheme:dark){{:root{{--bg:#1c1917;--fg:#f5f5f4;--muted:#a8a29e;--card:#292524;--line:#44403c}}}}
body{{margin:0;padding:24px 16px;background:var(--bg);color:var(--fg);font:14px/1.4 system-ui,sans-serif}}
h1{{font-size:18px;margin:0 0 16px}} .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}}
figure{{margin:0;padding:16px 8px;background:var(--card);border:1px solid var(--line);border-radius:10px;text-align:center}}
.ico{{height:48px;display:flex;align-items:center;justify-content:center;color:var(--fg)}} .ico svg{{width:40px;height:40px}}
figcaption{{margin-top:8px;color:var(--muted);font-size:12px;overflow-wrap:anywhere}} figcaption b{{color:var(--fg)}}
</style></head><body><h1>Icon preview: {escape(title)}</h1><div class="grid">
{cells}
</div></body></html>"""
    path = pathlib.Path(a.out).resolve()
    path.write_text(html, "utf-8")
    out(f"wrote {path} ({len(items)} icons)")


PKG_DIR = {"lucide": "lucide-react", "tabler": "@tabler/icons-react", "phosphor": "@phosphor-icons/react",
           "heroicons-outline": "@heroicons/react", "heroicons-solid": "@heroicons/react"}


def cmd_verify(idx, a):
    libs = resolve_libs(a.lib)
    if not libs or len({PKG_DIR[l] for l in libs}) != 1:
        sys.exit("--lib must name one library")
    lib = sorted(libs)[0]
    pkg = None
    for base in [pathlib.Path(a.project).resolve(), *pathlib.Path(a.project).resolve().parents]:
        cand = base / "node_modules" / PKG_DIR[lib]
        if cand.exists():
            pkg = cand
            break
    if not pkg:
        sys.exit(f"{PKG_DIR[lib]} is not installed in {a.project} (or its parents)")
    version = json.loads((pkg / "package.json").read_text("utf-8")).get("version", "?")
    dts = ""
    for f in pkg.rglob("*.d.ts"):
        if f.stat().st_size < 30_000_000:
            dts += f.read_text("utf-8", errors="ignore")
    out(f"{PKG_DIR[lib]} {version} at {pkg}")
    for name in a.names:
        ic = find_icon(idx, f"{lib}:{name}") if ":" not in name else find_icon(idx, name)
        export = ic["export"] if ic else name
        ok = re.search(rf"\b{re.escape(export)}\b", dts) is not None
        out(f"  {'OK     ' if ok else 'MISSING'} {export}" + ("" if ic or ok else "   (not in index either - likely invented)"))


def cmd_libs(idx, a):
    counts = Counter(ic["lib"] for ic in idx.icons)
    for lib, meta in idx.libs.items():
        out(f'{lib:18} {counts[lib]:5} icons  v{meta["version"]:12} {meta["license"]:4}  {meta["package"]:22}  {meta["style"]}')


def main():
    p = argparse.ArgumentParser(description="Offline semantic icon search (Lucide, Tabler, Phosphor, Heroicons)")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--lib"); s.add_argument("-n", type=int, default=10); s.add_argument("--json", action="store_true")
    r = sub.add_parser("recommend"); r.add_argument("slots"); r.add_argument("--lib"); r.add_argument("--json", action="store_true")
    g = sub.add_parser("get"); g.add_argument("id"); g.add_argument("--size", type=int); g.add_argument("--color"); g.add_argument("--json", action="store_true")
    v = sub.add_parser("preview"); v.add_argument("items", nargs="+"); v.add_argument("--lib"); v.add_argument("-n", type=int, default=8); v.add_argument("--out", required=True)
    c = sub.add_parser("verify"); c.add_argument("names", nargs="+"); c.add_argument("--lib", required=True); c.add_argument("--project", required=True)
    sub.add_parser("libs")
    a = p.parse_args()
    data, syn = load()
    idx = Index(data, syn)
    {"search": cmd_search, "recommend": cmd_recommend, "get": cmd_get, "preview": cmd_preview,
     "verify": cmd_verify, "libs": cmd_libs}[a.cmd](idx, a)


if __name__ == "__main__":
    main()
