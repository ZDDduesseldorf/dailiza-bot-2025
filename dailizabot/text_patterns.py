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
    
    [r"Magst du (.*)\?",
    ["Ja, ich liebe {0}!",
     "Bahhhh ich hasse {0}!",
     "Was ist {0}?"]],
    
    [r"(?i)wird [a-z]* Wetter",
     ["Es wird sonnig.",
      "Es wird wolkig.",
      "Es wird regnerisch.",
      "Es wird stürmisch."]]
    

]