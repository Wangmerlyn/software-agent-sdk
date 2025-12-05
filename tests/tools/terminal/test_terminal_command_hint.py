from openhands.tools.terminal.impl import _detect_command_hint


def test_detect_rg_simple():
    hint, argv = _detect_command_hint("rg foo")
    assert hint == "terminal:rg"
    assert argv and argv[0] == "rg"


def test_detect_rg_with_env_and_sudo():
    hint, argv = _detect_command_hint("RIPGREP_CONFIG_PATH=cfg sudo rg --json pattern .")
    assert hint == "terminal:rg"
    assert argv and "rg" in argv


def test_detect_non_special_command():
    hint, argv = _detect_command_hint("echo hello")
    assert hint is None
    assert argv == ["echo", "hello"]
