# ClipForge Workspace

视频制作产物输出目录。所有生成的视频、封面、音频等文件存放在此。

## 目录结构

- `2026/` — 按日期组织的视频输出
- `sources/` — 原始素材（视频、文档等）
- `bgm/` — 背景音乐素材（本地磁盘存储，未入库 GitHub，大文件）
- `covers/` — 封面图片
- `.env-checked` — 环境检查标记文件

## 规则

- 默认在当前 workspace 目录内操作。workspace 与父目录 `video-clipforge` 是两个独立 git 仓库，禁止 `cd` / `git -C` 到父目录执行 git 或文件写操作（会误操作另一个仓库）——除非用户明确要求操作其他目录
- 不要删除或修改 `.env-checked`、`.gitignore`、`.gitattributes`
- 不要自动提交大文件（视频、音频）到 git
- 视频制作工作流遵循上级目录 `clipforge` 的管线定义
