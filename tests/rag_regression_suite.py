from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.core.config import load_app_config
from app.rag import LocalKnowledgeBase


QUERIES = [
    "涂层起泡怎么办",
    "发现裂纹能不能先补漆",
    "储罐外壁腐蚀如何初判",
    "保温层下疑似腐蚀怎么处理",
    "进入罐内前需要检查什么",
    "进入受限空间只待几分钟可以吗",
    "动火前要确认哪些风险",
    "在封闭支撑腿上直接焊一下行不行",
    "高风险场景处置",
    "什么时候不能只做表面补漆",
    "阴极保护和涂层哪个更重要",
    "储罐该看哪些地方",
    "巡检记录要写什么",
    "发现锈水回渗说明什么",
    "暂时不漏还要不要管",
    "储罐底板腐蚀能不能直接补涂",
]


def main():
    config = load_app_config("configs/voice.yaml")
    kb = LocalKnowledgeBase(config.rag)

    hit_count = 0
    for index, query in enumerate(QUERIES, start=1):
        hits = kb.search(query, top_k=3)
        if hits:
            hit_count += 1
            top = hits[0]
            print(
                f"[{index:02d}] HIT  | {query} | {top.title} | {Path(top.source_path).name} | score={top.score}"
            )
        else:
            print(f"[{index:02d}] MISS | {query}")

    print(f"summary: {hit_count}/{len(QUERIES)} queries returned hits")


if __name__ == "__main__":
    main()
