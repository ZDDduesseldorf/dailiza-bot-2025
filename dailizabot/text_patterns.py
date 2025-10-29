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

    [r"ich fühle (.*)",
    ["Oh nein! Das tut mir leid zu hören. Möchtest du mir mehr darüber erzählen?"
     "Das klingt wirklich unangenehm. Wie lange hast du das schon?",
     "Hast du schon versucht, einen Arzt aufzusuchen?", ]],

    [r"Ich verändere (meinen|meine|mein) (.*)",
    ["Wow, du willst deinen {1} verändern?", 
    "Das klingt spannend! Was genau möchtest du ändern?",
    "Hast du schon Pläne, wie du deinen {1} ändern willst?",
    "Ich finde es toll, dass du an dir arbeiten möchtest",]]
]

