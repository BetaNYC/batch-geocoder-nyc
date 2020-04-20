<script>
    import { addressColumn, input } from '../stores'

    let selectedColumn = null
    let columnOptions = []


    $: updateColumnns($input)

    function updateColumnns(input){
        //reset selectedColumn and columnOptions when input is updated
        if ($input.length > 0 && Object.keys($input[0]).length > 0) {
            const newColumnOptions = Object.keys($input[0])
            columnOptions = newColumnOptions
            selectedColumn = newColumnOptions[0]
        } else {
            columnOptions = []
            selectedColumn = null
        }
    }

    $: addressColumn.set(selectedColumn)

</script>

<div class="container">
    <h5 class="is-size-5">3. Select a column</h5>
    <p class="is-size-7 has-text-grey-dark">Select the column that contains the address identifiers.</p>
    <div class="field">
        <div class="control">
            <div class="select is-small top-margin">
                <select bind:value={selectedColumn}>
                    {#each columnOptions as column}
                        <option value={column}>{column}</option>
                    {/each}
                </select>
            </div>
        </div>
    </div>
</div>