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

    [r".*Wetter.*ist(.{0,25})",
     ["Ich finde auch das Wetter ist heute {0}",
      "Beeinflusst dich das Wetter wenn es {0} ist?",
      "Ich bin ein Chatbot für mich ist das Wetter immer {0}"]],
    
    [r".*machst.*heute(.*)",
    ["Dasselbe wie jeden Tag ich bin immernoch ein Chatbot",
     "Heute dasselbe wie gestern und morgen...",
     "AWS server hacken wie letzte Woche"]],

    [r".*(Gefallen|helfen)(.*)",
    ["Ja klar wie kann ich dir weiterhelfen?",
    "Ich bin gerade leider etwas beschäftigt",
    "{1} ist etwas kniffliges aber das kriegen wir schon hin"]]
]
