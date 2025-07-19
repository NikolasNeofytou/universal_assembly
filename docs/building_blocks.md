# Building Blocks

The `lib/building_blocks.py` module defines small helper functions that generate
Universal Assembly instructions. These macros let programmers write programs in a
Python-like style and expand to the core instruction set.

Example:

```python
from lib import building_blocks as bb

bb.push(1)
bb.push(2)
bb.add()
bb.pop("result")
```

These calls expand to the tokens:

```
PUSH 1
PUSH 2
ADD
POP result
```
