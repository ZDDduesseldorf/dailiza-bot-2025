"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"wie geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],
    
    [r"(?i)\b(lästern|gelästert|beef|geredet)\b",
     ["Oh hört sich echt interessant! Erzähl mir mehr.",
      "Was ist passiert?",
      "Spill the tea!"]],
    
    [r"Ich fühle mich(.*)",
     ["Was beschäftigt dich?",
      "Willst du darüber reden, was stresst dich gerade?",
      "Warum fühlst du dich {0}?"]],

    [r"(?i)\b(langweile|faul|chillen|kein bock)\b",
     ["Soll ich dir ein Witz erzählen?",
      "Geh mal putzen lieber, du faule Kartoffel.",
      "Mach dir einen guten und chill weiter."]]

]

