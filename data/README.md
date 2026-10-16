# BluEmpress public data

These JSON files are the **public, community-improvable data** for BluEmpress. Suggest changes with an issue or a pull request that touches **only this folder**.

| File | What it is |
|---|---|
| [`features-roadmap.json`](features-roadmap.json) | Feature list and idea status (`live`, `testing`, `idea`) |
| [`moods.json`](moods.json) | The nine moods and portrait labels, plus the five chat modes |
| [`bluroom-check.json`](bluroom-check.json) | The lines BluEmpress says during a BluRoom Check |
| [`faq.json`](faq.json) | Frequently asked questions |
| [`tester-guide.json`](tester-guide.json) | Closed test steps and the feedback we want |
| [`schema/`](schema) | JSON Schemas that describe each file |

## License

The files above and the schemas are **CC BY-NC-SA 4.0**: share and adapt with credit, non-commercial only, and share alike. Full text: [`LICENSE-CC-BY-NC-SA-4.0.txt`](LICENSE-CC-BY-NC-SA-4.0.txt). This does not license the app, names, character, or images. See the [main LICENSE](../LICENSE).

## How to suggest an improvement

1. Edit the JSON in a fork (keep two-space indentation and double quotes).
2. Check it locally if you like:
   ```bash
   pip install -r scripts/requirements.txt
   python scripts/validate_data.py
   ```
3. Open a pull request. A read-only check validates every file against its schema.
4. For new BluRoom Check lines, use `"status": "suggested"` and the next free `bc-###` id.

## Rules for data

- No secrets, emails, phone numbers, or real private people.
- Keep it classy: no slurs or cursing.
- Keep persona facts general. Do not add personal details about the creators.
- Only describe features that really exist, or mark them `"status": "idea"`.
