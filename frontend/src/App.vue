<template>
  <div class="min-h-screen flex flex-col items-center bg-slate-900">
    <header class="w-full p-4 bg-slate-800 text-white flex justify-between items-center shadow-lg">
      <h1 class="font-bold text-xl">TAG Poker Trainer</h1>
      <StrategyPicker v-model="currentStrategy" />
    </header>

    <main class="flex-1 w-full max-w-4xl p-4 flex flex-col items-center justify-center">
      <PokerTable 
        v-if="currentScenario"
        :scenario="currentScenario" 
        :current-id="currentId"
        :selected-strategy="currentStrategy"
        :result="result"
        @action="submitAction"
        @next="loadNext"
      />
      
      <div v-else class="text-white animate-pulse text-xl">
        Loading Scenario...
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PokerTable from './components/PokerTable.vue';
import StrategyPicker from './components/StrategyPicker.vue';

// 環境変数からベースURLを取得し、末尾のスラッシュを削除
const API_BASE = import.meta.env.VITE_BASE_URL || "";
const baseUrl = API_BASE.replace(/\/$/, "");

const currentScenario = ref(null);
const currentStrategy = ref('TAG');
const result = ref(null);
const currentId = ref(1);

// シナリオ取得
const fetchScenario = async () => {
  try {
    const res = await fetch(`${baseUrl}/api/scenarios/${currentId.value}`);
    if (!res.ok) throw new Error("Failed to fetch scenario");
    currentScenario.value = await res.json();
  } catch (err) {
    console.error("Fetch error:", err);
  }
};

// アクション送信（判定）
const submitAction = async (action) => {
  try {
    const res = await fetch(`${baseUrl}/api/evaluate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        scenario_id: currentScenario.value.id,
        user_action: action,
        strategy_type: currentStrategy.ref || currentStrategy.value // refの考慮
      })
    });
    if (!res.ok) throw new Error("Evaluation failed");
    result.value = await res.json();
  } catch (err) {
    console.error("Submit error:", err);
  }
};

// 次のハンドへ進む
const loadNext = () => {
  if (result.value && result.value.next_scenario_id) {
    currentId.value = result.value.next_scenario_id;
    currentScenario.value = null; // ローディング表示にするため一旦クリア
    fetchScenario();
  }
  result.value = null; // 結果モーダルを閉じる
};

onMounted(fetchScenario);
</script>