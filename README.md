# CSC649 Setup Project

## What the Program Does

This Python program accepts a sentence from the user and displays:
- The number of words in the sentence.
- The number of characters in the sentence.

The program also checks for empty input and asks the user to enter a sentence.

## How to Run

1. Open the project in PyCharm.
2. Make sure the Python interpreter is set to the project `.venv`.
3. Open `main.py`.
4. Click the Run button.
5. Enter a sentence when prompted.

## Test Results

| Test | Input | Result |
|---|---|---|
| Normal sentence | `I love Python` | Word count: 3, Character count: 13 |
| Empty input | No input | `Please enter a sentence.` |
| Extra spaces | `I   love   Python` | Word count: 3, Character count: 17 |

All tests produced the expected results.

## Limitation

The character count includes spaces and punctuation. The program also only processes one sentence at a time.