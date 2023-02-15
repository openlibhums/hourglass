const dropdownOptions = {
	constrainWidth: false,
	coverTrigger: false,
}

document.addEventListener('DOMContentLoaded', event => {
  const elems = document.querySelectorAll('.dropdown-trigger');
  M.Dropdown.init(elems, dropdownOptions);
});
