
const filterCriteria = (function() {
	
	function filterCountry(countries, inputElement) {
		ListManager.setCountries(countries);
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
	
	function filterCity(cities, inputElement) {
		ListManager.setCities(cities);
		ListManager.setElement(inputElement);
		/*execute a function when someone writes in the text field:*/
		inputElement.removeEventListener("input", inputEvents.inputCallbackCity, false);
		inputElement.addEventListener("input", inputEvents.inputCallbackCity, false);
		/*execute a function presses a key on the keyboard:*/
		inputElement.removeEventListener("keyup", inputEvents.keyupCallback, false);
		inputElement.addEventListener("keyup", inputEvents.keyupCallback, false);

		/*execute a function when someone clicks in the document:*/
		document.addEventListener("click", function (e) {
			ListManager.closeAllLists();
		});
	}

	return {
		filterCountry: filterCountry,
		filterCity: filterCity
	}
})()
