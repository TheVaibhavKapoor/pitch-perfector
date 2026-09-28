import sys
sys.stdout.reconfigure(encoding='utf-8')


def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()


def save(f, c):
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)


c = get('customer_overview_solitaire.html')
body_end = c.find('</body>')
html_end = c.find('</html>')
orphan_len = len(c) - html_end - 7
print(f"File length: {len(c)}")
print(f"</body>: {body_end}, </html>: {html_end}")
print(f"Orphaned after </html>: {orphan_len} chars")

if orphan_len > 10:
    orphaned = c[html_end + 7:]
    valid_html = c[:body_end]
    new_content = valid_html + '\n' + orphaned.strip() + '\n</body>\n</html>'
    save('customer_overview_solitaire.html', new_content)
    print("Fixed!")
    c2 = get('customer_overview_solitaire.html')
    html2 = c2.find('</html>')
    disp2 = c2.find('openDispositionModal')
    print(f"After fix - </html> at: {html2}, openDispositionModal at: {disp2}, after html: {disp2 > html2}")
else:
    print("No orphaned content - file is OK")
    disp = c.find('openDispositionModal')
    print(f"openDispositionModal at: {disp}, after html: {disp > html_end}")
