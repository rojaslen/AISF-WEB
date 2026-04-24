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


def snapshot(data_file, csv_file, item_key, fieldnames):
    """Append a full dated snapshot (paths/referrers: 14-day rolling aggregate)."""
    with open(data_file) as f:
        data = json.load(f)

    today = __import__('datetime').date.today().isoformat()
    rows = [
        dict(zip(['date'] + fieldnames[1:], [today] + [item[k] for k in fieldnames[1:]]))
        for item in data
    ]

    if rows:
        Path(csv_file).parent.mkdir(parents=True, exist_ok=True)
        file_exists = Path(csv_file).exists()
        with open(csv_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(rows)
        print(f'{csv_file}: added {len(rows)} row(s)')
    else:
        print(f'{csv_file}: no data')


process('/tmp/views.json',     'traffic/views.csv',     'views',  ['date', 'views',   'uniques'])
process('/tmp/clones.json',    'traffic/clones.csv',    'clones', ['date', 'clones',  'uniques'])
snapshot('/tmp/paths.json',    'traffic/paths.csv',     'paths',      ['date', 'path', 'title', 'count', 'uniques'])
snapshot('/tmp/referrers.json','traffic/referrers.csv', 'referrers',  ['date', 'referrer', 'count', 'uniques'])
