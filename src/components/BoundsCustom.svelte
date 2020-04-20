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
            bounds: L.latLngBounds([40.496133, -74.2555913], [40.9155327, -73.70000906])
        }
        map = L.map(container, { ...settings }).setView([40.694457, -73.93045], 10)

        //draw layer
        const editableLayers = new L.FeatureGroup().addTo(map)

        L.control.layers({
            'osm': L.tileLayer(
                    'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png',
                    {
                        ...settings,
                        attribution: 'Carto | &copy; <a href="http://osm.org/copyright">OSM</a> contributors'
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