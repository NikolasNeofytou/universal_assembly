#!/usr/bin/env python3
"""Prototype assembler that accepts a Python-like syntax."""

import ast
import sys
import os
from typing import List, Tuple

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import building_blocks as bb

Token = Tuple[str, str]

MACROS = {name: getattr(bb, name) for name in dir(bb) if not name.startswith("_") and callable(getattr(bb, name))}


def assemble_pyasm(path: str) -> List[Token]:
    with open(path) as f:
        tree = ast.parse(f.read(), filename=path)
    tokens: List[Token] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            func_name = node.func.id
            macro = MACROS.get(func_name)
            if not macro:
                raise ValueError(f"Unknown instruction or macro '{func_name}'")
            args = []
            for arg in node.args:
                if isinstance(arg, ast.Constant):
                    args.append(arg.value)
                else:
                    args.append(ast.unparse(arg))
            tokens.extend(macro(*args))
    return tokens


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pyasm.py <source.pyasm>")
        sys.exit(1)

    for instr, ops in assemble_pyasm(sys.argv[1]):
        print(f"{instr} {ops}".strip())
