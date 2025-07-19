"""Basic building block macros for Universal Assembly."""

from typing import List, Tuple

Token = Tuple[str, str]


def push(value) -> List[Token]:
    return [("PUSH", str(value))]


def pop(dest) -> List[Token]:
    return [("POP", dest)]


def add() -> List[Token]:
    return [("ADD", "")]


def mov(dest, src) -> List[Token]:
    return [("MOV", f"{dest}, {src}")]


def add_two_constants(a, b) -> List[Token]:
    tokens = [("PUSH", str(a)), ("PUSH", str(b)), ("ADD", "")]
    return tokens
