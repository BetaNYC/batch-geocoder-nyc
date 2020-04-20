import App from './App.svelte'

//polyfill
import 'whatwg-fetch'

const app = new App({
  target: document.body
})

export default app
