async function init(searchInputId = 'search-input') {
	const searchInput = document.getElementById(searchInputId);
	const searchResultsUl = document.getElementById('search-results');
	const { documents, searchIndex } = await makeSearchIndex(searchInput, searchResultsUl);
	searchInput.addEventListener(
		"change",
		event => updateResultsList(event, documents, searchIndex, searchResultsUl)
	);
}


async function makeSearchIndex(searchInput, searchResultsUl) {
	const documentString = searchResultsUl.parentNode.getAttribute('data-site-search');
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


async function updateResultsList(event, documents, searchIndex, searchResultsUl) {
	const searchResults = await searchIndex.search(event.target.value)
	searchResultsUl.innerHTML = '';
	for (let result of searchResults) {
		let doc = documents[result.ref];
		let mergedPositions = getPositionsByField(result);
		let li = makeResultListItem(doc, result.ref, mergedPositions);
		searchResultsUl.appendChild(li);
	}
	searchResultsUl.parentNode.removeAttribute('hidden');
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
	let h2 = document.createElement('h2');
  h2.innerHTML = highlightFieldText(doc, 'name', positions);
	let p = document.createElement('p');
  p.innerHTML = highlightFieldText(doc, 'text', positions);
	let a = document.createElement('a');
	a.href = ref;
	a.appendChild(h2);
	a.appendChild(p);
	let li = document.createElement('li');
	li.appendChild(a);
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

init();
