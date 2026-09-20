# Contributing

Thank you for contributing to `Awesome Space Systems Simulation`.

## Curation Criteria

Submissions should meet the following criteria:

1. They are directly related to space systems modeling, simulation, testing, or validation.
2. The link is publicly accessible and the project's purpose can be confirmed from its documentation.
3. The entry belongs in the most specific available category and is not a duplicate.
4. The description is factual and avoids unsupported claims about performance or accuracy.

Projects with a license, examples, tests, benchmark results, or public validation material are especially welcome.

## Entry Format

```markdown
### Project Name

- Project Name - One-sentence description. URL: `PROJECT_URL`
- **Type:** library
- **Primary category:** dynamics
- **Simulation scope:** S1
- **Evidence level:** V1
- **Primary domain:** orbit propagation
- **Capability tags:** orbit, propagation
- **Language:** Python
- **License:** MIT
- **Platform:** Linux, macOS, and Windows
- **Time advancement:** variable-step numerical integration
- **SIL/HIL:** not documented
- **Validation status:** repository tests and examples
- **Maintenance status:** active
- **Review status:** reviewed
```

Do not guess missing information. Keep an item in `pending-candidates.md` until its official URL, scope, license or access terms, and primary category can be confirmed.

## Submission Checklist

- [ ] The link works
- [ ] The category is accurate
- [ ] Simulation scope and evidence level are supported by cited evidence
- [ ] A reviewed entry contains no `pending review` fields
- [ ] The description is concise and verifiable
- [ ] The entry is not duplicated
- [ ] No generated files, credentials, or private data are included

## Maintenance

If a project becomes unmaintained, its link breaks, or its license changes, open an issue or pull request with supporting evidence.

## How to verify a project

1. Start from the project's official repository or documentation.
2. Confirm the project identity, scope, language, license, and maintenance status.
3. Record only capabilities stated in official documentation or demonstrated by
   a reproducible example.
4. Separate simulation scope (`S0`-`S4`) from evidence level (`V0`-`V4`).
5. Keep uncertain fields as `pending review` and use the pending-candidates
   page when the official identity or access terms are unclear.

## How to add evidence

Evidence should identify the source and the claim it supports. Useful sources
include official validation reports, repository tests, published reference
comparisons, experimental results, and documented flight or mission heritage.
Do not convert a marketing statement into a validation level without a source.

## How to propose a benchmark

Use the benchmark template in `benchmarks/README.md`. Include the problem
definition, exact inputs, reference equations or data, error metrics,
tolerances, reproduction steps, and the current validation status. A proposed
benchmark is not a validated result until at least one reproducible run is
reviewed.

## Archived and restricted projects

Archived, commercial, or access-restricted projects may remain useful
references. Label their maintenance and access status explicitly, and do not
present them as current open-source recommendations.

## Task guides and unique ownership

Task guides should link to the primary catalog entry instead of copying its
metadata. Each project has one primary category; cross-cutting uses belong in
capability tags, guides, or cross-references.
