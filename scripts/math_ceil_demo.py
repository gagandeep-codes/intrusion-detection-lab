"""
math_ceil_demo.py

Demonstrates the use of math.ceil() in Python — rounding numbers
upward to the nearest integer.

Part of: Intrusion Detection Lab — Kali fundamentals
Author: Gagandeep Singh
"""

import math


def demo_ceil():
    """Print examples of math.ceil() behavior on different inputs."""
    test_values = [1.4, 5.3, -5.3, 22.6, 10.0]

    print("math.ceil() — rounds upward to nearest integer\n")
    print(f"{'Input':>10} {'Output':>10}")
    print("-" * 22)

    for value in test_values:
        result = math.ceil(value)
        print(f"{value:>10} {result:>10}")


if __name__ == "__main__":
    demo_ceil()
