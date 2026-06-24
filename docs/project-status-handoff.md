# 项目现状与交接说明

适用时间：`2026-06-24`

适用目的：给新的 Codex 对话、临时接手开发者、后续维护者快速建立上下文。此文档以**板端 `/mnt/ssd/spacemit_project`** 为唯一真源，不以 Windows 工作区为准。

## 1. 一句话总览

| 项目 | 当前状态 |
|---|---|
| 项目名称 | `spacemit_project` |
| 目标平台 | `Muse Pi Pro (K1)` |
| 唯一 canonical repo | `/mnt/ssd/spacemit_project` |
| GitHub 仓库 | `git@github.com:ggbxffcrqbb-lab/spacemit_project.git` |
| 当前主分支 | `main` |
| 当前板端提交 | `8bf5442` |
| 当前 GitHub `main` | 已与板端 `8bf5442` 同步 |
| Windows 工作区 | 仅作辅助编辑/传文件，不再作为 Git 真源 |

一句话结论：

项目已经完成板端正式工程收口、本地 RAG、增强知识导入、Phase 4 第一轮海工/油气/视觉缺陷补库，以及 `42/42` 现场问法回归命中；后续工作继续以板端为主推进。

## 2. 当前开发进度

### 2.1 已完成部分

| 模块 | 当前进度 | 说明 |
|---|---|---|
| 板端正式工程目录 | 已完成 | 真源固定为 `/mnt/ssd/spacemit_project` |
| GitHub 同步链路 | 已完成 | 当前板端主线已同步到 GitHub |
| Git 治理 | 已完成 | 以后默认只在板端操作 Git |
| ASR | 已完成基础接入 | 默认官方优化模型优先 |
| LLM | 已完成基础接入 | 默认 `qwen2.5:0.5b` |
| TTS | 已完成基础接入 | Matcha TTS 常驻路径稳定 |
| 常驻语音服务 | 已完成 | `voice-console / warmup / doctor` 已统一 |
| 本地 RAG | 已完成可维护版 | 本地知识库 + BM25/关键词检索 + 引用输出 |
| 知识导入器 | 已完成增强版 | 支持 `.md/.txt/.pdf/.docx`、递归导入、分类/标签 |
| RAG 检索增强 | 已完成第一轮 | 标题、章节标题已并入索引与打分 |
| 状态页 | 已完成 | 输出 `html/json/txt` 三份状态文件 |
| 公开资料/OCR 导入 | 已完成第一轮 | 已形成 `field_public_*` 与 `web_authority` |
| Phase 4 补库 | 已完成第一轮 | 已形成 `phase4_raw`、`phase4_cards_rules/sop/visual` |
| 回归测试 | 已完成第二轮 | `tests/rag_regression_suite.py` 当前 `42/42` 命中 |
| 维护文档 | 已更新 | README 与本交接文档已按 2026-06-24 现状更新 |

### 2.2 当前阶段判断

| 维度 | 判断 |
|---|---|
| 工程化程度 | 已从样例拼装进入正式维护态 |
| 板端开发能力 | 已具备 |
| 本地知识库能力 | 已超过最小闭环，进入持续补库与回归阶段 |
| GitHub 协作能力 | 已具备 |
| Windows 侧定位 | 次要工作区，不再承担 Git 权威职责 |
| 实机联调完备度 | 仍需按任务继续推进 |

## 3. 当前已验证的关键结果

| 项目 | 当前值 |
|---|---|
| 板端项目根目录 | `/mnt/ssd/spacemit_project` |
| 模型目录 | `/mnt/ssd/models` |
| 当前知识文档数 | `126` |
| 当前 chunk 数 | `15540` |
| Phase 4 原始导入层 | `data/knowledge/imported/phase4_raw/` |
| Phase 4 规则卡 | `data/knowledge/imported/phase4_cards_rules/` |
| Phase 4 SOP 卡 | `data/knowledge/imported/phase4_cards_sop/` |
| Phase 4 视觉判读卡 | `data/knowledge/imported/phase4_cards_visual/` |
| 板端 `rag-rebuild` | 已成功执行 |
| 板端 `rag_regression_suite.py` | 已成功执行，`42/42` 命中 |

## 4. 当前项目结构重点

| 路径 | 作用 |
|---|---|
| `app/main.py` | 统一 CLI 入口 |
| `app/voice/service.py` | 常驻语音服务主逻辑 |
| `app/rag/knowledge_base.py` | 本地检索与索引缓存 |
| `app/rag/importer.py` | 强化版知识导入器 |
| `app/ui/status_page.py` | 文本/HTML/JSON 状态页输出 |
| `scripts/voice.sh` | 板端统一脚本入口 |
| `scripts/knowledge_import.sh` | 知识导入快捷入口 |
| `scripts/build_phase4_knowledge_assets.py` | Phase 4 资料导入层与知识卡生成脚本 |
| `tests/rag_regression_suite.py` | 真实现场问法回归集 |
| `data/knowledge/imported/phase4_raw/` | Phase 4 原始正文导入层 |
| `data/knowledge/imported/phase4_cards_*` | Phase 4 结构化知识卡 |

## 5. 当前 Git 管理现状

| 项目 | 当前规则 |
|---|---|
| 真源仓库 | 只认板端 `/mnt/ssd/spacemit_project` |
| Git 提交位置 | 默认只在板端 canonical repo |
| GitHub 推送位置 | 默认只从板端推送 |
| Windows 仓库 | 不再保留 `.git`，仅作辅助工作区 |
| 大模型权重 | 不进 Git |
| 需要回退历史时 | 以板端 Git 提交记录为准 |

当前要特别提醒新的 Codex：

1. 不要把 Windows 目录当成 Git 权威状态。
2. 所有版本判断先看板端 `git status`、`git log`。
3. 如果需要修改文件，可以在 Windows 辅助编辑，但最后必须同步回板端、在板端验证、在板端提交。

## 6. 当前已知限制

| 项目 | 当前情况 | 影响 |
|---|---|---|
| `python -m app.main doctor` 直接运行 | 依赖环境未完整就绪时可能缺 `sounddevice` | 板端健康检查优先走 `bash scripts/voice.sh doctor` |
| 知识库规模 | 已扩到 `126` 篇，但仍可继续扩 | 回答质量仍可继续提升 |
| OCR 流程 | 仍有一部分依赖 Windows 侧整理 | 纯板端 OCR 还未工程化完毕 |
| 外设联调覆盖 | 需按任务继续补 | 相机/麦克风/更多板载能力仍需专项推进 |

## 7. 当前推荐下一步优先级

| 优先级 | 建议工作 |
|---|---|
| P1 | 继续导入真实巡检记录、扫描件 OCR、SOP、现场记录模板 |
| P1 | 按更真实的现场口语继续扩 `tests/rag_regression_suite.py` |
| P1 | 继续在板端执行 `rag-rebuild`、`rag-query`、`rag_regression_suite.py` 做闭环验证 |
| P2 | 优化 TTS 冷启动时间与常驻流程 |
| P2 | 把 OCR 清洗和知识卡生成进一步脚本化 |
| P2 | 继续补状态页和现场展示逻辑 |
| P3 | 按任务继续接相机、外设、多模态能力 |

## 8. 新对话接手时先做什么

### 8.1 先相信什么

| 应先相信 | 不应先相信 |
|---|---|
| 板端 `/mnt/ssd/spacemit_project` | Windows 本地目录的 Git 状态 |
| 板端 `git status` / `git log` | 历史对话里的旧提交号 |
| 板端 `rag-rebuild` / 回归结果 | Windows 侧的假设性判断 |

### 8.2 第一轮必做检查

```bash
ssh fyp@192.168.3.38 "cd /mnt/ssd/spacemit_project && git status --short --branch && git log --oneline --decorate -n 5"
ssh fyp@192.168.3.38 "cd /mnt/ssd/spacemit_project && bash scripts/voice.sh doctor"
ssh fyp@192.168.3.38 "cd /mnt/ssd/spacemit_project && PYTHONPATH=. python3 tests/rag_regression_suite.py"
```

### 8.3 如果需要继续做功能开发

推荐顺序：

1. 先在板端读当前代码与配置。
2. 如需批量整理资料，可在 Windows 侧辅助处理。
3. 修改后同步回板端。
4. 在板端执行验证。
5. 通过板端 canonical repo 提交并推送 GitHub。

## 9. 给新 Codex 的启动提示词

下面这段可以直接复制到新对话里：

```text
请先把 /mnt/ssd/spacemit_project 视为唯一 canonical repo，不要先相信 Windows 本地目录的 Git 状态，因为以后只在板端操作 Git。先通过 SSH 检查板端 git status、git log、bash scripts/voice.sh doctor，并阅读 docs/project-status-handoff.md、docs/git-maintenance.md、docs/phase3-rag-ui.md。当前板端与 GitHub 已同步到 8bf5442。当前知识库已有 126 篇文档、15540 个 chunks，Phase 4 第一轮补库已落在 data/knowledge/imported/phase4_raw 与 phase4_cards_rules/sop/visual，tests/rag_regression_suite.py 当前 42/42 命中。后续继续以板端为准推进补库、回归和实机验证。
```

## 10. 交接结论

| 结论 | 说明 |
|---|---|
| 项目已进入可维护状态 | 不再是样例堆叠阶段 |
| 板端真源明确 | `/mnt/ssd/spacemit_project` |
| GitHub 已同步 | 当前主线已与板端一致 |
| Windows 只保留辅助职责 | 以后不再承担 Git 权威角色 |
| Phase 4 已推进 | 补库、知识卡、回归验证均已落地 |
| 后续重点 | 扩真实资料、扩问法、继续板端闭环验证 |
