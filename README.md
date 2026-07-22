# スタブロ 法的文書

App Store 申請時に必要なプライバシーポリシーと利用規約を管理。

## ファイル

| ファイル | 用途 |
|---|---|
| `privacy-policy.md` | プライバシーポリシー（編集対象） |
| `terms.md` | 利用規約（編集対象） |
| `build.py` | md → html 変換スクリプト |
| `index.html` / `*.html` | GitHub Pages 公開用（build.py で再生成） |

## ローカル更新フロー

1. `privacy-policy.md` または `terms.md` を編集
2. `python3 build.py` で HTML 再生成
3. `gatemaster-legal` リポジトリにコミット & プッシュ

## GitHub Pages 公開手順（初回のみ）

```bash
# このディレクトリの中身を専用リポジトリにする
cd /Users/chom/GateMaster/legal
git init
git add .
git commit -m "Initial legal documents"

# GitHub に gatemaster-legal リポジトリを作成（public）
gh repo create gatemaster-legal --public --source=. --push

# GitHub Pages を有効化
# Settings → Pages → Source: main / root
```

公開URL: `https://chomchompanic.github.io/gatemaster-legal/`

- プライバシーポリシー: `/privacy-policy.html`
- 利用規約: `/terms.html`

これらの URL を App Store Connect とアプリ内 PaywallView に設定します。
