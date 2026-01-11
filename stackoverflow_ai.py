#!/usr/bin/env python3
import random
import sys

# StackOverflow Answer Generator 9000™
# Because reading actual answers is for people with time

def generate_answer(question):
    """
    Generates a perfect StackOverflow answer.
    Guaranteed to be 87% correct, 100% confident.
    """
    
    # Classic StackOverflow responses
    templates = [
        "Have you tried turning it off and on again?",
        "This is a duplicate question. Marking as duplicate.",
        "Your code is wrong. Here's how I would do it:",
        "Actually, you should use XYZ instead. It's better.",
        "This question is too broad. Please be more specific.",
        "I had the same problem 5 years ago. Here's my solution:",
        "You're using the wrong framework. Switch to my favorite one.",
        "The real question is: why would you even want to do that?",
        "Just use a library. Don't reinvent the wheel.",
        "Works on my machine. Must be your environment."
    ]
    
    # Random code snippet that may or may not help
    code_snippets = [
        "import this",
        "while True: print('help')",
        "def solution(): return 42",
        "# TODO: Fix this later",
        "print('Hello, World!')",
        "raise NotImplementedError('Figure it out yourself')",
        "# Magic happens here",
        "return None  # The answer to everything"
    ]
    
    # Pick random template and code
    template = random.choice(templates)
    code = random.choice(code_snippets)
    
    # Add random upvotes for authenticity
    upvotes = random.randint(-3, 257)
    
    # 30% chance of being marked as accepted answer
    is_accepted = random.random() < 0.3
    
    # Build the masterpiece
    answer = f"""
{'✓ ACCEPTED ANSWER' if is_accepted else ''}
{template}

```python
{code}
```

Upvotes: {upvotes} | Answered by: Expert_{random.randint(1, 999)}
"""
    
    return answer.strip()


def main():
    """
    Main function. Because every script needs one.
    Even if it's just pretending to be useful.
    """
    print("\n=== StackOverflow Answer Generator ===")
    print("Saving developers from actual research since never\n")
    
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("What's your programming problem? ").strip()
    
    if not question:
        question = "How do I fix my code?"  # Default question for lazy devs
    
    print(f"\nQuestion: {question}\n")
    print("=" * 50)
    print("\nGenerating expert answer...\n")
    
    # The magic happens here (not really)
    answer = generate_answer(question)
    
    print(answer)
    print("\n" + "=" * 50)
    print("\nRemember: This answer is probably wrong. Good luck!\n")


if __name__ == "__main__":
    main()
