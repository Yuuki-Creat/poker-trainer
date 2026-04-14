<script setup>
import { ref, onMounted, computed } from 'vue';
import PokerTable from './components/PokerTable.vue';
import StrategyPicker from './components/StrategyPicker.vue';
import ResultOverlay from './components/ResultOverlay.vue';

// 環境変数からベースURLを取得し、末尾のスラッシュを削除
const API_BASE = import.meta.env.VITE_BASE_URL || "";
const baseUrl = API_BASE.replace(/\/$/, "");
const scenarios = ref([]);
const currentScenario = ref(null);
const currentStrategy = ref('TAG');
const result = ref(null);

const stats = ref({
  currentHand: 0,
  totalScore: 0,
  history: []
});

const isGameOver = computed(() => stats.value.currentHand >= 100);

// シナリオ取得
const fetchScenarios = async () => {
  try {
    const res = await fetch(`${baseUrl}/api/scenarios`);
    scenarios.value = await res.json();
    nextHand();
  } catch (err) {
    console.error("Failed to Fetch scenarios:", err);
  }
};

const nextHand = () => {
  if (isGameOver.value) return;

  const randomIndex = Math.floor(Math.random() * scenarios.value.length);
  currentScenario.value = scenarios.value[randomIndex];
  result.value = null;
  stats.value.currentHand++;
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
        strategy_type: currentStrategy.value
      })
    });

    const data = await res.json();
    result.value = data;

    stats.value.totalScore += data.score;
  } catch (err) {
    console.error("Submit error:", err);
  }
};

onMounted(fetchScenarios);
</script>

<template>
  <div class="min-h-screen bg-slate-900 text-white p-4">
    <div class="max-w-md mx-auto mb-4 flex justify-between items-center bg-slate-800 p-3 rounded-xl border border-slate-700">
      <div>
        <p class="text-xs text-slate-400">Hand</p>
        <p class="font-mono text-lg">{{ stats.currentHand }} / 100</p>
      </div>
      <div class="text-right">
        <p class="text-xs text-slate-400">Total Score</p>
        <p class="font-mono text-lg text-yellow-400">{{ stats.totalScore }}</p>
      </div>
    </div>

    <div class="flex justify-center mb-6">
      <StrategyPicker v-model="currentStrategy" />
    </div>

    <div v-if="currentScenario" class="relative">
      <PokerTable 
        :scenario="currentScenario" 
        @action="submitAction" 
        :disabled="!!result || isGameOver"
      />
      
      <ResultOverlay 
        v-if="result" 
        :result="result" 
        :is-last="isGameOver"
        @next="nextHand" 
      />
    </div>

    <div v-if="isGameOver && !result" class="fixed inset-0 bg-slate-900/95 flex flex-col items-center justify-center p-6 z-50 text-center">
      <h2 class="text-4xl font-black mb-2 text-blue-400">SESSION COMPLETE</h2>
      <p class="text-slate-400 mb-8">100ハンドのトレーニングが終了しました</p>
      <div class="bg-slate-800 p-8 rounded-2xl border-2 border-blue-500 mb-8 w-full max-w-sm">
        <p class="text-sm text-slate-400 uppercase tracking-widest">Final Score</p>
        <p class="text-6xl font-mono font-bold text-white">{{ stats.totalScore }}</p>
      </div>
      <button @click="location.reload()" class="bg-blue-600 hover:bg-blue-500 px-8 py-4 rounded-full font-bold text-xl transition-all shadow-lg shadow-blue-900/20">
        RETRY SESSION
      </button>
    </div>
  </div>
</template>