<script setup>
const props = defineProps({
  scenario: {
    type: Object,
    default: null
  },
  // 動的なハンド用
  hand: {
    type: Array,
    default: () => []
  },
  disabled: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits(['action'])

const formatCard = (cardStr) => {
  if (!cardStr || cardStr.length < 2) return { value: '', symbol: '', color: '' }

  const suitMap = {
    's': { symbol: '♠', color: 'text-slate-900' }, 
    'h': { symbol: '♥', color: 'text-red-500' }, 
    'd': { symbol: '♦', color: 'text-red-500' }, 
    'c': { symbol: '♣', color: 'text-slate-900' }
  };

  const value = cardStr.slice(0, -1).toUpperCase();
  const suitKey = cardStr.slice(-1).toLowerCase();
  const suit = suitMap[suitKey] || { symbol: '?', color: 'text-gray-400' };

  return { value, ...suit }
};
</script>

<template>
  <div v-if="scenario" class="max-w-md mx-auto p-4">
    <div class="aspect-video bg-emerald-800 rounded-[100px] border-[12px] border-slate-700 relative flex flex-col items-center justify-center shadow-2xl mb-8">
      <div class="absolute inset-4 border-2 border-emerald-700/50 rounded-[80px]"></div>

      <div class="absolute top-6 right-8 bg-blue-600 px-3 py-1 rounded text-[10px] font-black uppercase text-white shadow-lg z-20">
        {{ scenario.phase }}
      </div>

      <div v-if="scenario.board && scenario.board.length > 0" class="flex space-x-1 mb-4 z-10">
        <div v-for="(cardStr, index) in scenario.board" :key="'board-'+index"
             class="w-10 h-14 bg-white rounded-md flex flex-col items-center justify-center shadow-lg border border-slate-200">
          <span class="text-sm font-black leading-none" :class="formatCard(cardStr).color">
            {{ formatCard(cardStr).value }}
          </span>
          <span class="text-lg leading-none mt-0.5" :class="formatCard(cardStr).color">
            {{ formatCard(cardStr).symbol }}
          </span>
        </div>
      </div>

      <div class="flex space-x-3 z-10">
        <div v-for="(cardStr, index) in (hand && hand.length > 0 ? hand : scenario.hand)" :key="'hand-'+index"
             class="w-16 h-24 bg-white rounded-lg flex flex-col items-center justify-center shadow-xl border border-slate-200">
          <template v-if="cardStr">
            <span class="text-2xl font-black leading-none" :class="formatCard(cardStr).color">
              {{ formatCard(cardStr).value }}
            </span>
            <span class="text-3xl leading-none mt-1" :class="formatCard(cardStr).color">
              {{ formatCard(cardStr).symbol }}
            </span>
          </template>
        </div>
      </div>

      <div class="absolute right-10 bottom-6 bg-slate-900/80 px-4 py-1 rounded-full border border-slate-600">
        <span class="text-xs font-bold text-slate-300 uppercase tracking-tighter">Position:</span>
        <span class="ml-2 text-sm font-black text-white">{{ scenario.position }}</span>
      </div>
    </div>

    <div class="grid grid-cols-3 gap-3">
      <button 
        v-for="btnAction in ['FOLD', 'CHECK', 'CALL', 'BET', 'RAISE']" 
        :key="btnAction"
        @click="emit('action', btnAction)"
        :disabled="disabled"
        class="py-4 rounded-xl font-black transition-all active:scale-95 disabled:opacity-30 shadow-md border-b-4 border-slate-300 active:border-b-0"
        :class="btnAction === 'FOLD' ? 'bg-slate-700 text-white border-slate-900' : 'bg-slate-100 text-slate-900'"
      >
        {{ btnAction }}
      </button>
    </div>
  </div>

  <div v-else class="h-64 flex flex-col items-center justify-center text-slate-500 italic">
    <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500 mb-4"></div>
    Shuffling cards...
  </div>
</template>