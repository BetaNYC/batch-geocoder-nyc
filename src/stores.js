import { writable } from 'svelte/store'
import getStatus from './utils/getStatus'

function createResults() {
  const { subscribe, set, update } = writable([]);

  return {
    subscribe,
    add: items => update(prev => {
      const newItems = [...prev, ...items]
      // for items that don't have an index give index (unique id)
      newItems.filter(i => i.index !== 0 && !i.index).forEach(i => {
        i.index = newItems.indexOf(i)
      })
      return newItems
    }),
    updateItem: (item, index) => update(prev => {
      const { status, color } = getStatus(item)
      item.status = status
      item.color = color
      prev[index] = item
      return prev
    }),
    reset: () => set([])
  };
}
//init stores
export let parameters = writable([])
export let inputText = writable('')
export let input = writable([])
export let addressColumn = writable(null)
//map store
export let mapStore = writable(null)
//result stores
export let results = createResults()
export let openedResultIndex = writable(null)
