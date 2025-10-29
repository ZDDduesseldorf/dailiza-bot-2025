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

    [r"wie (heisst|heißt) du", 
    ["Ich bin Dailiza, ein einfacher Chatbot.",
     "Man nennt mich Dailiza."]]

    [r"ich fühle mich (.*)",
    ["`Warum fühlst du dich {0}?",
    "Wie lange fühlst du dich schon {0}?",
    "Erz`ähl mir mehr darüber, dass du dich {0} fühlst."]]

    [r"(tschüss|auf wiedersehen|bis bald)",
    ["Tschüss!",
    "Bis bald!",
    "Auf Wiedersehen! Gib 'exit' ein, um das Programm zu beenden."]]

]
