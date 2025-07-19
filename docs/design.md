# Design Overview

This document outlines the initial design goals for the Universal Assembly project.

1. **Hardware Detection**
   - Provide scripts to detect CPU features, memory configuration, and available peripherals.
2. **Core Instruction Set**
   - Define a minimal cross-platform set of instructions. See
     [core_instruction_set.md](core_instruction_set.md) for the initial list.
3. **Macro Library**
   - Offer building blocks and safety checks for assembly programmers.
4. **Tooling**
   - Develop an assembler that adapts to hardware scan results and warns about unsupported instructions.


5. **Architecture Modules**
   - Architecture descriptions live in the `architectures` package. Each provides
     register lists and other metadata.

6. **Python-Like Building Blocks**
   - The `lib.building_blocks` module offers helper functions that expand to core
     instructions. Programmers can write programs using these functions and
     assemble them with `tools/pyasm.py`.

