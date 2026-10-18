from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'templates/bokprojekt/publishing/pdf-template.tex'
s = p.read_text()
assert 'paperwidth=$bookpaperwidth$' in s
assert 'paperheight=$bookpaperheight$' in s
print('PASS: PDF dimensions')
