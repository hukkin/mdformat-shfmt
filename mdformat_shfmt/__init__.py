__version__ = "0.1.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import subprocess


def format_sh(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode("utf-8")
    subprocess_kwargs = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.DEVNULL,
        "input": unformatted_bytes,
    }
    try:
        try:
            result = subprocess.run(["shfmt"], **subprocess_kwargs)
        except FileNotFoundError:
            # If `shfmt` is not installed, try Docker
            result = subprocess.run(
                ["docker", "run", "-i", "--rm", "mvdan/shfmt:latest", "-"],
                **subprocess_kwargs
            )
    except Exception as e:
        import traceback
        print(traceback.print_exc())
        raise
    if result.returncode:
        print('Exception("Failed to format shell code")')
        raise Exception("Failed to format shell code")
    return result.stdout.decode("utf-8")
