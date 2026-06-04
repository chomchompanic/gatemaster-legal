# プライバシーポリシー

**最終更新日: 2026年6月4日**

chom（以下「開発者」）は、iOS アプリ「MasterGate」（以下「本アプリ」）におけるユーザーのプライバシーを最大限尊重します。本ポリシーは、本アプリが取り扱う情報と、その利用方法を説明します。

---

## 1. 取り扱う情報

### 1.1 端末内にのみ保存される情報（外部送信なし）

以下の情報は、ユーザーの端末内（App Group 共有ストレージ・ローカル SQLite）にのみ保存され、開発者を含む第三者には送信されません。

- ブロック対象として選択したアプリ／ジャンルの識別子（FamilyControls API による不透明なトークン。アプリ名や使用履歴は含まれません）
- 学習カードの登録内容（ユーザー追加分含む）
- クイズの解答履歴・正誤・習得状態
- 通知許可状態
- アプリ内設定（クイズ問題数、上限時間など）
- アプリ利用時間予算と消費状況

### 1.2 外部に送信される情報（明示的な操作時のみ）

ユーザーが下記の機能を**自ら使用した場合に限り**、必要な情報が外部サーバーに送信されます。

| 機能 | 送信される情報 | 送信先 | 利用枠 |
|---|---|---|---|
| AI問題生成 | ユーザーが入力したテーマ文字列 | 開発者運用の Cloudflare Workers サーバー → Google Gemini API | 無料枠は生涯10問、超過後はプレミアム |
| 写真からの取込（AI後処理） | OCR で認識されたテキスト | 同上 | 無料枠は月10回、超過後はプレミアム |
| プレミアム購入 | App Store 決済レシート | Apple, RevenueCat | — |
| 広告配信（無料ユーザーのみ） | 広告識別子（IDFA）、診断情報、おおまかな国・地域 | Google AdMob | プレミアム購入で広告非表示 |

これらの通信内容には、ユーザー個人を特定する情報は含まれません。AI機能の無料枠超過時はペイウォール（プレミアム購入導線）が表示されますが、外部送信は発生しません。写真からの取込は端末内 Vision Framework で OCR 処理されるため、AI 後処理を行わない場合は外部送信ゼロです。

広告配信については、初回起動時に App Tracking Transparency（ATT）の許可ダイアログが表示されます。トラッキングを許可しない場合でも、関連性の低い広告は表示されます（広告自体は非表示にできません。プレミアム会員になると広告は完全に非表示になります）。

### 1.3 取得しない情報

- 氏名、メールアドレス、電話番号などの個人識別情報
- 位置情報（おおまかな国・地域を除く。AdMob が広告配信のために自動取得）
- 連絡先・写真・カレンダー等の他アプリのデータ
- ブロック対象アプリの実際の使用履歴（iOS FamilyControls の制約により開発者は取得不可）

---

## 2. 情報の利用目的

- 本アプリの機能を提供するため
- AI問題生成および OCR テキスト解析の結果をユーザーに返すため
- 課金処理の検証・購入の復元のため

開発者は、上記目的以外で情報を利用しません。

---

## 3. 第三者サービス

| サービス | 役割 | プライバシーポリシー |
|---|---|---|
| Apple（App Store / iOS） | アプリ配信・課金処理・端末 API | https://www.apple.com/jp/legal/privacy/ |
| Google Gemini API | AI問題生成・OCR後処理 | https://policies.google.com/privacy |
| Google AdMob | 広告配信（無料ユーザーのみ） | https://policies.google.com/technologies/ads |
| Cloudflare Workers | AI機能のための中継サーバー | https://www.cloudflare.com/privacypolicy/ |
| RevenueCat | サブスクリプション管理 | https://www.revenuecat.com/privacy |

これらのサービスへの送信内容は §1.2 のとおりです。Google および Cloudflare は API リクエストを一定期間サーバーログとして保管する場合があります。

---

## 4. データの保管と保護

- 端末内データは iOS 標準のサンドボックスおよび App Group コンテナで保護されます
- AI関連通信は HTTPS で暗号化されます
- 開発者の Cloudflare Workers サーバーには、リクエスト内容を恒久的に保管しません（リアルタイム中継のみ）
- 端末紛失時にデータが流出するリスクは、iOS の標準的なセキュリティ機能（パスコード／生体認証／リモートワイプ）に依存します

---

## 5. データの削除

本アプリをアンインストールすると、端末内に保存された全てのデータが削除されます。第三者サービス側のログ（Google・Cloudflare 等）は各サービスのポリシーに従って自動的に保持期限後に削除されます。

---

## 6. 子どもの利用について

本アプリは、保護者がお子様の学習を支援する用途での利用も想定しています。13歳未満のお子様が本アプリを利用する場合は、必ず保護者の同意と監督のもとでご利用ください。

本アプリは、お子様から意図的に個人情報を収集することはありません。本アプリで取り扱う学習進捗・クイズ履歴等は端末内にのみ保存されます（§1.1 参照）。

保護者の皆様へ：本アプリには、お子様が設定（ジャンル選択・解除時間など）を勝手に変更できないようにする「親PIN」機能が用意されています。設定画面からご利用ください。

---

## 7. 本ポリシーの変更

本ポリシーは、法令の改正やサービスの変更に伴い更新される場合があります。変更があった場合は、本ページの「最終更新日」を改定し、必要に応じてアプリ内で通知します。

---

## 8. お問い合わせ

本ポリシーや個人情報の取り扱いについてご質問がある場合は、以下までご連絡ください。

**連絡先:** chomurashouta@gmail.com

---

## English Summary

MasterGate (the "App") respects user privacy.

**Stored locally only (never transmitted):** blocked-app tokens, learning cards and progress, quiz history, notification permission state, in-app settings, usage budget.

**Transmitted externally (only when you actively use the feature):**
- AI question generation: your typed theme is sent through our Cloudflare Workers proxy to Google Gemini.
- Photo import (AI post-processing): the OCR-recognized text is sent the same way.
- Subscription purchase: receipt is processed via Apple and RevenueCat.

**Not collected:** name, email, phone, location, contacts, photos, advertising IDs, actual usage history of blocked apps.

Uninstalling the App deletes all locally stored data. For inquiries, contact chomurashouta@gmail.com.
