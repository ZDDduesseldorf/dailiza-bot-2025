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
     "Chatgbt kann dir im Notfall auch bei {0} helfen !"]],

    [r"Wo finde ich eine Anleitung zum Thema (.*)",
    ["Zu dem Thema {0} gibt es bestimmt ein passendes YouTube Video !",
     "Bei dem Thema {0} kann Chatgbt dir auch gut weiterhelfen !",
     "Vielleicht können Freunde, Familie oder auch deine professoren dir bei dem Thema {0} Helfen"]]

]
