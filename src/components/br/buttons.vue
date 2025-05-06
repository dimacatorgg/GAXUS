<script setup>
    const porps = defineProps({
        ime:String,
        boja:String,
        slika:String
    })
</script>
<template>
    <button>
        <span class="slika">
            {{ porps.slika }}
        </span>
        {{ porps.ime }}</button>
</template>