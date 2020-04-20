<script>
    import { input, inputText, parameters, addressColumn, results } from '../stores'
    import geoSearch from '../utils/geoSearch'

    function geocodeInput() {
        //add input to results
        const newInput = $input.map(fields => ({
            features: [],
            selectedFeatureId: null,
            address: fields[$addressColumn],
            fields,
            pending: true,
            checked: null,
            status: 'Pending',
            color: '#9e9e9e',
            error: null
        }))
        results.add(newInput)

        //clear input
        inputText.set('')

        // geocode only pending items using addressColumn and parameters
        $results.filter(result => result.pending).map(result => {
            return geoSearch(result.address, $parameters).then(features => {
                result.features = features
                result.selectedFeatureId = features.length ? features[0].properties.id : null
                result.pending = false
                results.updateItem(result, result.index)
            }).catch(error => {
                //todo - show errors
                result.features = []
                result.pending = false
                result.error = error.message
                results.updateItem(result, result.index)
            })
        })
    }

</script>

{#if $addressColumn !== null}
    <div class="container">
        <button class="button is-info" on:click={geocodeInput}>Add to geocoder</button>
    </div>
{/if}

<style>
    .container {
        margin-top: 0.5rem;
    }
</style>