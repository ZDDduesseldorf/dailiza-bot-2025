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

    [r"Ich glaube an (.*)",
    ["Warum glaubst du an {0}?",
     "Interessant, du glaubst also an {0}.",
     "Seit wann weißt du, dass du {0} glaubst?"]],

    [r"Ich habe Angst vor (.*)",
    ["Warum hast du Angst vor {0}?",
    "Glaubst du, dass {0} gefährlich ist?",
    "Was macht dir an {0} Angst?"]],

]
