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
    # Neues Muster 1
    [r"(.*)wetter(.*)",
     ["Ich habe kein Fenster, aber ich hoffe, es ist schön draußen!",
      "Das Wetter beeinflusst wirklich unsere Stimmung, oder?",
      "Wie ist es bei dir – Sonne oder Regen?"]],

]
