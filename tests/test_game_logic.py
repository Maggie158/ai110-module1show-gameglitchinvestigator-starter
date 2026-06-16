from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_direction_not_backwards():
    # Targets the fixed bug: the hint message used to be backwards.
    # A guess ABOVE the secret should tell the player to go LOWER.
    _, too_high_message = check_guess(60, 50)
    assert "LOWER" in too_high_message

    # A guess BELOW the secret should tell the player to go HIGHER.
    _, too_low_message = check_guess(40, 50)
    assert "HIGHER" in too_low_message
