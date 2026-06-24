# spacemit_project

Muse Pi Pro (K1) 板端正式工程。

## 当前结论

| 项目 | 当前状态 |
|---|---|
| 唯一真源 | `/mnt/ssd/spacemit_project` |
| Git 主操作位置 | 板端 canonical repo |
| Windows 侧定位 | 次要工作区，仅用于传文件、辅助编辑、操控板端 |
| GitHub 仓库 | `git@github.com:ggbxffcrqbb-lab/spacemit_project.git` |
| 当前阶段 | `Phase 4` 知识库扩充与板端可维护阶段 |
| 当前板端主线 | `main` |

## 当前重点

| 项目 | 说明 |
|---|---|
| 统一入口 | `PYTHONPATH=. python3 -m app.main` |
| 统一终端脚本 | `scripts/voice.sh` |
| 默认模式 | `qwen2.5:0.5b` |
| 极速模式 | `smollm2:135m` |
| 模型目录 | `/mnt/ssd/models` |
| 第三方依赖目录 | `/mnt/ssd/spacemit_project/third_party` |
| 日志目录 | `/mnt/ssd/logs/spacemit_project/voice` |
| 当前知识文档数 | `126` |
| 当前索引 chunk 数 | `15540` |
| 当前 RAG 回归 | `42/42` 命中 |
| 当前 RAG 资料层 | `web_authority`、`field_public_raw`、`field_public_ocr`、`phase4_raw` |
| 当前结构化知识卡 | `phase4_cards_rules`、`phase4_cards_sop`、`phase4_cards_visual` |

## Git 与工作区约定

| 项目 | 约定 |
|---|---|
| canonical repo | `/mnt/ssd/spacemit_project` |
| GitHub 提交 | 只从板端提交 |
| Windows 本地 `.git` | 不再保留 |
| Windows 副本作用 | 文件中转、资料整理、辅助生成文档，不作为版本真源 |
| 不再进 Git 的内容 | bootstrap `.onnx` / `.bin` 模型权重 |
| 正式模型落点 | `/mnt/ssd/models` |
| Windows 模型中转 | `D:\spacemit\tmp` |

## 当前目录重点

| 路径 | 作用 |
|---|---|
| `app/` | 正式业务代码 |
| `configs/` | 板端运行配置 |
| `scripts/` | 板端启动、自检、预热、知识处理脚本 |
| `tests/` | 板端回归测试与 smoke tests |
| `data/knowledge/` | 本地知识库正文与结构化知识卡 |
| `data/index/` | RAG 索引缓存 |
| `docs/` | 项目说明、维护文档、交接文档 |

## 当前已完成的关键能力

| 模块 | 状态 |
|---|---|
| 板端正式工程收口 | 已完成 |
| 本地 RAG 最小可用闭环 | 已完成 |
| 标题/章节增强检索 | 已完成 |
| 知识导入器 `.md/.txt/.pdf/.docx` | 已完成 |
| OCR/公开资料导入 | 已完成第一轮 |
| Phase 4 海工/油气/视觉缺陷补库 | 已完成第一轮 |
| 真实现场问法回归集 | 已扩到 `42` 条并全部命中 |
| GitHub 与板端主线同步 | 已完成 |

## 板端常用命令

```bash
cd /mnt/ssd/spacemit_project

# 板端健康检查 / 预热 / 交互
bash scripts/voice.sh doctor
bash scripts/voice.sh warmup
bash scripts/voice.sh voice-console

# RAG
PYTHONPATH=. python3 -m app.main --config configs/voice.yaml rag-rebuild
PYTHONPATH=. python3 -m app.main --config configs/voice.yaml rag-query "涂层起泡怎么办"

# 回归
PYTHONPATH=. python3 tests/rag_regression_suite.py
```

## Phase 4 当前落点

| 目录 | 说明 |
|---|---|
| `data/knowledge/imported/phase4_raw/` | 两批资料导入后的正文层 |
| `data/knowledge/imported/phase4_cards_rules/` | 油气/海工/升级复核规则卡 |
| `data/knowledge/imported/phase4_cards_sop/` | 有限空间、动火、海工检验 SOP 卡 |
| `data/knowledge/imported/phase4_cards_visual/` | 生锈、剥落、粉化、CUI 等视觉判读卡 |
| `scripts/build_phase4_knowledge_assets.py` | Phase 4 原始导入层与知识卡生成脚本 |
| `tests/rag_regression_suite.py` | 当前 42 条真实现场问法回归集 |

## 继续工作前先看

- [docs/project-status-handoff.md](docs/project-status-handoff.md)
- [docs/git-maintenance.md](docs/git-maintenance.md)
- [docs/phase3-rag-ui.md](docs/phase3-rag-ui.md)

## 当前最推荐的下一步

1. 继续扩真实巡检记录、扫描件 OCR、现场记录模板。
2. 继续把问法从 `42` 条往更真实的现场口语扩。
3. 在板端持续验证 `rag-rebuild`、`rag-query`、`rag_regression_suite.py`，不要只在 Windows 侧整理资料。
