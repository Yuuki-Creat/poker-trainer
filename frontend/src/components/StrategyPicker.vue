<template>
  <div class="flex bg-slate-700 rounded-lg p-1 space-x-1 text-xs md:text-sm shadow-inner">
    <button
      v-for="s in ['TAG', 'GTO', 'LAG']" 
      :key="s"
      @click="$emit('update:modelValue', s)" 
      :class="modelValue === s 
        ? 'bg-blue-600 text-white' 
        : 'text-slate-300 hover:bg-slate-600'"
      class="px-3 py-1 rounded transition-all font-bold"
    >
      {{ s }}
    </button>
  </div>
</template>

<script setup>
// Props の型定義を明示的に行う（推奨）
defineProps({
  modelValue: {
    type: String,
    default: 'TAG'
  }
});

// Emit の定義
defineEmits(['update:modelValue']);
</script>