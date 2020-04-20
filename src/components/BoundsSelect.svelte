<script>
    import BoundsCustom from './BoundsCustom.svelte'
    import { parameters } from '../stores'

    function getBoroParameters(boroNum) {
        return () => [`boundary.gid=whosonfirst:borough:${boroNum}`]
    }

    let bounds = [
        {
            id: 'citywide',
            name: 'Citywide',
            parameters: () => []
        },
        {
            id: 'bronx',
            name: 'The Bronx',
            parameters: getBoroParameters(2)
        },
        {
            id: 'brooklyn',
            name: 'Brooklyn',
            parameters: getBoroParameters(3)
        },
        {
            id: 'manhattan',
            name: 'Manhattan',
            parameters: getBoroParameters(1)
        },
        {
            id: 'staten_island',
            name: 'Staten Island',
            parameters: getBoroParameters(5)

        },
        {
            id: 'queens',
            name: 'Queens',
            parameters: getBoroParameters(4)
        },
        {
            id: 'custom',
            name: 'Custom',
            parameters: () => []
        }
    ]

    let selectedBound = bounds[0]

    //update parameters state
    $: parameters.set(selectedBound.parameters())

    function _updateCustomBounds(event) {
        if (selectedBound.id === 'custom') {
            selectedBound.parameters = () => {
                const { _southWest, _northEast } = event.detail
                return [
                    `boundary.rect.min_lat=${_southWest.lat}`, `boundary.rect.min_lon=${_southWest.lng}`,
                    `boundary.rect.max_lat=${_northEast.lat}`, `boundary.rect.max_lon=${_northEast.lng}`
                ]
            }
            bounds = bounds //update references
        }
    }


</script>


<div class="container">
    <h5 class="is-size-5">1. Indicate bound</h5>
    <p class="is-size-7 has-text-grey-dark">Search for locations within a borough or a custom boundary. This could
        improve your results.</p>
    <div class="field">
        <div class="control">
            <div class="select is-small top-margin">
                <select bind:value={selectedBound}>
                    {#each bounds as bound (bound.id)}
                        <option value={bound}>{bound.name}</option>
                    {/each}
                </select>
            </div>
        </div>
    </div>
    {#if selectedBound.id === 'custom'}
        <BoundsCustom on:message={_updateCustomBounds}/>
    {/if}
</div>