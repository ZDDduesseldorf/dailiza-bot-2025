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

    [r"^(hallo|hey|hi|servus|moin|guten (?:morgen|tag|abend))\b",
     ["Hallo! Wie kann ich dir helfen?",
      "Hey! Was gibt’s?",
      "Hi! Womit kann ich dich unterstützen?"]],

    [r"\bich (?:bin|fühle mich) (.*)",
     ["Warum fühlst du dich {0}?",
      "Seit wann bist du {0}?",
      "Was glaubst du, macht dich {0}?"]],

]
