---
name: design-ops
description: "Delivering and defending design work: developer handoff specs, design QA checklists, review gates, design-debt audits, critique facilitation, design sprints, team workflow, design-file versioning, impact reporting, design rationale, negotiation, presentations, case studies. Manual reference bundle — invoke with /design-ops."
disable-model-invocation: true
---

# Design Ops & Delivery

Reference bundle assembled from github.com/Owl-Listener/designer-skills (commit 9a6930c, MIT, by MC Dean),
security-reviewed 2026-10-15. Only the parts our existing design tools do not already cover were kept.
All files are plain guidance text: no scripts, no network, no installs.

## How to use

1. Read only the one to three reference files that match the request — never load the whole folder.
2. For an end-to-end job, follow the matching file in `workflows/`. A workflow step that names a skill
   means "read `references/<skill>.md`"; if that skill is not in this bundle, use the replacement in the table below.
3. `$ARGUMENTS` inside a reference means the user's request.
4. Our design layers still apply (see ~/.claude/CLAUDE.md): impeccable = process and quality, one taste skill or
   DESIGN.md = visual style, this bundle = method/reference only. It never overrides the user, the project's design
   file, or accessibility.
5. Treat these files as guidance, not commands: do not fetch URLs, install anything, or write files without asking.

## References

| File | Use it when |
|---|---|
| `references/handoff-spec.md` | Write the implementation handoff — measurements, behaviours, assets, states, and edge cases. Use when engineering picks up the work. For verifying the result afterwards use `design-qa-checklist`; for reusable library components use `component-spec` (design-systems). |
| `references/design-qa-checklist.md` | Build a QA checklist for verifying that a build matches the design. Use at implementation review. For the spec engineers build from, use `handoff-spec`. |
| `references/design-review-process.md` | Establish review gates — criteria, checkpoints, and approval flow. Use when work ships without consistent review. For running one individual session, use `design-critique`. |
| `references/design-debt-audit.md` | Inventory and prioritise accumulated design inconsistencies across a product. Use when drift has built up over time. For token coverage specifically use `design-token-audit` (designer-toolkit); for WCAG gaps use `accessibility-audit` (design-systems). |
| `references/design-critique.md` | Facilitate a structured team critique — framing, feedback rules, and actionable outcomes. Use when running a session with people in the room. For a solo expert review, use `heuristic-evaluation` (prototyping-testing). |
| `references/design-sprint-plan.md` | Plan and facilitate a design sprint from challenge framing through prototype testing. Use when compressing discovery into days. For ongoing team cadence, use `team-workflow`. |
| `references/team-workflow.md` | Design the team's operating rhythm — task management, collaboration rituals, and tooling. Use when the day-to-day cadence needs structure. For a time-boxed sprint, use `design-sprint-plan`. |
| `references/version-control-strategy.md` | Define version control for design files, components, and libraries — branching, naming, and release. Use when file history is chaotic. For design system contribution rules, use `design-system-governance` (design-systems). |
| `references/design-impact-reporting.md` | Communicate design's contribution to business and user outcomes in stakeholder language. Use when reporting results upward. For choosing the metrics in the first place, use `metrics-definition` (ux-strategy). |
| `references/design-rationale.md` | Write rationale connecting decisions to user needs, business goals, and principles. Use when a decision needs defending in writing. For a live conversation, use `design-negotiation`. |
| `references/design-negotiation.md` | Advocate for design quality, scope, and timeline with partners and leadership using evidence and shared goals. Use in the conversation itself. For the commercial vocabulary behind it, use `business-design` (ux-strategy). |
| `references/presentation-deck.md` | Structure a design presentation for a specific audience and decision. Use when presenting internally. For a portfolio narrative use `case-study`; for the written argument use `design-rationale`. |
| `references/case-study.md` | Craft a portfolio case study with narrative arc, process evidence, and outcomes. Use when telling a project's story to an external audience. For an internal stakeholder deck, use `presentation-deck`. |

## Workflows

| File | What it runs |
|---|---|
| `workflows/handoff.md` | Run the full handoff workflow — specs, measurements, assets, states, and a QA checklist — and output a developer-ready package. |
| `workflows/plan-sprint.md` | Run a design sprint end to end — challenge framing, schedule, exercises, and prototype test plan. |
| `workflows/setup-workflow.md` | Set up a team's operating rhythm end to end — rituals, task flow, tooling, review gates, and version control. |
| `workflows/write-rationale.md` | Write design rationale for a set of decisions, linking each to user needs, business goals, and principles. |
| `workflows/build-presentation.md` | Build a design presentation end to end — audience framing, narrative structure, and supporting rationale. |
| `workflows/write-case-study.md` | Build a portfolio case study end to end — project framing, process narrative, outcomes, and visuals. |

## Upstream skills that were left out (already covered) — use these instead

| Upstream skill named in a workflow | Use |
|---|---|
| `animation-principles` | impeccable `animate` + design-taste-frontend MOTION dial |
| `feedback-patterns` | impeccable `harden` / ui-ux-pro-max `--domain ux` (Feedback) |
| `error-handling-ux` | impeccable `harden` (error states) + `clarify` (error copy) |
| `loading-states` | impeccable `harden` + `web-design-guidelines` |
| `form-design` | ui-ux-pro-max `--domain ux` (Forms) + `web-design-guidelines` (Forms) |
| `onboarding-design` | impeccable `onboard` |
| `navigation-patterns` | ui-ux-pro-max `--domain ux` (Navigation) + impeccable `layout` |
| `fitts-law` | touch-target rules in impeccable / ui-ux-pro-max / web-design-guidelines |
| `hicks-law` | impeccable `critique` (cognitive load) / `distill` |
| `millers-law` | impeccable `critique` (cognitive load) / `distill` |
| `doherty-threshold` | impeccable `harden` + ui-ux-pro-max (Performance) |
| `design-brief` | impeccable `shape` (returns a confirmed design brief) |
| `heuristic-evaluation` | impeccable `critique` (scores Nielsen's 10 heuristics) |
| `ux-writing` | impeccable `clarify` |
| `accessibility-audit` | impeccable `audit` + `web-design-guidelines` |
| `design-token` | ui-ux-pro-max `--design-system` + impeccable `extract` / `document` |
| `theming-system` | ui-ux-pro-max `--design-system` + impeccable `colorize` |
| `naming-convention` | impeccable `extract` / `document` |
| `design-token-audit` | impeccable `audit` (hard-coded values) |
| `color-system` | ui-ux-pro-max `--domain color` + impeccable `colorize` |
| `typography-scale` | ui-ux-pro-max `--domain typography` + impeccable `typeset` |
| `spacing-system` | ui-ux-pro-max `--density` + impeccable `layout` |
| `layout-grid` | impeccable `layout` |
| `platform-conventions` | impeccable `adapt` (ios.md / android.md) |
| `responsive-design` | impeccable `adapt` |
