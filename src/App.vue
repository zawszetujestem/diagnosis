<template>
    <div> <h1>{{ title }}</h1>
    <button @click="greet">Add greet</button>
    </div>
</template>

<script>

export default {
    data() {
        return {
            title: "Hello Vue"
        }
    },
    methods: {
        greet() {
            alert('Hello!!!')
        },
    },
}
</script>

<style>

</style>
