<script>
    import { parameters, openedResultIndex, mapStore } from '../../stores'
    import { createEventDispatcher } from 'svelte'
    import StatusBlock from './StatusBlock.svelte'
    import ResultFieldsTable from './ResultFieldsTable.svelte'
    import geoSearch from '../../utils/geoSearch'

    const dispatch = createEventDispatcher()

    export let result = {
        address: '1 Test Street, Long Island Sound',
        selectedFeatureId: null,
        features: [],
        fields: [],
        status: 'Pending',
        color: '#9e9e9e',
        index: 0,
        pending: false
    }

    let value = ''

    function toggleOpened(){
        $openedResultIndex !== result.index ? openedResultIndex.set(result.index) : openedResultIndex.set(null)
    }

    function geocode(value) {
        geoSearch(value, $parameters).then(features => {
            result = {
                ...result,
                features,
                selectedFeatureId: features.length ? features[0].properties.id : null, //select first item by default
                checked: null
            }
            result = result
            update()
        })
    }

    let timer

    function debounceGeocode() {
        clearTimeout(timer)
        timer = setTimeout(() => {
            geocode(value)
        }, 250)
    }

    function toggleChecked(bool) {
        if (result.selectedFeatureId && bool == true) {
            result.checked = true
        } else if (bool == false) {
            result.checked = false
        } else {
            result.checked = null
        }
        result = result
        update()
    }

    function update() {
        dispatch('message', {
            result, index: result.index
        })
    }

    function updateSelectedFeatureId(e) {
        result.selectedFeatureId = e.target.value
        result.checked = null
        result = result
        update()
    }

    function zoomToSelectedFeature(){
      if(result.selectedFeatureId){
        const feature = result.features.find(feature => feature.properties.id === result.selectedFeatureId)
          if(feature){
            const coords = feature.geometry.coordinates.slice().reverse()
            $mapStore.flyTo(coords, 19);
          }
      }
    }


</script>
<div class="result-item" bind:this={result.dom}>
    <div class="top" on:click={toggleOpened}>
        <StatusBlock color={result.color} size="0.7"/> {result.address} (Hits: {result.features.length})
    </div>
    {#if result.index === $openedResultIndex}
        <div class="body">
            <ResultFieldsTable fields={result.fields}></ResultFieldsTable>
            <div class="field body-input">
                <p class="control">
                    <input class="input" type="text" placeholder="Typing in a corrected Street, Borough" bind:value={value}
                           on:keyup={() => value.length > 0 ? debounceGeocode(): null}>
                </p>
                <button class="button" on:click={() => toggleChecked(true)}>
                    <span class="icon">
                        <i class="material-icons">check</i>
                    </span>
                </button>
                <button class="button" on:click={() => toggleChecked(false)}>
                    <span class="icon">
                        <i class="material-icons">close</i>
                    </span>
                </button>
                <button class="button" on:click={zoomToSelectedFeature}>
                    <span class="icon">
                        <i class="material-icons">zoom_out_map</i>
                    </span>
                </button>
            </div>
            <div class="control results">
                {#each result.features as feature (feature.properties.id)}
                    <label class="radio">
                        <input type="radio" name={result.index} bind:group={result.selectedFeatureId}
                               on:change={updateSelectedFeatureId}
                               value={feature.properties.id}><span class="name">{feature.properties.label}</span>
                    </label>
                {/each}
            </div>
        </div>
    {/if}
</div>

<style>
    .result-item {
        border: 1px solid #ddd;
        border-radius: 4px;
        font-weight: 200;
        font-size: 0.85em;
        color: #5b5b5b;
        line-height: 24px;
        margin-bottom: 0.5rem;
    }

    .top {
        padding: 2px 15px;
        cursor: pointer;
        color: #333333;
        background-color: #f5f5f5;
        border-bottom: 2px solid #dddddd;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    .body-input {
        margin: 0.85rem 0.5rem;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    .button {
        height: 1.8rem;
        width: 15%;
        margin-left: 0.2rem;
    }

    .control{
        flex: 1;
    }

    .material-icons {
        font-size: 1.2rem;
    }

    .results{
        display: flex;
        flex-direction: column;
    }

    .results label {
        margin-left: 0.5rem;
        margin-bottom: 0.5rem;
        font-size: 0.85rem;
    }

    label .name {
        margin-left: 0.2rem;
    }

</style>