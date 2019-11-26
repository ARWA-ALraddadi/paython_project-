#--------------------------------------------------------------------#
#
# Example of using assertions to represent a program proof
#
# Function max_three below is adapted from the textbook "Algorithms"
# by R. Johnsonbaugh and M. Schaefer [Algorithm 1.2.1, page 5, 2004].
# In the second version we have attempted to construct a proof of
# its correctness using assertions, with Python's built-in "max"
# function serving as the oracle.  Following this we run a few
# tests to see if any of the assertions are violated.  (Of course,
# trying this handful of tests is no guarantee that our proof is
# correct.)

# Return the maximum of three given values
# Original code
def max_three(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

# Return the maximum of three given values
# Proven correct!
def max_three(a, b, c):
    assert a == a # Our precondition is always true
    result = a
    assert result == a
    if b > result:
        assert result == a and b > result
        assert b == max(a, b) # By implication
        result = b
        assert result == max(a, b)
    assert result == max(a, b)       
    if c > result:
        assert result == max(a, b) and c > result
        assert c == max(a, b, c) # By implication
        result = c
        assert result == max(a, b, c)
    assert result == max(a, b, c) # The postcondition
    return result

# Call the function and see if any of the assertions are violated
# (for these specific tests)
try:
    max_three(1, 2, 3)
    max_three(23, 15, 2)
    max_three(34, 105, 56)
    max_three(23, 23, 23)
    print("No assertion violations detected (yet!)")
except AssertionError:
    print("Your program proof is wrong! Counterexample found!")
