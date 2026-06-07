# ClipForge Workspace

视频制作产物输出目录。所有生成的视频、封面、音频等文件存放在此。

## 目录结构

- `2026/` — 按日期组织的视频输出
- `sources/` — 原始素材（视频、文档等）
- `bgm/` — 背景音乐素材
- `covers/` — 封面图片
- `.env-checked` — 环境检查标记文件

## 规则

- 不要删除或修改 `.env-checked`、`.gitignore`、`.gitattributes`
- 不要自动提交大文件（视频、音频）到 git
- 视频制作工作流遵循上级目录 `clipforge` 的管线定义
