# -*- coding: utf-8 -*-
import re

filepath = r'c:\Users\vaibh\.gemini\antigravity-ide\brain\485ac52c-f610-4a0c-861b-11a1c1471871\task.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('- [ ] Implement segment-business-content Other', '- [x] Implement segment-business-content Other')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
