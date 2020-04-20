<script>
    export let color = '#fff'
    export let size = 0.8

    $: style = `background-color: ${color}; width: ${size}em; height: ${size}em;`
</script>

<span {style}></span>

<style>
    span{
        display: inline-block;
        border-radius: 0.2em;
        margin-right: 0.2em;
        border: 1px solid #FFF;
    }
</style>