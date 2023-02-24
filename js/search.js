// See https://materializecss.github.io/materialize/modals.html

const trigger = document.getElementById('search-trigger');
const modal = document.getElementById('search-modal');
const input = document.getElementById('search-input');
const close = document.getElementById('search-close');
const form = document.getElementById('search-form');
const ul = document.getElementById('result-list');
const data = ul.getAttribute('data-site-search');


const modalOptions = {
	opacity: .3,
	inDuration: 100,
	outDuration: 100,
	onOpenEnd: event => input.focus(),
	onCloseEnd: event => trigger.focus(),
	startingTop: '10%',
	endingTop: '2%',
}


async function init() {
  const modalObj = M.Modal.init(modal, modalOptions);
  const { documents, searchIndex } = await makeSearchIndex();
  addEventListeners(documents, searchIndex, modalObj);
}


function addEventListeners(documents, searchIndex, modalObj) {

  // User presses Enter in form
  form.addEventListener("submit", event => event.preventDefault());

  // User types something
  input.addEventListener("keyup", event => {
    debounce(handleKeyup(event, documents, searchIndex))
  });

  // User clicks the X in the search bar
  close.addEventListener("click", event => modalObj.close());

}


async function makeSearchIndex() {
	const documents = await JSON.parse(data);
	const searchIndex = lunr(function () {
		this.ref('url');
		this.field('name');
		this.field('people');
		this.field('text');
		this.field('tags');
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


function handleKeyup(event, documents, searchIndex) {

	// Only 1 letter has been typed in so far
	if (input.value.length < 2) {
		ul.innerHTML = '';
		return;
	}

	// Otherwise
	updateResultsList(documents, searchIndex);
}


async function updateResultsList(documents, searchIndex) {
	ul.innerHTML = '';
	const searchResults = await searchIndex.search(input.value);
	for (let result of searchResults) {
		let doc = documents[result.ref];
		let mergedPositions = getPositionsByField(result);
		let li = makeResultListItem(doc, result.ref, mergedPositions);
		ul.appendChild(li);
	}

	if (ul.children.length == 0) {
		ul.innerHTML = '<li class="collection-item"><p>No results</p></li>';
	}
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
	let li = document.createElement('li');
	li.className = 'collection-item';

	let a = document.createElement('a');
	a.href = ref;
	let h5 = document.createElement('h5');
	h5.innerHTML = highlightFieldText(doc, 'name', positions);
	a.appendChild(h5);
	li.appendChild(a);

	if ('text' in doc) {
		let people = document.createElement('p');
		people.innerHTML = highlightFieldText(doc, 'people', positions);
		people.className = 'black-text byline';
		li.appendChild(people);
	}
	if ('people' in doc) {
		let p = document.createElement('p');
		p.innerHTML = highlightFieldText(doc, 'text', positions);
		p.className = 'black-text';
		li.appendChild(p);
	}

	if ('tags' in doc) {
		let tags = document.createElement('span');
		tags.innerHTML = highlightFieldText(doc, 'tags', positions);
		tags.className = 'black-text';
		li.appendChild(tags);
	}

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


document.addEventListener('DOMContentLoaded', event => init());
