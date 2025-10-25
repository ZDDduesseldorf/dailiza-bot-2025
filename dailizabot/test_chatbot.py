import pytest
from dailizabot.main import dailiza_answer


def test_dailiza_answer():
    user_input = "Wie geht es dir denn so?"
    expected_responses = [
        "Danke. Mir geht es gut und dir?",
        "Sehr gut, danke. Und wie läuft's bei dir?",
        "Ich kann nicht klagen. Was ist mit dir?"
    ]

    response = dailiza_answer(user_input)
    assert response in expected_responses, f"Unexpected response: {response}"

def test_was_macht_dir_gute_Laune():
    user_input = "Was macht dir gute Laune?"
    expected_responses = [
        "Kaffe macht mir gute Laune! Und dir?",
        "Ich freue mich immer, wenn ich helfen kann",
        "Gutes Essen erfreut mich sehr!",
    ]

    response = dailiza_answer(user_input)
    assert response in expected_responses, f"Unexpected response: {response}"

def test_willst_du_ein_eis():
    user_input = "Willst du ein Eis?"
    expected_responses =[
        "Na klar! schokolade bitte!",
        "Oh yes, strawberry am liebsten!",
        "Gerne, danke der Nachfrage!"
    ]

    response = dailiza_answer(user_input)
    assert response in expected_responses, f"Unexpected response: {response}"

def test_wie_ist_das_wetter():
    user_input = "Wie ist das Wetter heute?"
    expected_reposnses =[
        "Es regnet hier gerade.",
        "Es schneit leicht.",
        "Keine Sonne leider."
    ]
    
    response = dailiza_answer(user_input)
    assert response in expected_reposnses, f"Unexpected response: {response}" 