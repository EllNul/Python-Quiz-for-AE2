# results_io.py
import csv
from datetime import datetime
from pathlib import Path

# Default output file (in your project folder). Change if you want a different location.
RESULTS_CSV = Path("quiz_results.csv")

def append_result(name: str, score: int, total: int, csv_path: Path | str = RESULTS_CSV) -> None:
    """
    Append one quiz result to a CSV.
    Columns: name, score, total, percent, timestamp_iso

    - Creates the file with headers if it doesn't exist.
    - Uses local timezone timestamp in ISO-8601 (to seconds).
    """
    csv_path = Path(csv_path)
    file_exists = csv_path.exists()

    # Local time with timezone info
    ts = datetime.now().astimezone().isoformat(timespec="seconds")

    percent = round((score / total) * 100, 2) if total > 0 else 0.0

    # Ensure parent folder exists (in case you pass a path in OneDrive or similar)
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with csv_path.open(mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["name", "score", "total", "percent", "timestamp_iso"])
        writer.writerow([name, score, total, percent, ts])