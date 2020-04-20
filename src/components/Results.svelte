<script>
    import { results, parameters, resultsDOM, openedResultIndex } from '../stores'
    import ResultsMap from './results/ResultsMap.svelte'
    import StatusBlock from './results/StatusBlock.svelte'
    import ResultItem from './results/ResultItem.svelte'

    let status = [
        {
            name: 'Pending', color: '#9e9e9e', checked: true, count: 0
        },
        {
            name: 'Checked', color: '#8bc34a', checked: true, count: 0
        },
        {
            name: 'Unchecked', color: '#ff9800', checked: true, count: 0
        },
        {
            name: 'Failed', color: '#f44336', checked: true, count: 0
        }
    ]

    $: {
        //get status counts
        const counts = $results.reduce((counts, { status }) => {
            counts[status] += 1
            return counts
        }, { 'Pending': 0, 'Checked': 0, 'Unchecked': 0, 'Failed': 0 })

        status.forEach(i => i.count = counts[i.name])
        status = status
    }

    function updateQueueItem(event) {
        const { result, index } = event.detail
        results.updateItem(result, index)
    }

    $: filteredResults = $results.filter(result => {
        //filterResults based on checked statues and if currently selected
        const statusFilter = status.filter(i => i.checked).map(i => i.name).includes(result.status)
        const selectedFilter = result.index !== null && result.index === $openedResultIndex
        return statusFilter || selectedFilter
    })


</script>

<div class="container">
    <h5 class="is-size-5">4. Check the results</h5>
    <p class="is-size-6 has-text-grey-dark">Click on an address below or on the map to view or edit. If
        there were multiple locations for address found, the first hit will be selected.</p>
    <p class="is-size-7 has-text-grey"> Check and Unchecked are optional labels you may use to keep track of
        validated entries.</p>
    <div class="columns">
        <div class="column is-half">
            <div class="status">
                {#each status as item, name}
                    <label class="checkbox">
                        <input type="checkbox" bind:checked={item.checked}>
                        <StatusBlock color={item.color}/>
                        {item.name} {item.count}
                    </label>
                {/each}
                <div class="queue" bind:this={$resultsDOM}>
                    {#each filteredResults as result (result.index)}
                        <ResultItem {result} on:message={updateQueueItem}/>
                    {/each}
                </div>
            </div>
        </div>
        <div class="column is-half map">
            <ResultsMap/>
        </div>
    </div>
</div>


<style>
    .checkbox {
        padding-right: 0.6em;
        line-height: 1.6;
        vertical-align: middle;
        cursor: pointer;
        font-weight: 400;
    }

    .queue {
        margin-top: 1rem;
        max-height: 400px;
        overflow-y: auto;
    }

    .map {
        min-width: 400px;
    }

    .material-icons {
        font-size: 0.8rem;
    }
</style>