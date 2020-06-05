
const filterCriteria = (function() {
	
	function filterCountry(countries, inputElement) {
		ListManager.setCountries(countries);
		ListManager.setElement(inputElement);
	}
	
	function filterCity(cities, inputElement) {
		ListManager.setCities(cities);
		ListManager.setElement(inputElement);
	}

	return {
		filterCountry: filterCountry,
		filterCity: filterCity
	}
})()
