"""
Here we collect the chatbot text patterns.
"""

import random


psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"Was kannst du (.*)",
    ["Ich kann mit dir über verschiedene Themen sprechen und dir zuhören.",
     "Ich kann mit dir über vieles sprechen.",
     "Da ich ein Chatbot bin, kann ich nur mit dir sprechen.",
     "Ich kann fast alles - was willst du eigentlich??"]],

    [r"(random|zufällige)\s*zahl",
    [f"Hier ist deine Randomzahl: {random.randint(1,100)}"]]

]
