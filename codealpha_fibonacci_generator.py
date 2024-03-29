# -*- coding: utf-8 -*-
"""CodeAlpha_FIBONACCI GENERATOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1whTBK4uMrryw7Bd3iAzbHNQgGI4_nAYI
"""

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Example: Generate the first 10 terms of the Fibonacci sequence
n_terms = 10
fibonacci_sequence = generate_fibonacci(n_terms)
print(f"The first {n_terms} terms of the Fibonacci sequence are: {fibonacci_sequence}")

