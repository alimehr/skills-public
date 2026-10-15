---
name: product-ui-craft
description: "Concrete craft rules and a strict review bar for product UI (dashboards, admin panels, SaaS apps, tools, settings): focal point and weight-over-size hierarchy, density in px, subtle surface layering, one depth strategy, native -> headless primitive -> hand-roll ladder, semantic tokens, concentric radius, motion timing, the swap/squint/signature/token tests, an approval bar with presumptive blockers, and a diff-scoped de-slop pass. Manual reference — invoke with /product-ui-craft."
disable-model-invocation: true
---

# Product UI Craft

Reference extracted from github.com/Dammyjay93/interface-design (commit 2f9be32, MIT, by Damola Akinleye),
security-reviewed 2026-10-15. Everything our tools lacked was kept, verbatim. Plain text: no scripts, no network, no installs.

## Files

| File | Use it when |
|---|---|
| `references/craft-rules.md` | Building or polishing product UI: hierarchy and composition, surface layering, "use what exists", design-system essentials, polish and motion numbers, infinite expression, colour from the product's world, the Avoid list, visual-reference modes, and the four pre-delivery tests (swap, squint, signature, token). |
| `references/design-review.md` | A strict craft review of a build: six lenses, severity scoring, a false-positive filter (taste is not a defect), and an approval bar with presumptive blockers. Judges only; fixes only when asked. |
| `references/design-deslop.md` | A fast, diff-scoped pass that removes the tells of generated UI, with an explicit "what is NOT slop" filter. |

## How to use

- Scope: dashboards, admin, SaaS, tools, settings. Not for landing/marketing pages.
- Reference layer only. Our design layers still apply (~/.claude/CLAUDE.md): impeccable = process and quality,
  one taste skill or DESIGN.md = visual style. When the chosen style or the project's DESIGN.md says otherwise
  (depth strategy, sidebar colour, radius, fonts), the style/DESIGN.md wins. Accessibility always holds.
- The review and de-slop files mention `.interface-design/system.md`: read that as the project's DESIGN.md.
  They mention `show_widget`/`visualize`: use whatever preview the session offers, or skip.
- Left out on purpose (already covered or conflicting): the intent / domain-exploration process (impeccable
  `shape` / `new-work`), the mandatory per-component checkpoint (conflicts with "brief only for new pages"),
  and the `.interface-design/system.md` memory file (conflicts with one DESIGN.md per project).
