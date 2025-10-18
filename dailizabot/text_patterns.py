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

    # Eigene
    [r"Ich habe (.*)" , ["Warum hast du {0}?", "Wie hast du {0}?", "Wofür hast du {0}?"]],

    [r"Ich bin (.*)" , ["Bist du {0}, oder ist {0} du?", "Bist du {0}, oder fühlst du dich {0}?", "Denkst du ich bin auch {0}?"]]

]
#python -m dailizabot.main