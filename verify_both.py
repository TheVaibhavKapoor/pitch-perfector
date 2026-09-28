import sys, codecs, re
from html.parser import HTMLParser

class DOMChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            return
        if not self.stack:
            self.errors.append(f'Unexpected end tag </{tag}> at line {self.getpos()}')
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag:
            self.errors.append(f'Mismatched tag </{tag}> at {self.getpos()}, expected </{last_tag}> from {pos}')

for fname in ['experience_solitaire_dashboard_new.html', 'experience_solitaire_dashboard.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    checker = DOMChecker()
    checker.feed(html)

    print(f'=== {fname} ===')
    print(f'  File size: {len(html)}')
    print(f'  </main> count: {html.count("</main>")}')
    
    main_pos = html.find('</main>')
    for p in ['panel-dc', 'panel-cc', 'panel-assets', 'panel-investments', 'panel-forex', 'panel-other']:
        pos = html.find(f'id="{p}"')
        inside = 'IN' if pos != -1 and pos < main_pos else 'OUT' if pos != -1 else 'MISSING'
        print(f'  {p}: {inside}')
    
    print(f'  DOM Errors: {len(checker.errors)}')
    for err in checker.errors[:5]:
        print(f'    {err}')
    print(f'  Unclosed tags: {len(checker.stack)}')
    print()
