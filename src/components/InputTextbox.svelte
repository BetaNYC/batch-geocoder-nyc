<script>
  import { onMount, onDestroy } from 'svelte'
  import { input, inputText } from '../stores'
  import Papa from 'papaparse'

  const placeholder =
    'name\taddress\nMunicipal Building\t1 Centre Street, New York, NY 10007\nEquitable Building\t120 Broadway, New York, NY 10271'
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
    const reader = new FileReader()
    reader.onload = () => {
      console.log(reader.result)
      inputText.set(reader.result)
    }
    reader.readAsBinaryString(container.files[0])
  }

  function downloadSample() {
    // Convert tab-separated placeholder to proper CSV
    const csv = placeholder
      .split('\n')
      .map(row => row.split('\t').join(','))
      .join('\n')

    const blob = new Blob([csv], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)

    const a = document.createElement('a')
    a.href = url
    a.download = 'sample.csv'
    a.click()

    URL.revokeObjectURL(url)
  }

  onMount(() => container.addEventListener('change', readFile))
  onDestroy(() => container.removeEventListener('change', readFile))

  $: {
    //when value changes update store with an array of objects
    if ($inputText !== null) {
      Papa.parse($inputText, {
        header: true,
        delimitersToGuess: [',', '\t', '|', ';'],
        complete: results => input.set(results.data)
      })
    }
  }
</script>

<div class="container">
  <h5 class="is-size-5">
    2. Copy and paste a list of locations, or upload a csv.
  </h5>
  <p class="is-size-6 has-text-grey-dark">
    When pasting or uploading files, your first column should be the headers.
    Columns should be separated by tabs or commas.
  </p>
  <div class="field top-margin">
    <div class="control">
      <input type="file" bind:this={container} accept=".csv,.tsv" />
    </div>
  </div>
  <p class="is-size-7 has-text-grey">
    For the best results include a borough or zipcode following a comma. (ie 1 E
    161 St, 10451 or 1 E 161 St, Bronx). Remove apt numbers as well. Need a
    starting point? <a href={'#'} on:click|preventDefault={downloadSample}
      >Download a sample CSV</a
    >.
  </p>
  <div class="field top-margin">
    <div class="control">
      <textarea
        {placeholder}
        class="textarea"
        value={$inputText}
        on:keyup={({ target: { value } }) => debounce(value)}
      ></textarea>
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

  textarea::placeholder {
    color: #a8a8a8;
    font-weight: 300;
  }
</style>
