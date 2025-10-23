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



    [r"(ich vermisse) (.*)",
     ["was vermisst du an {1}?", 
      "es ist wichtig , dass du dich so fühlst wie du dich ",
      "{1} ist dir vielleicht wichtig ,aber was dir wichtig ist , ist nicht immer auch = gut für dich"]],

   [r"Ich verschiebe immer meine Hausaufgaben ,was sind deine Tipps",
    ["Mach deine Aufgaben !!!!",
    "Heul nicht mach jetzt.",
    "... Vaters ganzer stolz..."]],

    [r"warum (.*)",
     ["KEINE AHNUNG MEINE ANTWORTEN SIND BEGRENZT LIES EIN BUCH ODER SO", 
     "千里之行，始于足下。",
     "Vllt weil sie Sahra eine 1 geben sollten  "]],
]
