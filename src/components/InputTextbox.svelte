<script>
    import { onMount, onDestroy } from 'svelte'
    import { input, inputText } from '../stores'
    import Papa from 'papaparse'

    let container
    let timer

    const debounce = v => {
        clearTimeout(timer)
        timer = setTimeout(() => {
            inputText.set(v)
        }, 500)
    }

    function readFile() {
        //update value when file uploaded
        //todo - catch error
        const reader = new FileReader()

        reader.onload = () => {
            inputText.set(reader.result)
        }
        reader.readAsBinaryString(container.files[0])
    }

    onMount(() => container.addEventListener('change', readFile))

    onDestroy(() => container.removeEventListener('change', readFile))


    $: {
        //when value changes update store with an array of objects
        if ($inputText !== null) {
            Papa.parse($inputText, {
                header: true,
                complete: results => input.set(results.data)
            })
        }
    }

</script>


<div class="container">
    <h5 class="is-size-5">2. Copy and paste a list of locations, or upload a csv.</h5>
    <p class="is-size-7 has-text-grey-dark">When pasting or uploading files, your first column should be the
        headers. Columns should be separated by tabs or commas.</p>
    <div class="field top-margin">
        <div class="control">
            <input type="file" bind:this="{container}" accept=".csv,.tsv">
        </div>
    </div>
    <div class="field top-margin">
        <div class="control">
            <textarea class="textarea" value={$inputText} on:keyup={({ target: { value } }) => debounce(value)}></textarea>
        </div>
    </div>
</div>

<style>
    textarea {
        color: #5e5e5e;
        width: 100%;
        height: 150px;
        line-height: 1.1rem;
    }
</style>