from pathlib import Path

BASE_DIR = Path(".").resolve()
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)