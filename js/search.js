async function init(searchInputId = 'search-input') {
	const searchInput = document.getElementById(searchInputId);
	const searchResultsUl = document.getElementById('search-results');
	const { documents, searchIndex } = await makeSearchIndex(searchInput, searchResultsUl);

	// User types something
	searchInput.addEventListener(
		"keyup",
		event => debounce(handleKeyup(event, documents, searchInput, searchIndex, searchResultsUl))
	);

	// User clicks the X on the search bar
	document.querySelector('.search-bar i.close').addEventListener(
    "click",
    event => closeSearch(event, searchResultsUl)
  );

	// User clicks outside of the search bar or results
	document.querySelector('.search-bar').addEventListener(
    "click",
    event => event.stopPropagation()
  );
  document.querySelector('#search').addEventListener(
    "click",
    event => event.stopPropagation()
  );
  document.querySelector('body').addEventListener(
    "click",
    event => closeSearch(event, searchResultsUl)
  );

}


async function makeSearchIndex(searchInput, searchResultsUl) {
	const documentString = searchResultsUl.getAttribute('data-site-search');
	const documents = await JSON.parse(documentString);
	const searchIndex = lunr(function () {
		this.ref('url');
		this.field('name');
		this.field('text');
		this.metadataWhitelist = ['position'];
		for (let key in documents) {
			this.add(documents[key]);
		}
	});
	return { documents, searchIndex };
}


function debounce(fn) {
// Thanks to Materialize for this function: 
// https://github.com/materializecss/materialize/blob/f71022051b7d388dc77bd84c27cf4ac0bdb35263/docs/js/search.js#L282-L293
	let timeout;
  return function () {
    let args = Array.prototype.slice.call(arguments);
    let ctx = this;
    clearTimeout(timeout);
    timeout = setTimeout(function () {
      fn.apply(ctx, args);
    }, 100);
  };
};


function handleKeyup(event, documents, searchInput, searchIndex, searchResultsUl) {

	// Only 1 or 2 letters have been typed in so far
	if (searchInput.value.length < 3) {
		searchResultsUl.innerHTML = '';
		document.querySelector('#search').setAttribute('hidden', '');
		return;
	}

  // User hit the escape key
  if (event.keyCode === 27) {
	  closeSearch(event, searchResultsUl);
    return;
	}

	// Otherwise
	updateResultsList(event, documents, searchInput, searchIndex, searchResultsUl);
}


async function updateResultsList(event, documents, searchInput, searchIndex, searchResultsUl) {
	searchResultsUl.innerHTML = '';
	const searchResults = await searchIndex.search(event.target.value);
	for (let result of searchResults) {
		let doc = documents[result.ref];
		let mergedPositions = getPositionsByField(result);
		let li = makeResultListItem(doc, result.ref, mergedPositions);
		searchResultsUl.appendChild(li);
	}

	if (searchResultsUl.children.length == 0) {
		searchResultsUl.innerHTML = '<li class="collection-item">No results</li>';
	}
	document.querySelector('#search').removeAttribute('hidden');
}


function getPositionsByField(result){
	const fieldMap = new Map();
	let metadata = result.matchData.metadata;
	for (let stem in metadata) {
		for (let field in metadata[stem]) {
			if (!fieldMap.has(field)) {
				fieldMap.set(field, []);
			}
			for (let position of metadata[stem][field].position) {
				fieldMap.get(field).push(position);
			}
		}
	}
	for (let positionArray of fieldMap.values()) {
		positionArray.sort((a, b) => {return a[0] - b[0]});
	}
	return fieldMap;
}


function makeResultListItem(doc, ref, positions) {
	let h3 = document.createElement('h3');
  h3.innerHTML = highlightFieldText(doc, 'name', positions);
	let p = document.createElement('p');
  p.innerHTML = highlightFieldText(doc, 'text', positions);
  p.className = 'black-text';
	let a = document.createElement('a');
	a.href = ref;
	a.appendChild(h3);
	let li = document.createElement('li');
  li.className = 'collection-item';
  li.appendChild(a);
  li.appendChild(p);
  return li;
}


function highlightFieldText(doc, field, positions, charLimit=200) {
	// Thanks to Aaron Taylor for lots of the logic behind this function:
	// https://github.com/kujenga/website/blob/1768cf384d54b7e7ec8c88a02dc0ec3819061fc5/assets/js/search.jsx#L41-L79
	if (!positions.size) {
		return doc[field];
	}
	let innerHTML = '';
	let current = 0;
	if (positions.has(field)) {
		let firstPosition = positions.get(field)[0][0];
		if (firstPosition > charLimit - 20) {
			innerHTML += '...';
			current = firstPosition - 20;
			charLimit += current;
		}
		for (let [from, length] of positions.get(field)) {
			if (from > charLimit) {
				innerHTML += doc[field].slice(current, charLimit) + '...';
				break;
			}
			let to = from + length;
			innerHTML += doc[field].slice(current, from);
			let highlighted = doc[field].slice(from, to);
			innerHTML += `<span class="highlight">${highlighted}</span>`;
			current = to;
		}
	}
	innerHTML += doc[field].slice(current, charLimit);
	if (doc[field].length > charLimit) {
		 innerHTML += '...';
	}
	return innerHTML;
}


function closeSearch(event, searchResultsUl) {
	searchResultsUl.innerHTML = '';
	document.querySelector('#search').setAttribute('hidden', '');
	document.querySelector('#search-input').value = '';
	document.querySelector('#search-input').blur();
}


init();
