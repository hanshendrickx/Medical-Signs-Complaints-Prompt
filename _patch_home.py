from pathlib import Path

p = Path(r"templates/accounts/home.html")
t = p.read_text(encoding="utf-8")
t = t.replace(
    ".button.primary {\n            background: var(--accent);\n            border-color: var(--accent);\n            color: white;\n        }",
    ".button.primary {\n            background: var(--accent);\n            border-color: var(--accent);\n            color: white;\n        }\n\n        .button.danger {\n            background: #b91c1c;\n            border-color: #b91c1c;\n            color: white;\n        }\n\n        .button.success {\n            background: #166534;\n            border-color: #166534;\n            color: white;\n        }",
)
p.write_text(t, encoding="utf-8")
print("patched")
