__version__ = "0.0.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import subprocess


def format_sh(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode("utf-8")
    result = subprocess.run(
        ["shfmt"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        input=unformatted_bytes,
    )
    if result.returncode:
        raise Exception("Failed to format shell code")
    return result.stdout.decode("utf-8")
