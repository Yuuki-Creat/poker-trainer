<template>
  <div class="min-h-screen flex flex-col items-center">
    <header class="w-full p-4 bg-slate-800 text-white flex justify-between items-center shadow-lg">
      <h1 class="font-bold text-xl">TAG Poker Trainer</h1>
      <StrategyPicker v-model="currentStrategy" />
    </header>

    <main class="flex-1 w-full max-w-4xl p-4 flex flex-col items-center justify-center">
      <PokerTable 
        v-if="currentScenario"
        :scenario="currentScenario" 
        @action="sendAction"
      />
      
      <div v-else class="text-white animate-pulse">
        Loading Scenario...
      </div>
    </main>

    <ResultOverlay 
      v-if="result" 
      :result="result" 
      @next="loadNext" 
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PokerTable from './components/PokerTable.vue';
import StrategyPicker from './components/StrategyPicker.vue';
import ResultOverlay from './components/ResultOverlay.vue';

const API_BASE = import.meta.env.VITE_BASE_URL;
const baseUrl = API_BASE.replace(/\/$/, "");
const currentScenario = ref(null);
const currentStrategy = ref('TAG');
const result = ref(null);
const currentId = ref(1);


const fetchScenario = async () => {
    const res = await fetch(`${baseUrl}/api/scenarios/${currentId.value}`);
    // console.log(API_BASE)
    currentScenario.value = await res.json();
};

const sendAction = async (action) => {
    const res = await fetch(`${baseUrl}/api/evaluate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            scenario_id: currentScenario.value.id,
            user_action: action,
            strategy_type: currentStrategy.value
        })
    });
    result.value = await res.json();
}

const loadNext = () => {
    if (result.value && result.value.next_scenario_id) {
        currentId.value = result.value.next_scenario_id;
        fetchScenario(currentId.value)
    }
    result.value = null;
};

onMounted(() => fetchScenario(currentId.value))
</script>