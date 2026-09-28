import sys, re
sys.stdout.reconfigure(encoding='utf-8')


def get(f):
    try:
        return open(f, 'r', encoding='utf-16').read()
    except Exception:
        return open(f, 'r', encoding='utf-8', errors='ignore').read()


c = get('experience_solitaire_dashboard_new.html')

print(f"File length: {len(c)}")
print(f"</body> at: {c.find('</body>')}, </html> at: {c.find('</html>')}")

# Extract openSendDeckModal function body
pos = c.find('openSendDeckModal')
while pos != -1:
    context = c[pos:pos+300]
    print(f"\n--- openSendDeckModal at {pos} ---")
    print(context[:200])
    pos = c.find('openSendDeckModal', pos+1)

print("\n\n=== send-deck-modal div ===")
sdm = c.find('id="send-deck-modal"')
if sdm != -1:
    print(c[sdm-10:sdm+200])
else:
    print("NOT FOUND")

print("\n\n=== create-lead-modal div ===")
clm = c.find('id="create-lead-modal"')
if clm != -1:
    print(c[clm-10:clm+200])
else:
    print("NOT FOUND")
