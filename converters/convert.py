"""
原神角色 Skill 转换工具 —— convert.py

将 .trae/skills/*/SKILL.md 转换为多种 Agent 格式：
  python convert.py prompts     → 纯 Markdown Prompt（通用 Agent）
  python convert.py claude      → Claude Projects 格式
  python convert.py gpts        → ChatGPT GPTs 格式（JSON）
  python convert.py cursor      → Cursor Rules 格式

用法示例：
  python converters/convert.py prompts
"""

import os
import sys
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / ".trae" / "skills"


def parse_skill(filepath: Path) -> dict:
    """解析 SKILL.md，返回 {name, description, title, content}"""
    text = filepath.read_text(encoding="utf-8")
    # 提取 YAML frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    name = ""
    description = ""
    if fm_match:
        fm = fm_match.group(1)
        n = re.search(r'name:\s*"(.+?)"', fm)
        d = re.search(r'description:\s*"(.+?)"', fm)
        if n: name = n.group(1)
        if d: description = d.group(1)
    content = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL).strip()
    # 标题
    title_match = re.match(r"^# (.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else name
    return {
        "name": name,
        "description": description,
        "title": title,
        "content": content,
    }


def all_skills():
    """遍历所有 Skill 文件"""
    results = []
    for md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skill = parse_skill(md)
        skill["dirname"] = md.parent.name
        results.append(skill)
    return results


# ──────────────────────────────────────────────
#  输出格式
# ──────────────────────────────────────────────

def output_prompts(skills, out_dir: Path):
    """输出纯 Markdown Prompt（去掉 YAML 头，通用 Agent）"""
    out_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        path = out_dir / f"{s['dirname']}.md"
        path.write_text(s["content"], encoding="utf-8")
    print(f"✅ 已生成 {len(skills)} 个纯 Markdown Prompt → {out_dir}/")


def output_claude(skills, out_dir: Path):
    """输出 Claude Projects 可用的 System Prompt 文本"""
    out_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        text = (
            f"# Role: {s['title']}\n\n"
            f"## Description\n{s['description']}\n\n"
            f"{s['content']}"
        )
        path = out_dir / f"{s['dirname']}.md"
        path.write_text(text, encoding="utf-8")
    print(f"✅ 已生成 {len(skills)} 个 Claude 格式 → {out_dir}/")


def output_gpts(skills, out_dir: Path):
    """输出 ChatGPT GPTs 配置 JSON 列表"""
    out_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for s in skills:
        records.append({
            "name": s["title"],
            "description": s["description"],
            "instructions": s["content"],
        })
    path = out_dir / "gpts_roles.json"
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 已生成 GPTs 配置 → {path} ({len(records)} 个角色)")


def output_cursor(skills, out_dir: Path):
    """输出 Cursor Rules (.cursor/rules/)"""
    out_dir.mkdir(parents=True, exist_ok=True)
    for s in skills:
        text = f"# {s['title']}\n\n{s['description']}\n\n---\n\n{s['content']}"
        path = out_dir / f"{s['dirname']}.mdc"
        path.write_text(text, encoding="utf-8")
    print(f"✅ 已生成 {len(skills)} 个 Cursor Rule → {out_dir}/")


# ──────────────────────────────────────────────
#  主入口
# ──────────────────────────────────────────────

FORMATS = {
    "prompts": (output_prompts, ROOT / "prompts"),
    "claude":  (output_claude,  ROOT / "output" / "claude"),
    "gpts":    (output_gpts,    ROOT / "output" / "gpts"),
    "cursor":  (output_cursor,  ROOT / "output" / "cursor_rules"),
}


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in FORMATS:
        print("用法: python convert.py <格式>")
        print("可用格式:", ", ".join(FORMATS.keys()))
        print("示例: python converters/convert.py prompts")
        sys.exit(1)

    fmt = sys.argv[1]
    skills = all_skills()
    func, out_dir = FORMATS[fmt]
    func(skills, out_dir)
