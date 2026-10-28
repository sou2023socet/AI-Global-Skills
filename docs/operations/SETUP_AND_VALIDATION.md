# Setup and validation

The repository uses Python 3.11 or newer and the standard library only.

From the canonical project root:

```powershell
python scripts\validate_registry.py
python scripts\generate_canonical_catalogue.py
python scripts\generate_status_matrix.py
python -m unittest discover -s tests -v
```

The validator checks all canonical IDs and names, required `SKILL.md` sections,
execution ordering, dependency references and cycles, candidate catalogue
alignment, complete source migration dispositions, and all 143 source skill
destinations. Similarity pairs are emitted as review evidence rather than
being treated as automatic proof of duplication. The status matrix and
catalogue are generated from registry metadata rather than edited independently.
These checks do not prove that a skill works on every host or project.

Use the registry as metadata and open the matching `skills\<skill-id>\SKILL.md`
for instructions. Keep project-specific context outside this repository using
the [project template](../../templates/project-workspace/project.yaml).

Do not run builds, tests, package installation, application launches, or
artifact-producing checks without the host's explicit command-scoped approval.
