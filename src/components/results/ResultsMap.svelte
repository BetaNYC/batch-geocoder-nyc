<script>
    import L from '../../libs/leaflet'
    import { onMount } from 'svelte'
    import { results, openedResultIndex, mapStore } from '../../stores'

    let container
    let map
    let layer
    let selectedPointLayer

    onMount(() => {
        const settings = {
            maxZoom: 20,
            minZoom: 9,
            bounds: L.latLngBounds([40.496133, -74.2555913], [40.9155327, -73.70000906])
        }
        map = L.map(container, { ...settings }).setView([40.694457, -73.93045], 10)

        L.control.layers({
            'osm': L.tileLayer(
                    'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png',
                    {
                        ...settings,
                        attribution: 'Carto | &copy; <a href="http://osm.org/copyright">OSM</a> contributors'
                    }
            ).addTo(map),
            'google satellite': L.tileLayer('http://www.google.com/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
                ...settings,
                attribution: '&copy; Google'
            }),
            'google road': L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
                ...settings,
                attribution: '&copy; Google'
            })
        }, {}, { position: 'topright', collapsed: true }).addTo(map)

        mapStore.set(map)
    })

    $: {
        if (map) {
            if (layer) {
                map.removeLayer(layer)
            }

            function createMarker(feature, latlng) {
                const style = `
                background-color:${feature.properties.color};
                border-radius: 0.2em;
                margin-right: 0.2em;
                border: 1px solid #FFF;
                height: inherit;
                width: inherit;
                display: inherit;
              `

                const icon = L.divIcon({
                    className: 'leaflet-icon',
                    html: `<span style='${style}'></span>`,
                    iconSize: [10, 10],
                    iconAnchor: [5, 5]
                })
                return L.marker(latlng, { icon })
            }


            const geojsonFeature = $results.filter(result => result.features.length).map(result => {
                //select the selectedItem via selectedItemId, otherwise select the first item
                let feature = result.features.find(feature => feature.properties.id === result.selectedFeatureId)
                if (!feature) feature = result.features[0]
                feature.properties.color = result.color
                feature.properties.parentId = result.index
                return feature
            })

            layer = L.geoJSON(geojsonFeature, {
                pointToLayer: createMarker,
                onEachFeature: (feature, layer) => {
                    if (feature.properties && feature.properties.label) {
                        layer.bindPopup(feature.properties.label, {
                            closeButton: false,
                            autoPan: false,
                            offset: L.point(-5, 0)
                        })
                        layer.on('mouseover', () => layer.openPopup())
                        layer.on('mouseout', () => layer.closePopup())
                        layer.on('click', () => openedResultIndex.set(feature.properties.parentId))
                    }
                }
            }).addTo(map)

        }
    }

    $: {
        //have a point the map for the opened result improve visibility
        if (selectedPointLayer) {
            map.removeLayer(selectedPointLayer)
            selectedPointLayer = null
        }
        if ($results.length && $openedResultIndex) {
            const result = $results.find(result => result.index === $openedResultIndex)
            const feature = result.features.length ? result.features.find(feature => feature.properties.id === result.selectedFeatureId) : null
            if (result && feature) {
                const coords = feature.geometry.coordinates.slice().reverse()
                selectedPointLayer = L.marker(coords).addTo(map)
            }
        }

    }

    function zoomToExtent() {
        map.fitBounds(layer.getBounds())
    }

    function clearAll() {
        results.reset([])
    }


</script>

<div class="top">
    <button class="button is-small" on:click={zoomToExtent}>Fit map</button>
    <button class="button is-small is-danger" on:click={clearAll}>Clear all</button>
</div>
<div id="map" bind:this={container}></div>

<style>
    .top {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    #map {
        margin-top: 0.5rem;
        min-width: inherit;
        height: 400px;
    }

</style>