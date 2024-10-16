[![Build Status](https://github.com/hukkin/mdformat-shfmt/actions/workflows/tests.yaml/badge.svg?branch=master)](<https://github.com/hukkin/mdformat-shfmt/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![PyPI version](<https://img.shields.io/pypi/v/mdformat-shfmt>)](<https://pypi.org/project/mdformat-shfmt>)

# mdformat-shfmt
> Mdformat plugin to format shell code blocks

## Description
mdformat-shfmt is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format shell code blocks embedded in Markdown with [shfmt](https://github.com/mvdan/sh).
The plugin invokes shfmt in a subprocess so having either shfmt or Docker installed is a requirement.

## Installing
1. Install either [shfmt](https://github.com/mvdan/sh#shfmt) or [Docker](https://docs.docker.com/get-docker/)
1. Install mdformat-shfmt
   ```bash
   pip install mdformat-shfmt
   ```

## Usage
```bash
mdformat YOUR_MARKDOWN_FILE.md
```

## Limitations
The Docker fallback is only tested on Linux.
If you experience issues with it on Windows or macOS, please install shfmt.
