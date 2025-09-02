
### Truthiness

The discussion so far should be mostly review. It's time to talk about the main topic of this assignment: what is **truthiness**, and how does it impact our code? We'll tackle that next.

After that review of booleans and logical operators, we're finally able to talk about the notion of **truthiness**. Truthiness differs from boolean values in that Python evaluates almost all values as true. There are some exceptions, however:

- `False`
- `None`
- `0`
- `0.0`
- `0j`
- `""` (an empty string)
- `[]` (an empty list)
- `{}` (an empty dictionary)
- `()` (an empty tuple)
- `set()` (an empty set)
- `frozenset()` (an empty frozenset)
- `range(0)` (an empty range)

All of these values evaluate as false. **Memorize** them!

