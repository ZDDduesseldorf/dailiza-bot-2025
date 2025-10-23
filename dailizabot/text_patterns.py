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

    [r"Wie heißt du?",
     ["Nenn mich Daliza.",
      "Ich habe keinen Namen",
      "Nenn mich, wie du magst."]],

    [r"(Tschüss|Auf Wiedersehen|Tschau)",
     ["Tschüss!",
      "Auf Wiedersehen! Bis zum nächsten Mal.",
      "Tschau, War schön, mit dir zu sprechen."]]

    [r"Danke",
     ["Gern geschehen!",
      "Kein Problem!",
      "Sehr gern!"]],
]
