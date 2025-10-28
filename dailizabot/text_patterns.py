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
    
    [r"hallo|hey|hi",
    ["Hallo! Wie kann ich dir helfen?",
     "Guten Tag! Was führt dich zu mir?"]]

    [r"ich bin (müde|traurig|froh|glücklich)",
    ["Warum bist du {0}?",
     "Was macht dich {0}?",
     "Kannst du mehr darüber erzählen, warum du {0} bist?"]]

    [r"wer bist du|was bist du",
    ["Ich bin Dailiza, ein einfacher Chatbot.",
     "Man nennt mich Dailiza."]]
]

