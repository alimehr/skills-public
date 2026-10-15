---
name: ux-research
description: "User research methods: personas, empathy maps, journey maps, JTBD, interview scripts and summaries, affinity diagrams, card sorts, diary studies, surveys, usability test plans, behavioural analytics, qual-quant triangulation, research repositories. Manual reference bundle — invoke with /ux-research."
disable-model-invocation: true
---

# UX Research

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
| `references/user-persona.md` | Build research-grounded personas with goals, frustrations, and behavioural patterns. Use when decisions need a consistent user reference. For one session's emotional snapshot use `empathy-map`; for motivation framing use `jobs-to-be-done`. |
| `references/empathy-map.md` | Build a Says, Thinks, Does, Feels map for one user or segment. Use when sharing user understanding quickly. For a composite archetype with goals and behaviours use `user-persona`; for cross-session themes use `affinity-diagram`. |
| `references/journey-map.md` | Map one persona's end-to-end experience with stages, touchpoints, emotions, and pain points. Use when improving an existing experience. For the multi-channel ecosystem use `experience-map` (ux-strategy); for screen-level paths use `user-flow-diagram` (prototyping-testing). |
| `references/jobs-to-be-done.md` | Map functional, emotional, and social jobs with outcome expectations. Use when reframing decisions around motivation rather than features. For who the user is, use `user-persona`. |
| `references/interview-script.md` | Write a structured interview guide — warm-up, core exploration, and wrap-up. Use before running interviews. For analysing what comes back, use `summarize-interview`. |
| `references/summarize-interview.md` | Turn one interview transcript into themes, supporting quotes, and action items. Use immediately after a session. For synthesising many sessions at once, use `affinity-diagram`. |
| `references/affinity-diagram.md` | Cluster many qualitative data points into themes and insight statements. Use when synthesising across multiple sessions or sources. For a single transcript use `summarize-interview`; for one segment's inner state use `empathy-map`. |
| `references/card-sort-analysis.md` | Analyse open or closed card sort results into a proposed grouping and label set. Use after running a sort study. For turning that evidence into a full structure, use `information-architecture` (ux-strategy). |
| `references/diary-study-plan.md` | Design a diary study — prompts, cadence, duration, participant criteria, and analysis frame. Use when behaviour unfolds over days or weeks. For a single-session study, use `usability-test-plan`. |
| `references/survey-design.md` | Design unbiased survey instruments — question wording, scales, and sampling — to measure attitudes at scale. Use when you need quantitative breadth. For behavioural experiments, use `a-b-test-design` (prototyping-testing). |
| `references/usability-test-plan.md` | Design a usability study — research questions, methodology, participant criteria, metrics, and facilitation guide. Use when planning the study as a whole. For writing the task scenarios inside it, use `test-scenario` (prototyping-testing). |
| `references/behavioural-analytics.md` | Read funnels, retention curves, and event data as a designer — separating a design problem from a tracking artefact. Use when handed product data you did not design and asked why people drop off. For choosing what to measure, use `metrics-definition` (ux-strategy); for running a controlled test, use `a-b-test-design` (prototyping-testing). |
| `references/qual-quant-triangulation.md` | Reconcile what the numbers say with what users say, and design the study that settles it rather than restates it. Use when behavioural data and research findings point different ways. For reading the data on its own, use `behavioural-analytics`; for synthesising interviews on their own, use `affinity-diagram`. |
| `references/research-repository.md` | Build a repository that makes findings findable, reusable, and cumulative across teams. Use when the same research keeps getting redone. For synthesising one study, use `affinity-diagram`. |

## Workflows

| File | What it runs |
|---|---|
| `workflows/discover.md` | Run a full user research cycle — persona creation, empathy mapping, and journey mapping for a product or feature. |
| `workflows/interview.md` | Prepare an interview script or summarize an interview transcript into structured insights. |
| `workflows/synthesize.md` | Synthesize research data into affinity diagrams, themes, and actionable insights. |
| `workflows/test-plan.md` | Run the full usability study workflow — research questions, participant criteria, tasks, metrics, and facilitation guide. |

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
