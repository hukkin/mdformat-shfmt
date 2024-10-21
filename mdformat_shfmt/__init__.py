__version__ = "0.1.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import subprocess


def format_sh(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode()
    subprocess_kwargs = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.DEVNULL,
        "input": unformatted_bytes,
    }

    for cmd in (
        ["shfmt"],
        ["docker", "run", "-i", "--rm", "mvdan/shfmt:latest", "-"],
        ["podman", "run", "-i", "--rm", "docker.io/mvdan/shfmt:latest", "-"],
    ):
        try:
            result = subprocess.run(cmd, **subprocess_kwargs)
            break
        except FileNotFoundError:
            pass
    else:
        raise Exception("No shfmt executable found")

    if result.returncode:
        raise Exception("Failed to format shell code")
    return result.stdout.decode()
