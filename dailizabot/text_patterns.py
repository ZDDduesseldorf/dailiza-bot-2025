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

    [r"ich muss (.+) lernen",
     ["Oh oh, {0} das kenn ich. Viel Erfolg",
      "{0} zu lernen ist nie leicht",
      "Ich hoffe, du bestehst {0} mit 1,0"]],

    [r"ich bin süchtig nach tiktok",
     ["Same ich kann mein Tag nicht ohne TikTok verbringen",
     "Es ist eigentlich traurig, wie wir ohne nicht können",
     "Vielleicht sollten wir überlegen die App zu löschen"]],
 
]

