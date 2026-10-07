<script>
    import { createEventDispatcher } from 'svelte'

    const dispatch = createEventDispatcher()

    import L from '../libs/leaflet'
    import { onMount } from 'svelte'

    let container
    let map
    let layer

    $: {
        if (layer) {
            dispatch('message', layer.getBounds() );
        }
    }

    onMount(() => {
        const settings = {
            maxZoom: 20,
            minZoom: 9,
            bounds: L.latLngBounds([40.496133, -74.2555913], [40.9155327, -73.70000906]),
            apiKey: '4fe736cc-12f1-41e9-9ab9-b56366110e40'
        }
        map = L.map(container, { ...settings }).setView([40.694457, -73.93045], 10)

        //draw layer
        const editableLayers = new L.FeatureGroup().addTo(map)

        L.control.layers({
            'osm': L.tileLayer(
                    'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.{ext}?api_key={apiKey}',
                    {
                        ...settings,
                        ext: 'png',
                        attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    }
            ).addTo(map),
        }, {}, { position: 'topleft', collapsed: false }).addTo(map)

        //controls
        map.addControl(new L.Control.Draw({
            draw: {
                polyline: false,
                circlemarker: false,
                circle: false,
                polygon: false,
                marker: false,
                rectangle: { showArea: false }
            },
            edit: {
                featureGroup: editableLayers
            }
        }))

        map.on('draw:created', e => {
            if (layer) {
                //remove previous layer
                editableLayers.removeLayer(layer)
            }
            layer = e.layer
            editableLayers.addLayer(layer)
        })

    })
</script>

<div id="map" bind:this={container}></div>

<style>
    #map {
        margin-top: 0.5rem;
        width: 80%;
        height: 300px;
    }

</style>