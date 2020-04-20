const delay = ms => new Promise(res => setTimeout(res, ms));

async function geoSearch(text, params = []) {
  const res = await fetch(`https://geosearch.planninglabs.nyc/v1/autocomplete?text=${text}&size=10&${params.join('&')}`)
  const data = await res.json()
  await delay(2000);
  return data.features
}

export default geoSearch