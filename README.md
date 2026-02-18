# ☕ Merge Queue Café

A demo repository for showcasing **GitHub Pull Request Merge Queues**.

## What is this?

A tiny Flask-based café menu app used to demonstrate how merge queues handle
many concurrent pull requests that modify shared files.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## Tests

```bash
pytest tests/ -v
```

## The Demo

This repo has ~18 PRs that each make small, valid changes — adding menu items,
tweaking styles, adding features. Each PR passes CI on its own, but many touch
the same files (`menu.py`, `styles.css`, `templates/index.html`).

Without a merge queue, merging one PR can cause the next to fail. With merge
queues enabled, GitHub automatically batches compatible changes and serializes
conflicting ones, ensuring `main` always stays green.
