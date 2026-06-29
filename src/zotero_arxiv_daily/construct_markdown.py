from datetime import datetime
from pathlib import Path
import re

from .protocol import Paper


def _sanitize_markdown(value: str | None) -> str:
    if value is None:
        return "Not provided"
    value = str(value).strip()
    return value if value else "Not provided"


def _paper_id(paper: Paper) -> str:
    for value in (paper.url, paper.pdf_url, paper.doi_url):
        if not value:
            continue
        match = re.search(r"(?:arxiv\.|abs/|pdf/)(\d{4}\.\d{4,5})(?:v\d+)?", value, flags=re.IGNORECASE)
        if match:
            return match.group(1)
    return "unknown"


def _links(paper: Paper) -> list[str]:
    links = []
    if paper.url:
        links.append(f"- Abstract: {paper.url}")
    if paper.pdf_url:
        links.append(f"- PDF: {paper.pdf_url}")
    if paper.doi_url:
        links.append(f"- DOI: {paper.doi_url}")
    return links or ["- Not provided"]


def render_markdown(papers: list[Paper], generated_at: datetime | None = None) -> str:
    generated_at = generated_at or datetime.now()
    date = generated_at.strftime("%Y-%m-%d")
    lines = [
        f"# Daily arXiv - {date}",
        "",
        f"- Source: GitHub Actions generated paper list",
        f"- Generated at: {generated_at.isoformat(timespec='seconds')}",
        f"- Paper count: {len(papers)}",
        "",
    ]

    if not papers:
        lines.extend([
            "## No Papers Today",
            "",
            "No new papers were selected for this run.",
            "",
        ])
        return "\n".join(lines)

    seen_ids: set[str] = set()
    skipped_duplicates: list[str] = []
    index = 1
    for paper in papers:
        paper_id = _paper_id(paper)
        if paper_id != "unknown" and paper_id in seen_ids:
            skipped_duplicates.append(f"{paper.title} ({paper_id})")
            continue
        seen_ids.add(paper_id)

        summary = paper.markdown_summary or _fallback_summary(paper)
        lines.extend([
            f"## {index}. {_sanitize_markdown(paper.title)}",
            "",
            f"- Source: {_sanitize_markdown(paper.source)}",
            f"- arXiv ID: {paper_id}",
            f"- Relevance: {round(paper.score, 1) if paper.score is not None else 'Unknown'}",
            "",
            "### Links",
            "",
            *_links(paper),
            "",
            "### Authors",
            "",
            _sanitize_markdown(", ".join(paper.authors)),
            "",
            "### Abstract",
            "",
            _sanitize_markdown(paper.abstract),
            "",
            summary.strip(),
            "",
        ])
        index += 1

    lines.extend([
        "## Processing Notes",
        "",
        f"- Duplicate papers skipped: {len(skipped_duplicates)}",
    ])
    lines.extend([f"  - {item}" for item in skipped_duplicates])
    return "\n".join(lines)


def write_markdown_summary(
    papers: list[Paper],
    output_dir: str | Path,
    generated_at: datetime | None = None,
) -> Path:
    generated_at = generated_at or datetime.now()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    date = generated_at.strftime("%Y-%m-%d")
    path = output_dir / f"{date}-daily-arxiv.md"
    if path.exists():
        path = output_dir / f"{date}-daily-arxiv-{generated_at.strftime('%H%M%S')}.md"

    content = render_markdown(papers, generated_at)
    path.write_text(content, encoding="utf-8")
    return path


def _fallback_summary(paper: Paper) -> str:
    tldr = _sanitize_markdown(paper.tldr)
    abstract = _sanitize_markdown(paper.abstract)
    return "\n".join([
        "### 中文一句话结论",
        "",
        f"基于已有摘要判断：{tldr}",
        "",
        "### English TL;DR",
        "",
        tldr,
        "",
        "### 中文详细总结",
        "",
        f"基于论文摘要，该工作主要内容如下：{abstract}",
        "",
        "### 方法 / 贡献",
        "",
        "未提供独立的方法细节；请参考摘要和论文链接。",
        "",
        "### 实验或数据",
        "",
        "未提供独立的实验或数据细节；请参考摘要和论文链接。",
        "",
        "### 值得关注点",
        "",
        "该条目的相关性来自 Zotero 语料相似度排序，可优先根据 relevance 和摘要判断是否精读。",
        "",
        "### 局限性",
        "",
        "自动总结主要基于标题、摘要和可用正文预览，可能遗漏全文中的实验细节。",
    ])
