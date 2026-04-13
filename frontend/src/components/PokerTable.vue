<template>
  <div class="flex flex-col items-center justify-between w-full h-full text-white">
    <div class="w-full max-w-md mt-4">
      <div class="flex justify-between text-xs mb-1">
        <span>Hand {{ currentId }} / 100</span>
        <span>Strategy: {{ selectedStrategy }}</span>
      </div>
      <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden">
        <div class="bg-blue-500 h-full transition-all duration-500" :style="{ width: currentId + '%' }"></div>
      </div>
    </div>

    <div class="relative w-full max-w-xl aspect-[4/3] bg-emerald-800 rounded-[100px] border-[12px] border-slate-800 flex flex-col items-center justify-center shadow-inner my-8">
      <div v-if="scenario.board && scenario.board.length > 0" class="flex gap-2 mb-8">
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
      <button 
        v-for="btn in actions" 
        :key="btn" 
        @click="$emit('action', btn)" 
        class="bg-slate-100 text-slate-900 py-4 rounded-2xl font-black text-lg active:scale-95 transition-transform hover:bg-white disabled:opacity-50"
        :disabled="!!result"
      >
        {{ btn }}
      </button>
    </div>

    <ResultOverlay 
      v-if="result" 
      :result="result" 
      @next="$emit('next')" 
    />
  </div>
</template>

<script setup>
import ResultOverlay from './ResultOverlay.vue';

const props = defineProps({
  scenario: Object,
  currentId: Number,
  selectedStrategy: String,
  result: Object
});

const emit = defineEmits(['action', 'next']);

const actions = ['FOLD', 'CHECK', 'CALL', 'BET', 'RAISE'];
</script>