#!/usr/bin/env python3

import subprocess

def reload_qtile_config():
    # Run qtile cmd-obj -o cmd -f restart
    subprocess.run(["qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])

if __name__ == "__main__":
    reload_qtile_config()

