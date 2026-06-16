from pathlib import Path
import sys
import tempfile

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.core.config import RagConfig
from app.rag import LocalKnowledgeBase


def write_doc(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    with tempfile.TemporaryDirectory(prefix="spacemit-rag-heading-") as tmp_dir:
        root = Path(tmp_dir)
        knowledge_dir = root / "knowledge"
        write_doc(
            knowledge_dir / "risk.md",
            """# 高风险场景处置原则

## 必须优先升级的情况

发现穿孔、活动性泄漏、明显裂纹、结构变形或焊缝与承力关键部位受损时，应先隔离风险并升级复核。
""",
        )
        write_doc(
            knowledge_dir / "inspection.md",
            """# 储罐完整性检查范围

## 焊缝与接管

现场记录应覆盖接管、法兰、底圈板、平台连接处和可见腐蚀扩展边界。
""",
        )

        config = RagConfig(
            enabled=True,
            knowledge_dir=knowledge_dir,
            index_path=root / "index" / "knowledge_index.json",
            top_k=3,
            chunk_max_chars=220,
            min_score=0.8,
            max_context_chars=900,
            citation_limit=2,
            direct_answer_score=2.0,
        )
        kb = LocalKnowledgeBase(config)

        risk_hits = kb.search("高风险场景处置")
        assert risk_hits, "query by document title should return hits"

        section_hits = kb.search("焊缝与接管")
        assert section_hits, "query by section title should return hits"
        assert any(hit.title == "焊缝与接管" for hit in section_hits), "query by section title should preserve section match"

        print("ok", risk_hits[0].source_label, section_hits[0].source_label)


if __name__ == "__main__":
    main()
