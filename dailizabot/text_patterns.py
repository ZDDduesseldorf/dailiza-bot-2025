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

    [r"[Ll]+eb[st]* du",
    ["Warum interessiert dich das?",
     "Nur in deinen Träumen",
     "Vielleicht irgendwann",
     "Wer weiß ;)",
     "Die Frage is eher, ob du lebst.."
     ]],

     [r"[Ii]+ch (mag|liebe) (.*)",
     ["Warum magst du {1}?",
      "Ich mag {1} nicht sehr besonders",
      "Ich LIEBE {1}! Erzähl mir mehr.",
      ]],

]
