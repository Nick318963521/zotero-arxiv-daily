"""Tests for zotero_arxiv_daily.construct_markdown."""

from datetime import datetime

from tests.canned_responses import make_sample_paper
from zotero_arxiv_daily.construct_markdown import render_markdown, write_markdown_summary


def test_render_markdown_with_papers():
    paper = make_sample_paper(
        title="A Useful Paper",
        score=7.6,
        tldr="This is a concise English TL;DR.",
        markdown_summary="""### 中文一句话结论

这篇论文值得快速浏览。

### English TL;DR

This paper is worth a quick scan.

### 中文详细总结

它提出了一个实用方法。

### 方法 / 贡献

提出新方法。

### 实验或数据

摘要未说明。

### 值得关注点

相关性较高。

### 局限性

需要阅读全文确认。""",
    )

    markdown = render_markdown([paper], datetime(2026, 6, 28, 8, 30))

    assert "# Daily arXiv - 2026-06-28" in markdown
    assert "## 1. A Useful Paper" in markdown
    assert "- arXiv ID: 2026.00001" in markdown
    assert "### 中文一句话结论" in markdown
    assert "This paper is worth a quick scan." in markdown


def test_write_markdown_summary_uses_unique_filename(tmp_path):
    paper = make_sample_paper(title="A Useful Paper", tldr="Short summary.")
    generated_at = datetime(2026, 6, 28, 8, 30, 5)

    first = write_markdown_summary([paper], tmp_path, generated_at)
    second = write_markdown_summary([paper], tmp_path, generated_at)

    assert first.name == "2026-06-28-daily-arxiv.md"
    assert second.name == "2026-06-28-daily-arxiv-083005.md"
    assert first.exists()
    assert second.exists()
