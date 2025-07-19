#!/usr/bin/env python3
"""Simple assembler prototype for Universal Assembly."""

import sys
import re

INSTRUCTIONS = {
    "MOV", "ADD", "SUB", "MUL", "DIV",
    "AND", "OR", "XOR", "NOT",
    "PUSH", "POP",
    "JMP", "JZ", "JNZ",
    "CALL", "RET",
}


def assemble(path):
    tokens = []
    with open(path) as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith(';'):
                continue
            parts = re.split(r"\s+", line, maxsplit=1)
            instr = parts[0].upper()
            operands = parts[1] if len(parts) > 1 else ""
            if instr not in INSTRUCTIONS:
                raise ValueError(f"Unknown instruction '{instr}' at line {lineno}")
            tokens.append((instr, operands))
    return tokens


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: assembler.py <source.uas>")
        sys.exit(1)

    for instr, ops in assemble(sys.argv[1]):
        print(f"{instr} {ops}".strip())
