# Swim Dynasty

[English](README.md) · [游戏设计](docs/design.zh.html)

Swim Dynasty 是一款离线大学游泳经营游戏。你可以为队员编组、安排泳池与陆上训练、推进周回合并设置比赛阵容。

```sh
git clone https://github.com/davidliu-swimdad/swim-dynasty.git
cd swim-dynasty
python3 -m http.server 8000 --bind 127.0.0.1
```

打开 [中文](http://127.0.0.1:8000/) 或 [English](http://127.0.0.1:8000/en.html)。页面顶部可以切换语言，两种语言共用同一个浏览器存档。建议使用新版 Chromium 浏览器，以支持目录导入和 ZIP 解压。克隆完成后，游戏与演示数据可断网运行。

首次试玩使用虚构队伍。想试导入时，在「数据包」页选择本仓库的 `packs/` 目录，再选择开档日期并加载演示赛季。导入大学数据时，请选择包含各校独立 ZIP 的目录。多校总包只需解压外层，保留内层各校 ZIP。每所有兼容赛季包的学校都能单独开档。

后续可通过 [GitHub Releases](https://github.com/davidliu-swimdad/swim-dynasty/releases) 更新带版本的离线包。数据采集流程独立运行，仓库提供游戏代码、语言资源、设计和虚构演示数据。

更新中文界面程序后，可以编辑 `tools/english.txt` 并运行 `python3 tools/build_english.py`，生成随游戏发布的英文页面。

## 许可证

游戏代码采用 [GNU AGPL v3.0](LICENSE)。离线数据包通过 Release 附件单独分发。
