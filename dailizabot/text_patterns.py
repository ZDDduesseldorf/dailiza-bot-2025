"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"ist es wahr (.*)",
    ["Ja {0}. ist wahr",
    "Nein {0}, ist nicht wahr",
    "Bist du sicher, dass du das wissen willst?"]],

    [r"wie\s+(war|ist).*tag",
    ["Danke. Mein Tag war gut",
    "Sehr gut, danke. Und wie war dein Tag bei dir",
    "Ich kann nicht klagen. Es er war gut"]],

    [r"\bnein\b",
    ["ok",
    "Verstehe, kann ich dir anders wie helfen",
    "Gibt es noch etwas das du brauchst?"]],

    [r"\bja\b",
    ["Schön",
    "Das freut mich",
    "Bist du sicher, dass du es wirklich brauchst?"]],
]
