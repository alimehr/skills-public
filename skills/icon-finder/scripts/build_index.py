"""Build the offline icon index for the icon-finder skill from reviewed npm tarballs (data only, nothing executed)."""
import gzip, json, os, pathlib, re, shutil, sys
from html import escape

# Folder holding the extracted npm tarballs (npm pack + tar -xzf), passed as argv[1] or ICON_DATA_SRC.
SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ICON_DATA_SRC", "icon-data"))
OUT = pathlib.Path.home() / ".claude/skills/icon-finder/data"
OUT.mkdir(parents=True, exist_ok=True)


def pascal(name):
    return "".join(p[:1].upper() + p[1:] for p in re.split(r"[-_]", name) if p)


def node_svg(nodes, attrs):
    body = "".join(
        f"<{tag} " + " ".join(f'{k}="{escape(str(v), quote=True)}"' for k, v in a.items() if k != "key") + "/>"
        for tag, a in nodes)
    return f'<svg xmlns="http://www.w3.org/2000/svg" {attrs}>{body}</svg>'


def clean_svg(text):
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r">\s+<", "><", text)


STROKE24 = 'width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
icons = []

# Lucide (ISC) -- names/tags/nodes match lucide-react 1.33.0
L = SRC / "lucide-static-1.33.0/package"
tags = json.loads((L / "tags.json").read_text("utf-8"))
nodes = json.loads((L / "icon-nodes.json").read_text("utf-8"))
for name, nd in nodes.items():
    icons.append({"lib": "lucide", "name": name, "tags": tags.get(name, []), "cat": [],
                  "export": pascal(name), "svg": node_svg(nd, STROKE24)})

# Tabler outline (MIT)
T = SRC / "tabler-icons-3.49.0/package"
meta = json.loads((T / "icons.json").read_text("utf-8"))
tnodes = json.loads((T / "tabler-nodes-outline.json").read_text("utf-8"))
for name, nd in tnodes.items():
    m = meta.get(name, {})
    icons.append({"lib": "tabler", "name": name, "tags": [str(x) for x in m.get("tags", [])],
                  "cat": [m["category"]] if m.get("category") else [],
                  "export": "Icon" + pascal(name), "svg": node_svg(nd, STROKE24)})

# Phosphor regular (MIT) -- metadata parsed from the JS data file with regexes, never executed
P = SRC / "phosphor-icons-core-2.1.1/package"
js = (P / "dist/index.mjs").read_text("utf-8")
enum_src = js[:js.index("const n = [")]
enums = {}
for var, body in re.findall(r"(\w) = /\* @__PURE__ \*/ \(\(i\) => \((.*?)\)\)\(\1 \|\| \{\}\)", enum_src):
    for key, val in re.findall(r'i\.(\w+) = "([^"]+)"', body):
        enums[f"{var}.{key}"] = val
for block in re.split(r"\n  \{\n", js[js.index("const n = ["):])[1:]:
    name = re.search(r'name: "([^"]+)"', block).group(1)
    pas = re.search(r'pascal_name: "([^"]+)"', block).group(1)
    cats = [enums.get(c, c) for c in re.findall(r"\b(e\.\w+)", re.search(r"categories: \[([^\]]*)\]", block).group(1))]
    tg = re.search(r"tags: \[(.*?)\]", block, re.S)
    tlist = [t for t in re.findall(r'"([^"]+)"', tg.group(1)) if t != "*new*"] if tg else []
    svgf = P / "assets/regular" / f"{name}.svg"
    if not svgf.exists():
        continue
    icons.append({"lib": "phosphor", "name": name, "tags": tlist, "cat": cats,
                  "export": pas + "Icon", "svg": clean_svg(svgf.read_text("utf-8"))})

# Heroicons 24 outline + solid (MIT) -- no tags upstream; names only
H = SRC / "heroicons-2.2.0/package/24"
for style in ("outline", "solid"):
    for f in sorted((H / style).glob("*.svg")):
        icons.append({"lib": f"heroicons-{style}", "name": f.stem, "tags": [], "cat": [],
                      "export": pascal(f.stem) + "Icon", "svg": clean_svg(f.read_text("utf-8"))})

LIBS = {
    "lucide": {"version": "1.33.0", "package": "lucide-react", "import": "import {{ {export} }} from 'lucide-react'", "license": "ISC", "style": "outline, 24px grid, stroke 2"},
    "tabler": {"version": "3.49.0", "package": "@tabler/icons-react", "import": "import {{ {export} }} from '@tabler/icons-react'", "license": "MIT", "style": "outline, 24px grid, stroke 2"},
    "phosphor": {"version": "2.1.1 (core)", "package": "@phosphor-icons/react", "import": "import {{ {export} }} from '@phosphor-icons/react'", "license": "MIT", "style": "regular weight shown (also thin/light/bold/fill/duotone via weight prop), 256 grid"},
    "heroicons-outline": {"version": "2.2.0", "package": "@heroicons/react", "import": "import {{ {export} }} from '@heroicons/react/24/outline'", "license": "MIT", "style": "outline, 24px grid, stroke 1.5"},
    "heroicons-solid": {"version": "2.2.0", "package": "@heroicons/react", "import": "import {{ {export} }} from '@heroicons/react/24/solid'", "license": "MIT", "style": "solid, 24px grid"},
}
data = {"libs": LIBS, "icons": icons}
with gzip.open(OUT / "icons.json.gz", "wt", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

lic = OUT / "licenses"
lic.mkdir(exist_ok=True)
for lib, path in [("lucide", L / "LICENSE"), ("tabler", T / "LICENSE"), ("phosphor", P / "LICENSE"), ("heroicons", H.parent / "LICENSE")]:
    shutil.copy(path, lic / f"{lib}-LICENSE.txt")

from collections import Counter
print(Counter(i["lib"] for i in icons), (OUT / "icons.json.gz").stat().st_size, "bytes")
