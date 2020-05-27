const formManager = (function() {
	
	$('form').submit(function(e){ e.preventDefault(); });
	function formatFormData(domId, array){
		var selected = [];
		for (var option of document.getElementById('feature').options) {
		  if (option.selected) selected.push(option.value);
		}
		document.getElementById('textFeature').value = selected.join('-');
		elem = document.getElementById(domId);
		data = array.filter(e => e.name == elem.value);
		if(!data.length && elem.value != "") return false;
		elem.value = data && data[0] ? data[0].name : "";
		document.getElementById("country-form").submit();
		document.getElementById("table-events").style.display = "none";
		document.getElementById("spin").style.display = "block";
	}

	function logout() {
		document.getElementById("logout-form").submit()
	}

	return {
		formatFormData: formatFormData,
		logout: logout
	}
})()
