# Swim Dynasty

[中文](README.zh.md) · [Game design](docs/design.en.html)

Swim Dynasty is an offline college swimming coaching game. Assign training groups, plan pool and dryland sessions, advance weekly, and build race lineups.

```sh
git clone https://github.com/davidliu-swimdad/swim-dynasty.git
cd swim-dynasty
python3 -m http.server 8000 --bind 127.0.0.1
```

Open [English](http://127.0.0.1:8000/en.html) or [中文](http://127.0.0.1:8000/). Use the language links at the top to switch while keeping the same browser save. Use a recent Chromium browser for folder imports and ZIP decompression. Once cloned, the game and bundled demo run without internet access.

The initial save starts with a fictional team. To try importing, open **Packs**, select the repository’s `packs/` folder, choose a start date, and load the demo season. To import school data, select a folder containing individual season ZIPs. Extract an outer multi-school ZIP first and keep the individual ZIPs intact. Each school with a compatible season pack can be opened separately.

Versioned offline packs can be attached to [GitHub Releases](https://github.com/davidliu-swimdad/swim-dynasty/releases). The data collection pipeline runs separately. This repository includes the game, its localization, design, and fictional demo.

To update English UI copy, edit `tools/english.txt` and run `python3 tools/build_english.py` after changing the Chinese source page. The generated English page ships with the game.
