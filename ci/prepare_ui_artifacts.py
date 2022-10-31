import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
# Needed for setup purposes, filling the FILE_HASHES dict
from tests.ui_tests import read_fixtures  # isort:skip

read_fixtures()
from tests.ui_tests import _hash_files, FILE_HASHES, SCREENS_DIR  # isort:skip

# As in CI we are running tests for more models separately,
# there will always be the other models missing.
# Therefore, choosing just the cases for our model.
if len(sys.argv) > 1:
    model = sys.argv[1].upper()
else:
    model = "TT"
model_file_hashes = {k: v for k, v in FILE_HASHES.items() if k.startswith(f"{model}_")}

for test_case, expected_hash in model_file_hashes.items():
    recorded_dir = SCREENS_DIR / test_case / "recorded"
    actual_hash = _hash_files(recorded_dir)
    assert expected_hash == actual_hash
    shutil.make_archive(
        str(ROOT / "ci/ui_test_records" / actual_hash), "zip", recorded_dir
    )
