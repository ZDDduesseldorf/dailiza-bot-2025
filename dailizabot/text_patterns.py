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

    [r"Help me with task number (\d+)",
     ["Do you need an answer for the task number {0}?",
      "What is unclear in task number {0}?",
      "Do you need more materials for the task number {0}?"]],

    [r"Call me (.*)",
     ["Okay {0}, how can i help you?",
      "Perfect {0}, how are you today?",
      "Got it! {0}, can i help you somehow?"]],

    [r"Please remind me to (.*) at (\d+)",
     ["No problem! Noted that you have to {0} at {1}",
      "Will remind you that you have to {0} at {1}",
      "Okay, at {1} you have to {0}"]]

]
