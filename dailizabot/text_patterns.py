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

    [r".*hilfe.*",
    ["Klar, wie kann ich dir helfen?",
    "Ich bin hier, um zu helfen. Was ist dein Anliegen?",
    "Beschreibe dein Problem genauer."]],

    [r".*wer bist du.*",
    ["Ich bin Dailiza, dein einfacher Chatbot.",
    "Mein Name ist Dailiza. Wie kann ich dir helfen?",
    "Ich bin Dailiza, immer für einen Chat bereit."]],

]
