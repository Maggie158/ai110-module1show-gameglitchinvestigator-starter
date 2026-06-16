# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Purpose:** A Streamlit number-guessing game where the player guesses a secret number within a difficulty-based range, guided by Higher/Lower hints.
- **Bugs found:** (1) New Game didn't work; (2) range/secret ignored difficulty (showed 1–100, secret out of bounds); (3) submit took two clicks; (4) hints were backwards; (5) switching difficulty didn't reset the game.
- **Fixes applied:** Reset state on New Game and on difficulty change; re-roll the secret to the active range and show real `low/high`; correct the high/low hints; remove the int-vs-str secret hack; refactor logic into `logic_utils.py`.

## 📸 Demo Walkthrough

A full sample game on **Easy** (secret = **12** for this trace).

1. **Launch & settings.** Run `python -m streamlit run app.py`. In the sidebar, select **Difficulty: Easy**. The sidebar updates to **Range: 1 to 20** and **Attempts allowed: 6**, and a fresh game starts automatically (attempts, history, and score reset to 0).
2. **Starting state.** The main panel shows *"Guess a number between 1 and 20. Attempts left: 6"*. Expanding **Developer Debug Info** shows `Secret: 12`, `Attempts: 0`, `Score: 0`, `History: []` — confirming the secret is inside the 1–20 range.
3. **Guess 1 → too low.** Type `5`, click **Submit Guess 🚀** once. Hint: **📈 Go HIGHER!** (outcome "Too Low"). Score: `0 → -5`. Attempts left: 5. History: `[5]`.
4. **Guess 2 → too high.** Type `18`, Submit. Hint: **📉 Go LOWER!** (outcome "Too High"). Score: `-5 → 0` (the +5 even-attempt bonus). Attempts left: 4. History: `[5, 18]`.
5. **Guess 3 → win.** Type `12`, Submit. Hint: **🎉 Correct!**, balloons animate. Final message: *"You won! The secret was 12. Final score: 60"* (win bonus `100 - 10*(3+1) = 60`). Game status becomes "won".
6. **New Game.** Click **New Game 🔁**: status, attempts, history, and secret all reset, and the game is playable again immediately (no double-click, no frozen "already won" screen).
7. **Switch difficulty mid-game.** Change **Difficulty** to **Normal**: the range updates to 1–100, a new in-range secret is rolled, and attempts/history/score all clear automatically — past attempts do not carry over.

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.14.6, pytest-9.1.0, pluggy-1.6.0
collected 4 items

tests/test_game_logic.py ....                                            [100%]

============================== 4 passed in 0.00s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
