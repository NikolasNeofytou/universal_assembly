#!/usr/bin/env python3
"""Simple assembler prototype for Universal Assembly."""

import sys
import re

import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from architectures import get_arch


INSTRUCTIONS = {
    "MOV", "ADD", "SUB", "MUL", "DIV",
    "AND", "OR", "XOR", "NOT",
    "PUSH", "POP",
    "JMP", "JZ", "JNZ",
    "CALL", "RET",
}



def assemble(path, arch=None):
    tokens = []
    arch_features = get_arch(arch) if arch else None
    if arch_features:
        print(f"Assembling for {arch} with registers: {arch_features['registers']}")


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

    if not (2 <= len(sys.argv) <= 3):
        print("Usage: assembler.py <source.uas> [arch]")
        sys.exit(1)

    source = sys.argv[1]
    arch = sys.argv[2] if len(sys.argv) == 3 else None
    for instr, ops in assemble(source, arch=arch):

        print(f"{instr} {ops}".strip())
