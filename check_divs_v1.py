with open('experience_solitaire_dashboard_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()

def count_divs(start_marker, end_marker):
    start = html.find(start_marker)
    end = html.find(end_marker)
    segment = html[start:end]
    opens = segment.count('<div')
    closes = segment.count('</div')
    print(f"v1 {start_marker.split('id=')[-1].strip('\"')} Opens: {opens}")
    print(f"v1 {start_marker.split('id=')[-1].strip('\"')} Closes: {closes}")

count_divs('id="panel-assets"', '<!-- close panel-assets -->')
count_divs('id="panel-investments"', '<!-- close panel-investments -->')
