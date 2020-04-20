<script>
    import 'bulma/css/bulma.css'

    import LoadingIndicator from './components/results/LoadingIndicator.svelte'
    import SpeedSubtitle from './components/fun/SpeedSubtitle.svelte'
    import BoundsSelect from './components/BoundsSelect.svelte'
    import InputTextbox from './components/InputTextbox.svelte'
    import ColumnsSelect from './components/ColumnsSelect.svelte'
    import AddToResults from './components/AddToResults.svelte'
    import Result from './components/Results.svelte'
    import ExportTextbox from './components/ExportTextbox.svelte'
    import Footer from './components/Footer.svelte'


</script>

<main>
    <div class="has-text-centered">
        <h3 class="title is-3">Batch geocoder for nyc</h3>
        <SpeedSubtitle/>
        <div class="has-text-grey-dark">
            <p>Fueled by Planning Lab's <a href="https://labs-geosearch-docs.netlify.app/">GeoSearch</a> and Pelias.
                Inspired by
                Erik Willems' <a href="https://geocode.localfocus.nl/">Batch geocoder for journalists</a>.</p>
        </div>
    </div>

    <br>
    <BoundsSelect/>
    <br>
    <InputTextbox/>
    <br>
    <ColumnsSelect/>
    <AddToResults/>
    <br>
    <Result/>
    <br>
    <ExportTextbox/>
    <br>
    <Footer/>

    <LoadingIndicator/>
</main>

<style>
    :global(main) {
        margin: 20px auto;
        max-width: 1500px;
        color: #444;
        padding: 0 25px;
        font-family: 'Open Sans', sans-serif !important;
    }

    :global(.top-margin) {
        margin-top: 0.5rem;
    }
</style>
