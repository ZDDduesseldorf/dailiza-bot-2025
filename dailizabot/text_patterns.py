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

    [r"was hältst du von (.*)\??",
    ["Was genau interessiert dich an {0}?",
    "Warum willst du meine Meinung zu {0} wissen?",
    "Findest du {0} denn spannend?"]],

    [r"(immer|nie|ständig) passiert mir (.*)",
    ["Wieso glaubst du, dass dir das {1} {0} passiert?",
    "Gibt es einen Grund, warum das immer wieder vorkommt?",
    "Wie fühlst du dich dabei, dass dir das {0} passiert?"]],

    [r"ich verstehe das nicht(.*)",
    ["Kannst du genauer sagen, was daran unklar ist?",
    "Was genau würdest du gerne verstehen?",
    "Welche Aspekte sind für dich besonders verwirrend?"]],
]
