const Autocomplete = window.M.Autocomplete

const base = 'https://api.ror.org/organizations?'
const searchParams = new URLSearchParams()
let timeout

async function searchROR (event) {
  searchParams.set('query', event.target.value)
  const response = await fetch(base + searchParams.toString())
  const results = await response.json()
  return Object.fromEntries(
    results.items.map(
      result => [result.name, null]
    )
  )
}

class APIAutocomplete extends Autocomplete {
  _handleInputKeyupAndFocus (event) {
    window.clearTimeout(timeout)
    timeout = window.setTimeout(async () => {
      if (event.target.value.length > 2) {
        this.updateData(await searchROR(event))
      }
      super._handleInputKeyupAndFocus(event)
    }, 500)
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const elems = document.querySelectorAll('input.autocomplete')
  APIAutocomplete.init(elems, {
    minLength: 2,
    data: {}
  })
  // elems[0].addEventListener('keyup', event => searchROR(event, instances[0]))
})
