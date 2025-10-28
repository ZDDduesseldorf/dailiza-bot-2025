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

    [r"(?i)\bdu\s+bist\s+(doof|idiot|langsam|dumm|bescheuert|Opfer)\b",
     ["Aua, das tut mir Leid. Kannst du mir das genauer erklären?",
      "Ich gebe mein Bestes :(",
      "Oh, das ist aber gemein! Vielleicht hab ich's falsch verstanden."   ]],

    [r"(?i)\bdu\s+bist\s+(schön|wundervoll|schlau|hübsch|lieb|nett|intelligent)\b",
     ["Danke! Du bist auch {0}!",
      "Das ist lieb und das kann ich nur zurück geben.",
      "Du schmeichelst mir...",
      ]],  
]
