$('form').submit(function(e){ e.preventDefault(); });

var arr, element;

const filterCriteria = (function() {
	var currentFocus = -1;

	$(document).ready(function() {
		$(window).keydown(function(event){
			if(event.keyCode == 13) {
				event.preventDefault();
				return false;
			}
		});
	});

	const inputCallback = function(e) {
		var itemsList, item, val = this.value;
		/*close any already open lists of autocompleted values*/
		closeAllLists();
		if(val.length < 3) return;
		if (!val) { return false; }
		/*create a DIV element that will contain the items (values):*/
		itemsList = document.createElement("DIV");
		itemsList.setAttribute("id", this.id + "autocomplete-list");
		itemsList.setAttribute("class", "autocomplete-items");
		/*append the DIV element as a child of the autocomplete container:*/
		this.parentNode.appendChild(itemsList);

		for (i = 0; i < arr.length; i++) {
			/*check if the item starts with the same letters as the text field value:*/
			if (arr[i].name.substr(0, val.length).toUpperCase() == val.toUpperCase()) {
				/*create a DIV element for each matching element:*/
				item = document.createElement("DIV");
				/*make the matching letters bold:*/
				item.innerHTML = "<strong>" + arr[i].name.substr(0, val.length) + "</strong>";
				item.innerHTML += arr[i].name.substr(val.length);

				/*insert a input field that will hold the current array item's value:*/
				item.innerHTML += "<input type='hidden' value='" + arr[i].name + "'>";
				/*execute a function when someone clicks on the item value (DIV element):*/
					item.addEventListener("click", function(e) {
						/*insert the value for the autocomplete text field:*/
						element.value = this.getElementsByTagName("input")[0].value;
						/*close the list of autocompleted values,
						(or any other open lists of autocompleted values:*/
						closeAllLists();
					});
				itemsList.appendChild(item);
			}
		}
	}

	const keyupCallback = function(e) {
		var x = document.getElementById(this.id + "autocomplete-list");
		if (x) x = x.getElementsByTagName("div");
		if (e.keyCode == 40) {
			/*If the arrow DOWN key is pressed, increase the currentFocus variable:*/
			currentFocus++;
		/*and and make the current item more visible:*/
		addActive(x);
		} else if (e.keyCode == 38) { //up
		/*If the arrow UP key is pressed,
		decrease the currentFocus variable:*/
		currentFocus--;
		/*and and make the current item more visible:*/
		addActive(x);
		} else if (e.keyCode == 13) {
			e.preventDefault()
			/*If the ENTER key is pressed, prevent the form from being submitted,*/
		if (currentFocus > -1) {
			/*and simulate a click on the "active" item:*/
			if (x) x[currentFocus].click();
		}
		}

		function addActive(x) {
			/*a function to classify an item as "active":*/
			if (!x) return false;
			/*start by removing the "active" class on all items:*/
			removeActive(x);
			if (currentFocus >= x.length) currentFocus = 0;
			if (currentFocus < 0) currentFocus = (x.length - 1);
			/*add class "autocomplete-active":*/
			x[currentFocus].classList.add("autocomplete-active");
		}
		
		function removeActive(x) {
			/*a function to remove the "active" class from all autocomplete items:*/
			for (var i = 0; i < x.length; i++) {
			x[i].classList.remove("autocomplete-active");
			}
		}
	}

	function filterDOM(array, inputElement) {
		arr = array;
		element = inputElement;
		/*execute a function when someone writes in the text field:*/
		inputElement.removeEventListener("input", inputCallback, false);
		inputElement.addEventListener("input", inputCallback, false);
		/*execute a function presses a key on the keyboard:*/
		inputElement.removeEventListener("keyup", keyupCallback, false);
		inputElement.addEventListener("keyup", keyupCallback, false);

		/*execute a function when someone clicks in the document:*/
		document.addEventListener("click", function (e) {
			closeAllLists();
		});
	}

	function closeAllLists() {
		/*close all autocomplete lists in the document, except the one passed as an argument:*/
		var x = document.getElementsByClassName("autocomplete-items");
		for (var i = 0; i < x.length; i++) {
			x[i].parentNode.removeChild(x[i]);
		}
	}

	return filterDOM
})()

function sendData(domId, array){
	elem = document.getElementById(domId)
	data = array.filter(e => e.name == elem.value)
	if(!data.length && elem.value != "") return false;
	elem.value = data && data[0] ? data[0].alpha2Code : ""
	document.getElementById("country-form").submit()
}