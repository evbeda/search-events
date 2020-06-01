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
		document.getElementById("filter-form").submit();
		document.getElementById("filter-form").style.visibility = "hidden";
		document.getElementById("table-events").style.display = "none";
		document.getElementById("divCountry").style.visibility = "hidden"
		document.getElementById("spin").style.display = "block";

	}

	return {
		formatFormData: formatFormData,
	}
})()
