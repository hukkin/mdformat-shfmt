from pathlib import Path
import subprocess
from unittest.mock import patch

from markdown_it.utils import read_fixture_file
import mdformat
import pytest

TEST_CASES = read_fixture_file(Path(__file__).parent / "data" / "fixtures.md")


@pytest.mark.parametrize(
    "line,title,text,expected", TEST_CASES, ids=[f[1] for f in TEST_CASES]
)
def test_fixtures(line, title, text, expected):
    """Test fixtures in tests/data/fixtures.md."""
    md_new = mdformat.text(text, codeformatters={"sh"})
    if md_new != expected:
        print("Formatted (unexpected) Markdown below:")
        print(md_new)
    assert md_new == expected


def test_shfmt_error(capfd):
    """Test that any prints by shfmt go to devnull."""
    unformatted_md = """~~~bash
$[
~~~
"""
    formatted_md = """```bash
$[
```
"""
    result = mdformat.text(unformatted_md, codeformatters={"bash"})
    captured = capfd.readouterr()
    assert not captured.err
    assert not captured.out
    assert result == formatted_md


def test_docker():
    """Test Docker fallback if shfmt not installed."""
    input_ = """\
~~~sh
function func1()
{
echo "test"
  }
~~~
"""
    expected_output = """\
```sh
function func1() {
\techo "test"
}
```
"""

    unmocked_run = subprocess.run

    def no_shfmt_run(*args, **kwargs):
        """Make subprocess.run think that `shfmt` is not installed."""
        if args[0][0] == "shfmt":
            raise FileNotFoundError
        return unmocked_run(*args, **kwargs)

    with patch("mdformat_shfmt.subprocess.run", new=no_shfmt_run):
        output = mdformat.text(input_, codeformatters={"sh"})
    assert output == expected_output
