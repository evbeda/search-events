
const filterCriteria = (function() {
	
	function filterDOM(array, inputElement) {
		ListManager.setArr(array);
		ListManager.setElement(inputElement);
		/*execute a function when someone writes in the text field:*/
		inputElement.removeEventListener("input", inputEvents.inputCallback, false);
		inputElement.addEventListener("input", inputEvents.inputCallback, false);
		/*execute a function presses a key on the keyboard:*/
		inputElement.removeEventListener("keyup", inputEvents.keyupCallback, false);
		inputElement.addEventListener("keyup", inputEvents.keyupCallback, false);

		/*execute a function when someone clicks in the document:*/
		document.addEventListener("click", function (e) {
			ListManager.closeAllLists();
		});
	}

	return filterDOM
})()
