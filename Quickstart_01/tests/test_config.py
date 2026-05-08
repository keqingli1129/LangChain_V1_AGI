import os

import pytest

from Quickstart_01.utils.config import DataConfig, Config


def test_dataconfig_creates_log_dir(tmp_path):
    log_dir = tmp_path / "logs"
    log_file = str(log_dir / "app.log")
    cfg = DataConfig(log_file=log_file)
    assert os.path.isdir(str(log_dir))
    assert cfg.log_file == log_file
    assert isinstance(cfg.max_bytes, int)
    assert cfg.backup_count == 3
    assert cfg.llm_type == "openai"


def test_dataconfig_default_uses_cwd(monkeypatch, tmp_path):
    # avoid creating files in the repo by changing cwd to a tempdir
    monkeypatch.chdir(tmp_path)
    cfg = DataConfig()
    assert os.path.isdir(os.path.dirname(cfg.log_file))


def test_config_log_dir_exists():
    log_dir = os.path.dirname(Config.LOG_FILE)
    assert log_dir != ""
    assert os.path.isdir(log_dir)
