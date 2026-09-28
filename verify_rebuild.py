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
            self.errors.append(f'Mismatched tag </{tag}> at line {self.getpos()}, expected </{last_tag}> from line {pos}')

for fname in ['experience_solitaire_dashboard_new.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    checker = DOMChecker()
    checker.feed(html)

    print(f'{fname}:')
    print(f'  Total size: {len(html)}')
    print(f'  </main> count: {html.count("</main>")}')
    
    # Check all panels present
    for p in ['panel-dc', 'panel-cc', 'panel-assets', 'panel-investments', 'panel-forex', 'panel-other']:
        pos = html.find(f'id="{p}"')
        print(f'  {p}: pos={pos}')
    
    main_pos = html.find('</main>')
    panel_assets_pos = html.find('id="panel-assets"')
    print(f'  panel-assets before </main>: {panel_assets_pos < main_pos}')
    
    print(f'  DOM Errors: {len(checker.errors)}')
    for err in checker.errors[:5]:
        print(f'    {err}')
    print(f'  Unclosed: {len(checker.stack)}')
