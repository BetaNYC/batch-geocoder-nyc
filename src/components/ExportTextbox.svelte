<script>
    import Papa from 'papaparse'
    import { results } from '../stores'

    let value = ''
    let hiddenLink

    $:  exportData = $results.map(({ features, fields, status, selectedFeatureId }) => {
        //generate export to include original fields, _location, _latitude, _longitude, _status
        const feature = features.find(feature => feature.properties.id === selectedFeatureId)

        if (feature) {
            const d_feature = Object.assign({}, feature) // deep copy
            return {
                ...fields,
                _location: d_feature.properties.label,
                _latitude: d_feature.geometry.coordinates[1],
                _longitude: d_feature.geometry.coordinates[0],
                _status: status
            }
        }
        return {
            ...fields,
            _location: '?',
            _latitude: '?',
            _longitude: '?',
            _status: status
        }
    })

    $: updateTextBox(exportData)

    let timer
    const updateTextBox = exportData => {
        clearTimeout(timer)
        timer = setTimeout(() => {
            value = Papa.unparse(exportData, { delimiter: '\t' })
        }, 500)
    }

    function downloadCSV() {
        if (hiddenLink) {
            const csvExport = Papa.unparse(exportData, { delimiter: ',' })
            const url = 'data:text/plain;charset=utf-8,' + window.encodeURIComponent(csvExport)
            hiddenLink.setAttribute('download', 'export.csv')
            hiddenLink.setAttribute('href', url)
            hiddenLink.click()
        }
    }
</script>

<div class="container">
    <h5 class="is-size-5">5. Copy and paste coordinates to spreadsheet, or <a on:click={downloadCSV}>download a csv</a>.
    </h5>
    <p class="is-size-7 has-text-grey-dark">Order of columns: [Original Columns], _location, _latitude, _longitude,
        _status.</p>
    <div class="field top-margin">
        <div class="control">
            <textarea class="textarea" bind:value></textarea>
        </div>
    </div>
    <a bind:this={hiddenLink} class="hidden"></a>
</div>

<style>
    textarea {
        color: #5e5e5e;
        width: 100%;
        height: 150px;
        line-height: 1.1rem;
    }

    .hidden {
        display: none;
    }
</style>