<script setup>
const formatCard = (cardStr) => {
  if (!cardStr || cardStr.length < 2) return { value: '', symbol: '', color: '' }
  const suitMap = {
    's': { symbol: '♠', color: 'text-white' }, 
    'h': { symbol: '♥', color: 'text-red-500' }, 
    'd': { symbol: '♦', color: 'text-red-500' }, 
    'c': { symbol: '♣', color: 'text-white' }
  };
  const value = cardStr.slice(0, -1);
  const suitKey = cardStr.slice(-1).toLowerCase();
  const suit = suitMap[suitKey] || { symbol: '?', color: 'text-gray-400' };
  return { value, ...suit }
};
</script>

<template>
  <div class="flex space-x-2 z-10">
    <div v-for="(cardStr, index) in scenario.hand" :key="index" 
         class="w-16 h-24 bg-white rounded-lg flex flex-col items-center justify-center shadow-xl border border-slate-200">
      
      <template v-if="cardStr">
        <span class="text-2xl font-bold leading-none" :class="formatCard(cardStr).color">
          {{ formatCard(cardStr).value }}
        </span>
        <span class="text-3xl leading-none" :class="formatCard(cardStr).color">
          {{ formatCard(cardStr).symbol }}
        </span>
      </template>
    </div>
  </div>
</template>
