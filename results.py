import csv # Import csv module so it can push the results to a csv
from datetime import datetime # For the date/ time
from pathlib import Path # Where the results will be posted

RESULTS_CSV = Path("quiz_results.csv")

def append_result(name: str, score: int, total: int, csv_path: Path | str = RESULTS_CSV) -> None:

    csv_path = Path(csv_path)
    file_exists = csv_path.exists()

    # Local time with timezone info
    ts = datetime.now().astimezone().isoformat(timespec="seconds")

    percent = round((score / total) * 100, 2) if total > 0 else 0.0

    # Ensure parent folder exists
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with csv_path.open(mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["name", "score", "total", "percent", "timestamp_iso"])
        writer.writerow([name, score, total, percent, ts])