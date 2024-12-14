<div align="center">
  <img src="assets/header.svg" alt="Cat Tech Dashboard" width="800">
</div>

# 🐱 猫猫テクノロジー ダッシュボード

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B.svg)](https://streamlit.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 概要

猫猫テクノロジー ダッシュボードは、猫に関する様々なデータを視覚的に表示する対話型ダッシュボードアプリケーションです。基本情報から統計データまで、猫に関する包括的な情報を提供します。

## 🌟 主な機能

- 猫の基本的な特徴の表示
- 人気品種のグラフ表示
- 行動パターンの円グラフ表示
- 年間統計データの表示
- 人気度トレンドの時系列表示

## 🔧 プロジェクト構造

```
cat-tech-dashboard/
├── assets/           # アセットファイル
│   └── header.svg    # READMEヘッダー画像
├── data/             # データ関連ファイル
│   └── cat_data.py   # 猫のデータ定義
├── pages/            # ページコンポーネント
│   ├── basic_info.py # 基本情報ページ
│   └── statistics.py # 統計データページ
├── app.py            # メインアプリケーション
├── config.py         # アプリケーション設定
└── README.md         # プロジェクトドキュメント
```

## 💻 技術スタック

- **Python**: メインのプログラミング言語
- **Streamlit**: Webアプリケーションフレームワーク
- **Pandas**: データ処理と分析
- **Plotly**: インタラクティブな可視化

## 🚀 セットアップと実行

1. 依存パッケージのインストール:
```bash
pip install streamlit pandas plotly
```

2. アプリケーションの実行:
```bash
streamlit run app.py
```

## 📊 実装された改善点

### 1. プロジェクト構造の最適化
- **config.py**: アプリケーション設定の一元管理
- **data/cat_data.py**: データの集約
- **pages/**: 各ページのロジックを分離
- **app.py**: メインアプリケーションの簡素化

### 2. コードの品質向上
- 単一責任の原則に基づくモジュール分割
- 関数の責務を明確化
- 適切なドキュメント文字列の追加
- 設定とデータの分離

### 3. メンテナンス性の向上
- データ更新が容易
- 新機能追加が簡単
- コードの再利用性が向上
- テストが書きやすい構造

## 🔍 使用方法

1. サイドバーメニューから表示したいページを選択
2. 「基本情報」ページでは猫の特徴や行動パターンを確認
3. 「統計データ」ページでは詳細な統計情報とトレンドを確認

## 🤝 コントリビューション

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。
