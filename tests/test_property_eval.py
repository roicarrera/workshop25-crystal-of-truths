"""
Exercise: Property-Based Testing with Hypothesis

You are given a function `eval_expr(expr: str)` in `PBT.evaluator`, which evaluates arithmetic expressions made up of digits (0–9) and operators `+` and `*`, with no spaces or parentheses.

Examples:
    - "1+2" -> 3
    - "2*3+1" -> 7
    - "9+9+9" -> 27

Your task is to design a **property-based test** for this evaluator using the Hypothesis library.

To do so:
1. Write a **Hypothesis strategy** that generates valid input expressions: strings of digits and operators as described above.
2. Identify **a property** that the results of `eval_expr()` should fulfill.
3. Implement a test using `@given(...)` that verifies the chosen property.
4. Use shrinking and/or examples to find edge cases where the property could break.

Hints:
- Think about what makes the expressions valid.
- The function should mimic typical operator precedence.
- The property might relate to known Python behavior or math laws.
- Avoid hardcoding specific inputs — use strategies.

Use this scaffold as your starting point:
"""

from hypothesis import given, strategies as st
from PBT.evaluator import eval_expr

# TODO: Implement your custom strategy to generate valid expressions
@st.composite
def gen_expr(draw):
    # Replace this stub with your own logic
    return draw(st.just("1+1"))

# TODO: Define and justify your own property here
@given(gen_expr())
def test_eval_expr_property(expr):
    result = eval_expr(expr)

    # Replace the line below with a meaningful assertion
    assert isinstance(result, int)  # Placeholder to get started