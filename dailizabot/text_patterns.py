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
    "Hast du dich immer so gefühlt?",
    "Was denkst du, warum du dich {0} fühlst?"]],

    [r"Ich bin (.*)",
    ["Seit wann bist du {0}?",
    "Findest du, dass es gut ist, {0} zu sein?",
    "Wie ist das Gefühl, dass du {0} bist?"]],

    [r"Bist du (.*)\?",
     ["Warum fragst du, ob ich {0} bin?",
      "Ja! Ich bin natürlich {0}.",
      "Auf keinen Fall bin ich {0}."]]

]
