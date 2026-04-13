<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
    <div class="bg-white w-full max-w-sm rounded-3xl p-8 text-center shadow-2xl transform transition-all scale-100">
      <div :class="statusClass" class="inline-block px-4 py-1 rounded-full text-xs font-bold mb-4">
        {{ result.status || (result.score === 100 ? 'CORRECT' : 'MISTAKE') }}
      </div>
      
      <h2 class="text-5xl font-black text-slate-900 mb-2">{{ result.score }}</h2>
      
      <p class="text-sm text-slate-500 mb-6 leading-relaxed">
        {{ result.feedback }}
      </p>
      
      <button 
        @click="$emit('next')" 
        class="w-full py-4 bg-slate-900 text-white rounded-2xl font-bold hover:bg-slate-800 active:scale-95 transition-all"
      >
        Next Hand
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

// 親から 'result' という名前で受け取る
const props = defineProps({
  result: {
    type: Object,
    required: true
  }
});

defineEmits(['next']);

const statusClass = computed(() => {
  if (!props.result) return '';
  if (props.result.score === 100) return 'bg-green-100 text-green-700';
  if (props.result.score > 0) return 'bg-yellow-100 text-yellow-700';
  return 'bg-red-100 text-red-700';
});
</script>