import json
import os
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('GDELT_URL', 'https://api.gdeltproject.org/api/v2/doc/doc')
params = {'query': 'robotics OR "3D printing"', 'mode': 'artlist', 'maxrecords': 20, 'format': 'json', 'sort': 'datedesc'}
response = requests.get(url, params=params, timeout=30)
response.raise_for_status()
data = response.json()
items = []
for article in data.get('articles', []):
    items.append({'title': article.get('title'), 'url': article.get('url'), 'source': 'gdelt', 'published_at': article.get('seendate'), 'collected_at': datetime.now(timezone.utc).isoformat()})
Path('data').mkdir(exist_ok=True)
Path('data/gdelt-sample.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'{len(items)} registros salvos em data/gdelt-sample.json')
