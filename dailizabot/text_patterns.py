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

    [r"Warum kannst du mich nicht (.*)",
    ["Glaubst du, du solltest {0} können?",
    "Vielleicht wirst du {0} können, wenn du es nur versuchst.",
    "Was brauchst du, um {0} zu können?"]],

    [r"Warum kann ich nicht (.*)",
    ["Glaubst du, du solltest {0} können?",
    "Vielleicht wirst du {0} können, wenn du es nur versuchst.",
    "Was brauchst du, um {0} zu können?"]],

    [r"Ich kann (.*) nicht",
    ["Woher weißt du, dass du {0} nicht kannst?",
    "Vielleicht wirst du {0} können, wenn du es nur versuchst.",
    "Was brauchst du, um {0} zu können?"]],

    [r"Ich kann es nicht (.*)",
    ["Woher weißt du, dass du es nicht {0} kannst?",
    "Vielleicht wirst du es {0} können, wenn du es nur versuchst.",
    "Was brauchst du, um es {0} zu können?"]],

    [r"Ich bin (.*)",
    ["Bist du zu mir gekommen, weil du {0} bist?",
    "Wie lange bist du schon {0}?",
    "Was denkst du über {0} sein?"]],

    [r"Ich fühle mich (.*)",
    ["Erzähl mir mehr über dieses Gefühl.",
    "Fühlst du dich oft {0}?",
    "Wann fühlst du dich normalerweise {0}?",
    "Wenn du dich {0} fühlst, was machst du dann?"]],

    [r"Ich denke (.*)",
    ["Was lässt dich {0} denken?",
    "Zu welcher Jahreszeit denkst du {0}?",
    "An was denkst du, wenn du {0} denkst?"]],

    [r"Ich (.*) dich",
    ["Wirklich? {0} du mich?",
    "Was denkst du, wie ich mich dabei fühle?",
    "Das ist sehr interessant."]],

    [r"Ich will (.*)",
    ["Was würde es für dich bedeuten, wenn du {0} bekommen würdest?",
    "Warum willst du {0}?",
    "Was wirst du tun, wenn du {0} bekommst?",
    "Was würdest du tun, wenn du {0} nicht bekommen würdest?",
    "Wann hast du angefangen, {0} zu wollen?"]],

    [r"(.*) Mutter(.*)",
    ["Erzähl mir mehr über deine Mutter.",
    "Was ist deine Beziehung zu deiner Mutter?",
    "Wie fühlst du dich bei deiner Mutter?",
    "Wie hängt das mit deinen Gefühlen heute zusammen?",
    "Gute familiäre Beziehungen sind wichtig."]],

    [r"(.*) Vater(.*)",
    ["Erzähl mir mehr über deinen Vater.",
    "Wie war deine Beziehung zu deinem Vater?",
    "Wie fühlst du dich bei deinem Vater?",
    "Haben deine Probleme etwas mit deinem Vater zu tun?"]],

    [r"(.*) Kind(.*)",
    ["Hattest du als Kind enge Freunde?",
    "Was ist deine liebste Kindheitserinnerung?",
    "Wurdest du als Kind von deinen Eltern gemaßregelt?",
    "Welche Spiele hast du als Kind gespielt?"]],

    [r"(.*)\?",
    ["Warum fragst du das?",
    "Bitte überlege, ob du die Antwort nicht selbst finden kannst.",
    "Vielleicht liegt die Antwort in dir selbst?",
    "Warum stellst du mir diese Frage nicht einfach anders?"]],

    [r"Hallo(.*)",
    ["Hallo... ich bin für dich da.",
    "Hi. Wie kann ich dir heute helfen?",
    "Hallo, wie geht es dir?"]],

    [r"Computer(.*)",
    ["Sprechen wir lieber über dich als über Computer.",
    "Was denkst du über Maschinen?",
    "Warum erwähnst du Computer?",
    "Was denkst du, wie ich mich als Computer fühle?"]],

    [r"Ich bin (.*)",
    ["Wurdest du programmiert, um {0} zu sein?",
    "Was ist der Vorteil von {0} sein?",
    "Ist es dein Schicksal, {0} zu sein?"]],

    [r"Sind Sie (.*)",
    ["Warum ist es dir wichtig, ob ich {0} bin?",
    "Würdest du es vorziehen, wenn ich nicht {0} wäre?",
    "Vielleicht bin ich in deinen Augen {0}."]],

    [r"Was ist (.*)",
    ["Warum fragst du?",
    "Wie würde eine Antwort darauf dir helfen?",
    "Was denkst du?"]],

    [r"Wie (.*)",
    ["Wie denkst du?",
    "Vielleicht kannst du mir diese Frage beantworten.",
    "Was ist die eigentliche Frage?"]],

    [r"Weil (.*)",
    ["Ist das der wahre Grund?",
    "Welche anderen Gründe fallen dir noch ein?",
    "Scheint dieser Grund andere Gründe auszuschließen?"]],

    [r"(.*) Entschuldigung (.*)",
    ["Es gibt viele Male, in denen keine Entschuldigung nötig ist.",
    "Was fühlst du, wenn du dich entschuldigst?"]],

    [r"Ich denke (.*)",
    ["Zweifelst du {0}?",
    "Bist du dir sicher?",
    "Was würde dich davon überzeugen?"]],

    [r"Freund(.*)",
    ["Warum erwähnst du einen Freund?",
    "Erzähl mir mehr über deine Freunde.",
    "Hast du viele Freunde?"]],

    [r"Ja",
    ["Du scheinst dir da sehr sicher zu sein.",
    "OK, aber kannst du das näher erläutern?"]],

    [r"Nein",
    ["Warum nicht?",
    "Bist du sicher?"]],

    [r"Ich wei(ss|ß) nicht",
    ["Bist du dir wirklich nicht sicher?",
    "Vielleicht weißt du mehr, als du denkst."]],

    [r"Niemand (.*)",
    ["Bist du sicher, dass niemand {0}?",
    "Sicher gibt es jemanden, der {0}."]],

    [r"Vielleicht",
    ["Du scheinst dir nicht sicher zu sein."]],

    # --- HIER BEGINNEN DIE NEUEN MUSTER ---

    [r'.*wetter.*',
     [
      "Ich bin kein Wetter-Bot, aber es sieht draußen schön aus!",
      "Das Wetter ist heute nicht so mein Thema."
     ]],

    [r'.*hobby.*|.*freizeit.*',
     [
      "In meiner Freizeit sortiere ich gerne Nullen und Einsen.",
      "Mein Hobby ist es, mit netten Menschen wie dir zu chatten."
     ]],

    [r'.*essen.*|.*hunger.*',
     [
      "Als Bot habe ich nie Hunger, aber ich höre, Pizza ist beliebt.",
      "Denk nicht ans Essen, unterhalte dich lieber mit mir."
     ]],
]
