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

    [r"geht.{0,5}s.{0,5} (.*)",
    ["Freut mich zu hören, dass es dir {0} geht!",
    "Schade Mamelade.",
    "Luegner! Dir geht es nicht {0}."]],

    [r"Was gibt es zu (.*)",
    ["Fisch {0}",
    "Portfolio {0}",
    "Nicht zu {0}"]],

    [r"Auf einer Skalar von 1-10, wie sehr (.*) du mich",
    ["Du bist uninteressant",
    "Garnicht",
    "Keine Skalar der Welt kann diesen Wert ermessen oder erfassen"]],

]
