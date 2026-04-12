# poker-trainer

poker-trainer/
├── backend/
│   ├── main.py            # FastAPIエントリーポイント・ルーティング
│   ├── models.py          # リクエスト/レスポンスの型定義
│   ├── engine.py          # 戦略評価ロジック（コア）
│   ├── scenarios.py       # 100ハンド分のシナリオデータ
│   └── storage.py         # GitHub Gist 連携
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── PokerTable.vue      # 描画（レスポンシブ）
│   │   │   ├── StrategyPicker.vue  # 戦略選択
│   │   │   └── ResultOverlay.vue   # 評価結果表示
│   │   ├── App.vue
│   │   └── main.js
│   └── index.html
└── requirements.txt