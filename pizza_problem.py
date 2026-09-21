"""A pizzeria offers 8 different toppings (pepperoni, mushrooms, onions, sausage, 
bacon, extra cheese, olives, and peppers). You order a large pizza and get to choose 3 toppings.

Does order matter here? (Is a pepperoni, mushroom, and onion pizza different from an onion, 
mushroom, 
and pepperoni pizza?)

Write a Python snippet that defines a
 combinations(n: int, r: int) -> int function using your factorial 
function.

Calculate and print the total number of unique 3-topping pizzas you can create out of the 8 choices!"""

import itertools


def factorial(n: int) -> int:
    """Calculate the factorial of a number n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combinations(n: int, r: int) -> int:
    """Calculate the number of combinations C(n, r)."""
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


# 1. Define the topping options
toppings = [
    "pepperoni",
    "mushrooms",
    "onions",
    "sausage",
    "bacon",
    "extra cheese",
    "olives",
    "peppers",
]

n_toppings = len(toppings)
r_toppings = 3

# 2. Mathematical verification using your custom functions
total_count = combinations(n_toppings, r_toppings)
print(f"Mathematical total of unique 3-topping pizzas: {total_count}")
print("-" * 50)

# 3. Generate all specific combinations using itertools
all_combos = list(itertools.combinations(toppings, r_toppings))

# 4. Print all 56 combinations neatly numbered
print("All 56 Possible Combinations:")
for index, combo in enumerate(all_combos, start=1):
    formatted_toppings = ", ".join(combo)
    print(f"{index:2d}. {formatted_toppings}")
