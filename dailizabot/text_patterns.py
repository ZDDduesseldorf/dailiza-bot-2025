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

    [r"(tschüss|auf wiedersehen|bis bald)",
    ["Tschüss!",
    "Auf Wiedersehen!",
    "Bis bald!"]], 

    [r"Ich will (.*)",
    ["Was würde es dir bringen, {0} zu haben?",
    "Warum willst du {0}?"]],

    [r"Ich heiße (.*)",
    ["Schön, dich kennenzulernen, {0}. Wie kann ich dir helfen?",
    "Freut mich, {0}. Was möchtest du besprechen?"]]

]