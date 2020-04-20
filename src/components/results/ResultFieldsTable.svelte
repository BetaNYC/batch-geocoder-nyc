<script>
    export let fields = {}
</script>

<div class="fields">
    <table class="table is-narrow is-bordered">
        <thead>
        <tr>
            {#each Object.keys(fields) as col}
                <th>{col}</th>
            {/each}
        </tr>
        </thead>
        <tbody>
        <tr>
            {#each Object.values(fields) as col}
                <td>{col}</td>
            {/each}
        </tr>
        </tbody>
    </table>
</div>

<style>
    .fields {
        max-width: 100%;
        overflow-x: auto;
        margin: 0.5rem;
    }
</style>