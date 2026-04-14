<script setup>
const props = defineProps({
  scenario: {
    type: Object,
    default: null
  }
});

const formatCard = (cardStr) => {
  if (!cardStr || cardStr.length < 2) return { value: '', symbol: '', color: '' }
  const suitMap = {
    's': { symbol: '♠', color: 'text-white' }, 
    'h': { symbol: '♥', color: 'text-red-500' }, 
    'd': { symbol: '♦', color: 'text-red-500' }, 
    'c': { symbol: '♣', color: 'text-white' }
  };

  const value = cardStr.slice(0, -1).toUpperCase(); // 数字（10なども考慮）
  const suitKey = cardStr.slice(-1).toLowerCase();
  const suit = suitMap[suitKey] || { symbol: '?', color: 'text-gray-400' };

  return { value, ...suit }
};
</script>

<template>
  <div v-if="scenario && scenario.hand" class="max-w-md mx-auto">
    
    <div class="aspect-video bg-emerald-800 rounded-[100px] border-[12px] border-slate-700 relative flex items-center justify-center shadow-2xl overflow-hidden">
      <div class="absolute inset-4 border-2 border-emerald-700/50 rounded-[80px]"></div>
      
      <div class="flex space-x-3 z-10">
        <div v-for="(cardStr, index) in scenario.hand" :key="index" 
             class="w-16 h-24 bg-white rounded-lg flex flex-col items-center justify-center shadow-xl border border-slate-200 transform hover:scale-105 transition-transform">
          
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

      <div class="absolute bottom-6 bg-slate-900/80 px-4 py-1 rounded-full border border-slate-600">
        <span class="text-xs font-bold text-slate-300 uppercase">Position:</span>
        <span class="ml-2 text-sm font-black text-white">{{ scenario.position }}</span>
      </div>
    </div>
  </div>

  <div v-else class="h-64 flex items-center justify-center text-slate-500 italic">
    Shuffling cards...
  </div>
</template>