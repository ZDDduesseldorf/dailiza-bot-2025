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

    [r"Wie ist das Wetter", 
     ["Es ist sonnig!",
     "Es ist regnerisch!",
     "Es ist windig!"]],

    [r"Kannst du ([^?.!]+)", 
     ["Nein, {0} kann ich leider nicht.",
     "Hmm... Ich denke ich kann {0} nicht.",
     "{0} kann ich nicht"]],

    [r"bist du ([^?.!]+)",
    ["ICH BIN KEIN {0}!",
    "Was ist {0}?",
    "Ich denke, dass ich kein {0} bin."]]

]