# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Click the "New Game" tab/button | A new game starts with a fresh secret number | Nothing happens; the New Game tab doesn't work | None |
| Set Difficulty to Easy (Range: 1 to 20) | Game interface should use range 1 to 20 and secret within bounds | Game still shows "Guess a number between 1 and 100" and the secret is 91, which is out of the 1–20 bounds | None |
| Submit a new guess | Guess is submitted on the first click | Must click twice to submit a new guess | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code (the VS Code AI coding assistant) in agent mode, giving it `app.py` and `logic_utils.py` as context.

**Correct suggestion:** The AI explained that the "hints are backwards" glitch lived in `check_guess`, where a guess above the secret returned the "Go HIGHER!" message instead of "Go LOWER!". It suggested swapping the two hint messages. I verified this by reading the corrected logic and by running pytest — the guess of 60 against a secret of 50 now returns a message containing "LOWER", and the test passes.

**Incorrect/misleading suggestion:** When refactoring `check_guess` into `logic_utils.py`, the AI's first framing was to "just move the function," which on its own would have crashed the game: `app.py` was still converting the secret to a string on even-numbered attempts (`attempts % 2`), so an int-vs-str comparison would raise a TypeError once the messy fallback was dropped. I caught this by reading through the submit handler in `app.py`, and the fix also required removing that string-conversion hack so `check_guess` always receives an int.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed by combining two checks: reading the corrected logic line by line to confirm it matched the expected behavior, and re-running the game and the test suite to confirm the symptom was gone. For the high/low bug I ran `pytest` and added a new test, `test_hint_direction_not_backwards`, that asserts a too-high guess returns a message containing "LOWER" and a too-low guess returns "HIGHER". It passed alongside the three starter tests (4 passed total), which showed the hint direction was now correct — this test would have failed against the original buggy code. I also fixed the starter tests, which compared `check_guess(...)` to a bare string even though it returns an `(outcome, message)` tuple. The AI helped by generating the targeted test case and explaining that asserting on the message string (not just the outcome label) was what actually pinned down the bug I fixed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I'd say Streamlit re-runs your whole script from top to bottom every time you interact with the page — every click, typed value, or dropdown change replays the entire file like it's loading fresh. That means any normal variable resets each time, so you can't just store the secret number in a regular variable or it gets re-randomized on every click. `st.session_state` is the fix: it's a dictionary that *survives* those reruns, so values like the secret, attempts, and history stick around between interactions. The bugs in this project came from misusing that — the secret never being re-rolled when it should be, and game state (status/history) not being cleared when starting a new game or switching difficulty, because the code forgot to reset those persistent values.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
