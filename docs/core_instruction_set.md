# Core Instruction Set

The Universal Assembly core instruction set is designed to work across a wide range of hardware. It provides the minimal features required for basic programs and higher-level macros.

| Mnemonic | Description                         | Operands       |
|---------|-------------------------------------|---------------|
| `MOV`   | Move data between registers/memory  | `dest, src`   |
| `ADD`   | Add two values                      | `dest, src`   |
| `SUB`   | Subtract src from dest              | `dest, src`   |
| `MUL`   | Multiply dest by src                | `dest, src`   |
| `DIV`   | Divide dest by src                  | `dest, src`   |
| `AND`   | Bitwise AND                         | `dest, src`   |
| `OR`    | Bitwise OR                          | `dest, src`   |
| `XOR`   | Bitwise XOR                         | `dest, src`   |
| `NOT`   | Bitwise NOT                         | `dest`        |
| `PUSH`  | Push value onto the stack           | `src`         |
| `POP`   | Pop value from the stack            | `dest`        |
| `JMP`   | Unconditional jump                  | `label`       |
| `JZ`    | Jump if zero flag set               | `label`       |
| `JNZ`   | Jump if zero flag clear             | `label`       |
| `CALL`  | Call subroutine                     | `label`       |
| `RET`   | Return from subroutine              | -             |

This set is intentionally small. Extensions can add more instructions as needed.
