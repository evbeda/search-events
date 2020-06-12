const ListManager = (function() {

    let countries, cities, element;
    let currentFocus = -1;

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
        for (let i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }

    function closeAllLists() {
        /*close all autocomplete lists in the document, except the one passed as an argument:*/
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            x[i].parentNode.removeChild(x[i]);
        }
    }

    function incrementCurrentFocus() {
        currentFocus++;
    }

    function decrementCurrentFocus() {
        currentFocus--;
    }

    function getCurrentFocus() {
        return currentFocus;
    }

    function getCountries() {
        return countries;
    }
    
    function getCities(country) {
        return cities.filter(e => e.country == country);
    }

    function getElement() {
        return element;
    }

    function setCountries(value) {
        countries = value;
    }
    
    function setCities(value) {
        cities = value;
    }

    function setElement(value) {
        element = value;
    }

    return {
        addActive: addActive,
        removeActive: removeActive,
        closeAllLists: closeAllLists,
        incrementCurrentFocus: incrementCurrentFocus,
        decrementCurrentFocus: decrementCurrentFocus,
        getCurrentFocus: getCurrentFocus,
        getCountries: getCountries,
        getCities: getCities,
        setCountries: setCountries,
        setCities: setCities,
        getElement: getElement,
        setElement: setElement
    }
})()