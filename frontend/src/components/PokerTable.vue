<template>
  <div class="flex flex-col items-center justify-between min-h-screen bg-slate-900 p-4 text-white">
    <div class="w-full max-w-md mt-4">
      <div class="flex justify-between text-xs mb-1">
        <span>Hand {{ currentId }} / 100</span>
        <span>Strategy: {{ selectedStrategy }}</span>
      </div>
      <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden">
        <div class="bg-blue-500 h-full transition-all" :style="{ width: (currentId) + '%' }"></div>
      </div>
    </div>

    <div class="relative w-full max-w-xl aspect-[4/3] bg-emerald-800 rounded-[100px] border-[12px] border-slate-800 flex flex-col items-center justify-center shadow-inner">
      <div v-if="scenario.board.length > 0" class="flex gap-2 mb-8">
        <div v-for="card in scenario.board" :key="card" class="w-12 h-16 bg-white rounded shadow text-black flex items-center justify-center font-bold">
          {{ card }}
        </div>
      </div>
      <div class="flex gap-4">
        <div v-for="card in scenario.hand" :key="card" class="w-16 h-24 bg-white rounded-lg shadow-xl text-black flex items-center justify-center text-xl font-bold border-2 border-slate-300">
          {{ card }}
        </div>
      </div>
      <div class="absolute bottom-6 bg-black/50 px-4 py-1 rounded-full text-sm">
        Position: {{ scenario.position }}
      </div>
    </div>

    <div class="grid grid-cols-3 gap-3 w-full max-w-md pb-8">
      <button v-for="btn in actions" :key="btn" @click="submitAction(btn)" 
        class="bg-slate-100 text-slate-900 py-4 rounded-2xl font-black text-lg active:scale-95 transition-transform hover:bg-white">
        {{ btn }}
      </button>
    </div>

    <ResultOverlay v-if="result" :data="result" @next="fetchNext" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import ResultOverlay from './ResultOverlay.vue';

const scenario = ref({ hand: [], board: [], position: '', id: 1 });
const currentId = ref(1);
const selectedStrategy = ref('TAG');
const result = ref(null);
const actions = ['FOLD', 'CHECK', 'CALL', 'BET', 'RAISE'];

// const fetchNext = async () => {
//     result.value = null;
//     const res = await fetch(`/api/scenarios/${currentId.value}`);
//     scenario.value = await res.json();
// };

const submitAction = async (act) => {
    const res = await fetch('/api/evaluate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            scenario_id: scenario.value.id,
            user_action: act,
            strategy_type: selectedStrategy.value
        })
    });
    result.value = await res.json();
    currentId.value = result.value.next_scenario_id || 1;
}

onMounted(fetchNext);
</script>