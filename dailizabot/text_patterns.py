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

    [r"(Servus|Grüß dich|Guten Morgen|Guten Tag|Hi|Hallo|Gutan Abend)",
     ["Hallo, wie kann ich dir helfen?", "Servus, brauchst du meine Hilfe?",
      "Ich hoffe, es geht dir gut. Bin bereit dir zu helfen..."]],

    [r"Ich würde gerne (.*) in Zukunft werden",
     ["Warum möchtest du {0} werden?", 
      "Weißt du, was du studieren musst, um {0} zu werden?",
      "{0} zu sein ist bestimmt sehr toll!"]], 

    [r"Mein (.*) ist (.*).",
     ["Wieso ist dein {0} {1}?",
      "Warum ist dein {0} {1} geworden?",
      "Echt? Ist dein {0} wirklich {1}?"]]

]
