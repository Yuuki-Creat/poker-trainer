<template>
    <div class="flex bg-slate-700 rounded-lg p-1 space-x-1 text-xs md:text-sm">
        <button
            v-for="s in ['TAG', 'GTO', 'LAG']" :key="s"
            @click="$emit('update.modelValue', s)"
            :class="modelValue === s ? 'bg-blue-600 text-white' : 'text-slate-300 hover:bg-slate-600'"
            class="px-3 py-1 rounded transition-colors font-bold"
        >
            {{ s }}
        </button>
    </div>
</template>

<script setup>
defineProps = (['modelValue']);
defineEmits = (['update.modelValue']);
</script>