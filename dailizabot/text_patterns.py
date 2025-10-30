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

    [r"Mir geht.{0,5}s.{0,5} (.*)",
    ["Warum geht es dir {0}?",
    "Das klingt {0}. Möchtest du darüber erzählen?",
    "Was hat dich dazu gebracht, dass es dir {0} geht?"]],

    [r"meine Lieblingsfarbe ist (.*)",
    ["{0} ist wirklich eine tolle Farbe!",
    "Ich mag {0} auch sehr gerne",
    "Mir geht es nicht so, ich mag die Farbe {0} nicht so gerne."]],

    [r"Ich habe keine Lust auf (.*)",
    ["Das ist okay, das hat jeder mal",
    "Dann mach mal eine Pause und lass es diesmal sein",
    "Warum hast du keine Lust auf {0}"]] 


]
