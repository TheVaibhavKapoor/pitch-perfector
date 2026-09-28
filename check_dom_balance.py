import sys, codecs
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

with open('experience_solitaire_dashboard_new.html', 'r', encoding='utf-8') as f:
    html = f.read()

checker = DOMChecker()
checker.feed(html)

print('Errors count:', len(checker.errors))
for err in checker.errors[:10]:
    print(err)
if checker.stack:
    print('Unclosed tags:', len(checker.stack))
    for tag, pos in checker.stack[-10:]:
        print(f'Unclosed <{tag}> at {pos}')
