"""Generate the English page from the Chinese game source."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = (root / "index.html").read_text(encoding="utf-8")
dictionary = dict(line.split("|", 1) for line in
                  (root / "tools/english.txt").read_text(encoding="utf-8").splitlines())
pattern = re.compile("|".join(map(re.escape, sorted(dictionary, key=len, reverse=True))))
english = pattern.sub(lambda match: dictionary[match[0]].replace("␠", " "), source)
english = (english.replace('<html lang="zh-CN">', '<html lang="en">', 1)
           .replace('docs/design.zh.html', 'docs/design.en.html'))
for original, translated in {"，": ", ", "。": ". ", "；": "; ", "：": ": ",
                              "（": " (", "）": ")", "？": "?", "、": ", "}.items():
    english = english.replace(original, translated)
remaining = set(re.findall(r"[\u3400-\u9fff]+", english.replace(">中文<", "><")))
if remaining:
    raise SystemExit(f"Missing translations: {', '.join(sorted(remaining))}")
(root / "en.html").write_text(english, encoding="utf-8")
