const StateManager = (function() {

	let countries, cities;

	function filterCountry(countries, inputElement) {
		setCountries(countries);
		ListManager.setElement(inputElement);
	}
	
	function filterCity(inputElement) {
		const dataCountries = countries.filter(c => c.name == document.getElementById('country').value)
		if (dataCountries && dataCountries.length){
			setCities(dataCountries[0].cities);
		}
		ListManager.setElement(inputElement);
	}

	function setCountries(value) {
        countries = value;
    }
    
    function setCities(value) {
        cities = value;
	}
	
	function getCountries() {
        return countries;
    }
    
    function getCities() {
        return cities;
	}

	return {
		filterCountry,
		filterCity,
		setCountries,
		setCities,
		getCities,
		getCountries,
	}
})()
