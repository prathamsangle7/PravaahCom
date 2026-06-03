import os

apps = [
    'accounts','students','trainers','programs','courses',
    'batches','sessions','attendance','assessments','certificates',
    'hostels','rooms','allocations','finance','notifications',
    'documents','audit','reports','dashboard','api'
]

for app in apps:
    path = os.path.join('apps', app, 'apps.py')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        fixed = content.replace(
            f"name = '{app}'",
            f"name = 'apps.{app}'"
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f"Fixed: apps/{app}/apps.py")
    else:
        print(f"NOT FOUND: {path}")

print("Done!")
