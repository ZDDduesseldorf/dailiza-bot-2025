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

    [r"kannst du mir bei (.*) helfen",
    ["Sehr gerne helfe ich dir bei {0} !",
     "Wo genau benötigst du bei {0} hilfe ?",
     "Chatgbt kann dir im Notfall auch bei {0} helfen !"]]

]
