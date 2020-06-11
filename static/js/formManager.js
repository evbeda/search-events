const formManager = (function() {

	const domIds = ["country", "city"];

	$('form').submit(function(e){ e.preventDefault(); });

	function formatFormData(formId){
		if(formId === 'features-form'){
			fillFeatureUrlValue();
		}
		validateCountryAndCity();
		document.getElementById(formId).submit();
		showSpinner(formId);
	}

	function fillFeatureUrlValue(){
		var selected = [];
		for (var option of document.getElementById('feature').options) {
			if (option.selected) selected.push(option.value);
		}
		document.getElementById('textFeature').value = selected.join('-');
	}

	function validateCountryAndCity(){
		const countries = StateManager.getCountries();
		const selectedCountry = countries.filter(e => e.name == document.getElementById("country").value);
		const dataArray = [countries];
		if (selectedCountry && selectedCountry.length){
			StateManager.setCities(selectedCountry[0].cities);
			const cities = StateManager.getCities();
			dataArray.push(cities);
		}

		for(let i=0; i<dataArray.length; i++){
			const domId = domIds[i];
			const elem = document.getElementById(domId);
			const data = dataArray[i].filter(e => e.name == elem.value);
			if(!data.length && elem.value != "") return false;
			elem.value = data && data[0] ? data[0].name : "";
		}
	}
	
	function showSpinner(formId){
		document.getElementById(formId).style.display = "none";
		document.getElementById("table-events").style.display = "none";
		document.getElementById("accordion").style.display = "none";
		document.getElementById("spin").style.display = "block";
	}

	return {
		formatFormData,
	}
})()
