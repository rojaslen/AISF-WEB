import json
import csv
from pathlib import Path


def load_existing_dates(filepath):
    p = Path(filepath)
    if not p.exists():
        return set()
    with open(p, 'r', newline='') as f:
        return {row['date'] for row in csv.DictReader(f)}


def append_rows(filepath, fieldnames, new_rows):
    p = Path(filepath)
    p.parent.mkdir(parents=True, exist_ok=True)
    file_exists = p.exists()
    with open(p, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for row in sorted(new_rows, key=lambda r: r['date']):
            writer.writerow(row)


def process(data_file, csv_file, item_key, fieldnames):
    with open(data_file) as f:
        data = json.load(f)

    existing = load_existing_dates(csv_file)
    new_rows = [
        {'date': item['timestamp'][:10], fieldnames[1]: item['count'], fieldnames[2]: item['uniques']}
        for item in data.get(item_key, [])
        if item['timestamp'][:10] not in existing
    ]

    if new_rows:
        append_rows(csv_file, fieldnames, new_rows)
        print(f'{csv_file}: added {len(new_rows)} row(s)')
    else:
        print(f'{csv_file}: no new data')


process('/tmp/views.json', 'traffic/views.csv',  'views',  ['date', 'views',  'uniques'])
process('/tmp/clones.json', 'traffic/clones.csv', 'clones', ['date', 'clones', 'uniques'])
