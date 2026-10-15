# Claude Code skill library (design)

A curated, conflict-free set of Claude Code skills for UI/UX design work. Each third-party skill was security-reviewed (no network access, no installs, no telemetry), and trimmed to the parts not covered elsewhere. Skills added after review are manual-only (`disable-model-invocation: true`) — call them with `/<skill-name>`; `impeccable` and the five taste-skill folders are unchanged upstream copies and may trigger automatically.

## Install

Copy any folder from `skills/` into `~/.claude/skills/`, and files from `agents/` into `~/.claude/agents/`. Scripts need Python 3 (standard library only).

## Contents

| Skill | What it is | Source · licence |
|---|---|---|
| `impeccable` (+ 4 agents in `agents/`) | Frontend design process + quality checks (craft, critique, audit, polish, animate…) | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) · Apache-2.0 |
| `design-taste-frontend` | Brief → design direction with variance/motion/density dials | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · MIT |
| `high-end-visual-design` | Soft, calm, premium look | taste-skill · MIT |
| `minimalist-ui` | Editorial minimal (Notion/Linear style) | taste-skill · MIT |
| `industrial-brutalist-ui` | Swiss/terminal brutalist, data-heavy | taste-skill · MIT |
| `redesign-existing-projects` | Audit + upgrade an existing UI | taste-skill · MIT |
| `interaction-design` | State machines, micro-interaction specs, gestures, UX laws | [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) · MIT (bundled) |
| `design-system-extras` | Motion tokens, localization/RTL, component specs, governance | designer-skills · MIT (bundled) |
| `ux-research` | Personas, journeys, JTBD, interviews, surveys, analytics | designer-skills · MIT (bundled) |
| `ux-strategy` | IA, content strategy, competitive UX, service blueprint, metrics | designer-skills · MIT (bundled) |
| `ux-testing` | A/B, usability plans, prototypes, wireframes, user flows | designer-skills · MIT (bundled) |
| `design-ops` | Handoff, design QA, review gates, critique, case studies | designer-skills · MIT (bundled) |
| `product-ui-craft` | Craft rules, design review and de-slop for product UI | [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) · MIT (repackaged) |
| `web-design-guidelines` | ~100 code-level UI rules, terse `file:line` review | [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) · MIT (frozen snapshot 434b7f9, no remote fetch) |
| `vercel-react-view-transitions` | React/Next.js View Transition API reference | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) · MIT |
| `ui-ux-pro-max` | Local searchable UI/UX data: styles, palettes, fonts (incl. Persian), a11y rules, charts, GSAP presets, 5 stack guides | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · MIT (trimmed and updated, see its SKILL.md) |
| `icon-finder` | Offline meaning-based icon search (Lucide, Tabler, Phosphor, Heroicons; English + Persian) | original · MIT; icon data ISC/MIT (`data/licenses/`) |

Each folder carries its upstream LICENSE (and NOTICE where required). Local changes (manual-only flag, removed network fetches, trimmed data) are described inside the affected SKILL.md files; `impeccable` and the taste-skill folders are unmodified.
