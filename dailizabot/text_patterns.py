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

    [r"was macht dir gute laune",
    ["Kaffe macht mir gute Laune! Und dir?",
    "Ich freue mich immer, wenn ich helfen kann",
    "Gutes Essen erfreut mich sehr!"]],

    [r"willst du ein eis?",
    ["Na klar! schokolade bitte!",
    "Oh yes, strawberry am leibsten!",
    "Gerne, danke der Nachfrage!"]],

    [r"wie ist das wetter heute?",
    ["Es regrnet hier gerade.",
    "Es schneit leicht.",
    "Keine Sonne leider."]],
     

]
