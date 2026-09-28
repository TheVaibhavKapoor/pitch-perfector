import os
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py') or file.endswith('.html'):
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    if 'Air India' in f.read():
                        print('Found in', file)
            except Exception:
                pass
