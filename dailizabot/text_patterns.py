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

    [r"Ich fühle mich (.*)",
    ["Warum fühlst du dich {0}?",
    "Was denkst du, hat dazu geführt, dass du dich {0} fühlst?",
    "Wie lange fühlst du dich schon {0}?"]],

    [r"(?:Ich denke|Ich glaube) (.*)",
    ["Warum denkst du, dass {0}?",
    "Was hat dich zu dieser Überzeugung gebracht, dass {0}?",
    "Könnte es auch sein, dass ,{0} nicht ganz stimmt?"]],

    [r"Ich habe (.*) gemacht",
    ["Was hat dich dazu gebracht, {0} zu machen?",
    "Und wie fühlst du dich jetzt, nachdem du {0} gemacht hast?",
    "Glaubst du, es war die richtige Entscheidung, {0} zu machen?"]]
]
