#!/usr/bin/env python3
"""Simple hardware scan script for Universal Assembly."""
import platform
import json

def scan():
    info = {
        "system": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }
    return info

if __name__ == "__main__":
    print(json.dumps(scan(), indent=2))
