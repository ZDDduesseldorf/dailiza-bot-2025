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

    [r"ich studiere (.*)",
    ["Wie findest du das Studium %1?",
    "Interessant. %1 ist sicher ein anspruchsvolles Fach."]],  

    [r"ich bin (.*) müde",
    ["Warum bist du %1 müde?",
    "Ich hoffe, du kannst dich bald ausruhen."]] 
]