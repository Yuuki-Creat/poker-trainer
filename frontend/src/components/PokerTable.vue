<script setup>
const props = defineProps(['scenario', 'disabled']);
const emit = defineEmits(['action']);

const formatCard = (cardStr) => {
  const suitMap = {
    's': { symbol: '♠', color: 'text-white' }, 
    'h': { symbol: '♥', color: 'text-red-500' }, 
    'd': { symbol: '♦', color: 'text-red-500' }, 
    'c': { symbol: '♣', color: 'text-white' }
  };
  const value = cardStr.slice(0, -1);
  const suit = suitMap[cardStr.slice(-1)];
  return { value, ...suit }
};
</script>

<template>
  <div class="max-w-md mx-auto">
    <div class="aspect-video bg-emerald-800 rounded-[100px] border-[12px] border-slate-700 relative flex items-center justify-center shadow-2xl overflow-hidden">
      <div class="absolute inset-4 border-2 border-emerald-700/50 rounded-[80px]"></div>
      
      <div class="flex space-x-2 z-10">
        <div v-for="card in scenario.hand" :key="card" 
             class="w-16 h-24 bg-white rounded-lg flex flex-col items-center justify-center shadow-xl border border-slate-200">
          <span class="text-2xl font-bold leading-none" :class="formatCard(card).color">{{ formatCard(card).value }}</span>
          <span class="text-3xl leading-none" :class="formatCard(card).color">{{ formatCard(card).symbol }}</span>
        </div>
      </div>

      <div class="absolute bottom-6 bg-slate-900/80 px-4 py-1 rounded-full border border-slate-600">
        <span class="text-xs font-bold text-slate-300 uppercase tracking-tighter">Position:</span>
        <span class="ml-2 text-sm font-black text-white">{{ scenario.position }}</span>
      </div>

      <div class="absolute top-6 right-6 bg-blue-600 px-3 py-1 rounded text-[10px] font-black uppercase">
        {{ scenario.phase }}
      </div>
    </div>

    <div class="grid grid-cols-3 gap-2 mt-8">
      <button v-for="a in ['FOLD', 'CHECK', 'CALL', 'BET', 'RAISE']" :key="a"
              @click="emit('action', a)"
              :disabled="disabled"
              class="py-4 rounded-xl font-black transition-all active:scale-95 disabled:opacity-30 disabled:pointer-events-none shadow-md"
              :class="a === 'FOLD' ? 'bg-slate-700 hover:bg-slate-600' : 'bg-slate-100 text-slate-900 hover:bg-white'">
        {{ a }}
      </button>
    </div>
  </div>
</template>
