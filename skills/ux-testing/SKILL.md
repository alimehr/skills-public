---
name: ux-testing
description: "Validation methods: A/B test design, click/first-click tests, usability task scenarios, accessibility test plans with assistive-tech users, prototype fidelity strategy, wireframe specs, user-flow diagrams, parallel concepts and concept selection with decision records. Manual reference bundle — invoke with /ux-testing."
disable-model-invocation: true
---

# UX Testing & Prototyping

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
| `references/a-b-test-design.md` | Design an A/B experiment — hypothesis, variants, primary metric, and sample size. Use when a change can be measured quantitatively at scale. For observing behaviour qualitatively, use `test-scenario`. |
| `references/click-test-plan.md` | Design first-click and click tests for findability and navigation. Use when testing whether people can locate something. For full task-based observation, use `test-scenario`. |
| `references/test-scenario.md` | Write realistic usability task scenarios with success criteria and facilitation notes. Use when you have a study and need the tasks. For the surrounding study design, use `usability-test-plan` (design-research). |
| `references/accessibility-test-plan.md` | Plan accessibility testing — assistive technologies, participant criteria, WCAG coverage, and session protocol. Use when scheduling testing with real AT users. Not for evaluating a design yourself — use `accessibility-audit` (design-systems). |
| `references/prototype-strategy.md` | Choose prototype fidelity and method to match the design question and the decision at stake. Use before building a prototype. For what to test once it exists, use `test-scenario`. |
| `references/wireframe-spec.md` | Specify wireframe layout — content priority, component placement, and annotation. Use when defining structure before visual design. For grid mechanics, use `layout-grid` (ui-design). |
| `references/user-flow-diagram.md` | Diagram screen-level paths, decision points, and branch logic. Use when specifying how a feature is traversed. For the emotional end-to-end arc, use `journey-map` (design-research). |
| `references/parallel-concepts.md` | Build several genuinely different solutions to the same problem at once, spread across what the user does rather than how it looks. Use when one direction is on the table and the team is about to refine it by default. For choosing between the concepts afterwards, use `concept-selection`. |
| `references/concept-selection.md` | Choose between competing concepts against criteria fixed in advance, and record what each rejected concept was testing. Use when several directions are alive and one has to win. For picking which problem to work on, use `opportunity-framework` (ux-strategy); for deciding by production traffic, use `a-b-test-design`. |

## Workflows

| File | What it runs |
|---|---|
| `workflows/experiment.md` | Design an A/B experiment end to end — hypothesis, variants, primary metric, and sample size. |
| `workflows/explore-options.md` | Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record. |
| `workflows/prototype-plan.md` | Create a prototyping and testing plan for a design initiative. |
| `workflows/test-plan.md` | Choose a testing method and build the plan around it — method selection, task scenarios, click tests, and accessibility coverage. |

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
