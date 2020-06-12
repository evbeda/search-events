const FormManager = (function() {

	const domIds = ["country", "city"];
	const FILTER_IDS = ["country", "city", "card"];
	const ERROR_MESSAGES = {
		"country": "Make sure you typed a valid country name, including capital letters.",
		"city": "Make sure you typed a valid state name, including capital letters.",
		"card": "This field must either be empty or have exactly 4 digits."
	}

	function formatFormData() {
		try {
			fillFeatureUrlValue();
		} catch(e) {}
		validateFilters();
		for(let i = 0; i < FILTER_IDS.length; i++) {
			try {
				const domId = FILTER_IDS[i]
				const domElement = document.getElementById(domId);
				if(!domElement.checkValidity()) {
					domElement.setCustomValidity(ERROR_MESSAGES[domId])	
					return false;
				}
			} catch(e) {}
		}
		document.getElementById('submit-form').submit();
		SpinnerManager.showSpinner();
	}

	function fillFeatureUrlValue(){
		var selected = [];
		for (var option of document.getElementById('feature').options) {
			if (option.selected) selected.push(option.value);
		}
		document.getElementById('textFeature').value = selected.join('-');
	}

	function validateFilters() {
		try {
			if(!validateLastFourDigits()) return false;
			
			const countries = StateManager.getCountries();
			const selectedCountry = countries.filter(e => e.name == document.getElementById("country").value);
			if(!validateCountry()) return false;
	
			const dataArray = [countries];
			if (selectedCountry && selectedCountry.length) {
				StateManager.setCities(selectedCountry[0].cities);
				const cities = StateManager.getCities();
				const selectedCity = cities.filter(e => e.name == document.getElementById("city").value);
				const cityValid = document.getElementById("city").value === "" || (selectedCity && selectedCity.length);
				validateField("city", cityValid);
				dataArray.push(cities);
			}
	
			for(let i=0; i<dataArray.length; i++){
				const domId = domIds[i];
				const elem = document.getElementById(domId);
				const data = dataArray[i].filter(e => e.name == elem.value);
				if(!data.length && elem.value != "") return false;
				elem.value = data && data[0] ? data[0].name : "";
			}
	
			return true;
		} catch(e) {}
	}

	function validateLastFourDigits() {
		const lastFour = document.getElementById("card").value
		const cardValid = lastFour.length === 0 ||lastFour.length === 4;
		validateField("card", cardValid);
		return cardValid;
	}

	function validateCountry() {
		const countries = StateManager.getCountries();
		const selectedCountry = countries.filter(e => e.name == document.getElementById("country").value);
		const countryValid = document.getElementById("country").value === "" || (selectedCountry && selectedCountry.length);
		validateField("country", countryValid);
		return countryValid;
	}

	function validateField(domId, condition) {
		let message = condition ? "" : ERROR_MESSAGES[domId];
		document.getElementById(domId).setCustomValidity(message);
	}

	function validateNumbers(event, domId) {
		document.getElementById(domId).setCustomValidity("");
        if(event.metaKey && event.keyCode == KEY_CODES.R) return true; //reload page
        if(event.metaKey && event.keyCode == KEY_CODES.C) return true; //copy
        if(((event.keyCode < KEY_CODES.ZERO) || (event.keyCode > KEY_CODES.NINE))&& event.keyCode != KEY_CODES.DELETE && ((event.keyCode < KEY_CODES.LEFT) || (event.keyCode > KEY_CODES.DOWN))){
            event.preventDefault();
        }
	}

	return {
		formatFormData,
		validateField,
		validateNumbers
	}
})()
