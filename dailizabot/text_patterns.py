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
    
    [r"(?:wie.{0,8}(?:ist|wird).{0,8}das.{0,3}wetter(?:.{0,12}(?:heute|morgen|übermorgen))?)",
    ["Ich denke, das Wetter wird ganz okay.",
    "Scheint wechselhaft zu werden.",
    "Sieht gut aus – zumindest im Moment."]],
    
    [r"(?:wie\s+spät\s*(?:ist\s*es)?|uhrzeit|welche\s+zeit\s*(?:ist\s*es)?)",
    ["Ich habe leider keine Uhr, aber gefühlt ist es immer Zeit für einen Kaffee.",
    "Die genaue Uhrzeit weiß ich nicht, aber es ist bestimmt später, als du denkst.",
    "Zeit ist relativ und eine Frage der Einstellung."]],
    


]
