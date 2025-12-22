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
        [r".*(hi|hello|hey).*",
     ["Hello! How can I help you today?",
      "Hi there! What can I do for you?",
      "Hey! How are you?"]],

    [r".*(today|date|day).*",
     ["Today is a good day.",
      "I don't know the exact date, but today feels nice.",
      "Time flies, doesn't it?"]],

    [r".*(ich verstehe nicht|was meinst du).*",
     ["Kannst du das bitte anders formulieren?",
      "Das habe ich leider nicht verstanden.",
      "Magst du es noch einmal erklären?"]],


]
