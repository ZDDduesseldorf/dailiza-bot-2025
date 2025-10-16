"""
Here we collect the chatbot text patterns.
"""

psychobabble = [

    [r"hallo|hi|hey|guten tag|servus|moin",
     ["Hallo! Schön, dass du da bist.",
      "Hey! Wie geht’s dir heute?",
      "Hi! Worüber möchtest du sprechen?"]],

    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"wie ist das wetter",
     ["Ich weiß es nicht genau, aber ich hoffe, es ist schön bei dir!",
      "Wetter ist immer ein interessantes Thema. Magst du Sonnenschein lieber oder Regen?"]]

]
