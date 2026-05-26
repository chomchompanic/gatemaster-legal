#!/usr/bin/env python3
"""シンプル md→html 変換。GitHub Pages 公開用。

使い方:
    python3 build.py
→ privacy-policy.md / terms.md から同名の .html を生成。
"""
import re
import pathlib
import sys

HERE = pathlib.Path(__file__).parent

TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - MasterGate</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Yu Gothic", sans-serif;
    max-width: 720px; margin: 0 auto; padding: 24px; line-height: 1.7; }}
  h1 {{ font-size: 26px; }}
  h2 {{ margin-top: 32px; border-bottom: 1px solid #ccc; padding-bottom: 4px; }}
  h3 {{ margin-top: 20px; }}
  a {{ color: #5e5ce6; word-break: break-all; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; }}
  th, td {{ border: 1px solid #999; padding: 8px 12px; text-align: left; }}
  hr {{ margin: 32px 0; border: 0; border-top: 1px solid #ccc; }}
  code {{ background: rgba(125,125,125,.15); padding: 2px 6px; border-radius: 4px; }}
  .back {{ display: inline-block; margin-top: 32px; }}
</style>
</head>
<body>
{body}
<p class="back"><a href="./">← トップに戻る</a></p>
</body>
</html>
"""


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out = []
    in_table = False
    in_para = False

    def close_para():
        nonlocal in_para
        if in_para:
            out.append("</p>")
            in_para = False

    def close_table():
        nonlocal in_table
        if in_table:
            out.append("</tbody></table>")
            in_table = False

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and "---" in (lines[i + 1] if i + 1 < len(lines) else ""):
            close_para()
            # ヘッダ
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append("<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in cells) + "</tr></thead><tbody>")
            in_table = True
            i += 2
            continue
        if in_table and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
            i += 1
            continue
        close_table()

        if line.startswith("# "):
            close_para()
            out.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith("## "):
            close_para()
            out.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith("### "):
            close_para()
            out.append(f"<h3>{line[4:].strip()}</h3>")
        elif line.strip() == "---":
            close_para()
            out.append("<hr>")
        elif line.strip().startswith("- "):
            close_para()
            # 簡易リスト処理
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>")
            continue
        elif line.strip() == "":
            close_para()
        else:
            if not in_para:
                out.append("<p>")
                in_para = True
            else:
                out.append("<br>")
            out.append(line)

        i += 1

    close_para()
    close_table()
    html = "\n".join(out)
    # **bold** → <strong>
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    # [text](url) → <a>
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"<a href='\2'>\1</a>", html)
    # bare urls
    html = re.sub(r"(?<![\"'])(https?://[^\s<)]+)", r"<a href='\1'>\1</a>", html)
    return html


def build(name: str, title: str):
    src = HERE / f"{name}.md"
    dst = HERE / f"{name}.html"
    md = src.read_text(encoding="utf-8")
    body = md_to_html(md)
    dst.write_text(TEMPLATE.format(title=title, body=body), encoding="utf-8")
    print(f"Built {dst.name}")


if __name__ == "__main__":
    build("privacy-policy", "プライバシーポリシー")
    build("terms", "利用規約")
