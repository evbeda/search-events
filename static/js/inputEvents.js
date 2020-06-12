const inputEvents = (function() {

    const keyupCallback = function(e) {
        let x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == KEY_CODES.DOWN) {
            /*If the arrow DOWN key is pressed, increase the currentFocus variable:*/
            ListManager.incrementCurrentFocus();
            /*and and make the current item more visible:*/
            ListManager.addActive(x);
        } else if (e.keyCode == KEY_CODES.UP) { //up
            /*If the arrow UP key is pressed, decrease the currentFocus variable:*/
            ListManager.decrementCurrentFocus();
            /*and and make the current item more visible:*/
            ListManager.addActive(x);
        } else if (e.keyCode == KEY_CODES.ENTER) {
            e.preventDefault();
            /*If the ENTER key is pressed, prevent the form from being submitted,*/
            currentFocus = ListManager.getCurrentFocus();
            if (currentFocus > -1 && x) {
                x[currentFocus].click();
            }
        }
    }

    const inputCallback = function(e) {
        let itemsList, item, val = this.value;
        /*close any already open lists of autocompleted values*/
        ListManager.closeAllLists();
        if (!val) {
            document.getElementById('city').disabled = true;
        }
        
        /*create a DIV element that will contain the items (values):*/
        itemsList = document.createElement("DIV");
        itemsList.setAttribute("id", this.id + "autocomplete-list");
        itemsList.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(itemsList);
        
        countries = StateManager.getCountries();
        document.getElementById('city').disabled = countries.map(e => e.name).indexOf(val) == -1
        
        FormManager.validateField("country", true);
        for (i = 0; i < countries.length; i++) {
            /*check if the item starts with the same letters as the text field value:*/
            if ((countries[i].code.toUpperCase() == val.toUpperCase() && val.length == 2) || (countries[i].name.substr(0, val.length).toUpperCase() == val.toUpperCase() && val.length >= 3)) {
                /*create a DIV element for each matching element:*/
                item = document.createElement("DIV");
                /*make the matching letters bold:*/
                item.innerHTML = "<strong>" + countries[i].name.substr(0, val.length) + "</strong>";
                item.innerHTML += countries[i].name.substr(val.length);
    
                /*insert a input field that will hold the current array item's value:*/
                item.innerHTML += "<input type='hidden' value='" + countries[i].name + "'>";
                /*execute a function when someone clicks on the item value (DIV element):*/
                item.addEventListener("click", function(e) {
                    /*insert the value for the autocomplete text field:*/
                    element = ListManager.getElement();
                    element.value = this.getElementsByTagName("input")[0].value;
                    const code = countries.filter(e => e.name==element.value)[0].code;
                    document.getElementById('city').disabled = countries.map(e => e.name).indexOf(element.value) == -1
                    /*close the list of autocompleted values, (or any other open lists of autocompleted values:*/
                    ListManager.closeAllLists();
                });
                itemsList.appendChild(item);
            }
        }
        if (document.getElementById('city').disabled) {
            document.getElementById('city').value = '';
        }
    }

    const inputCallbackCity = function(e) {
        let itemsList, item, val = this.value;
        /*close any already open lists of autocompleted values*/
        ListManager.closeAllLists();
        
        /*create a DIV element that will contain the items (values):*/
        itemsList = document.createElement("DIV");
        itemsList.setAttribute("id", this.id + "autocomplete-list");
        itemsList.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(itemsList);
        
        countries = StateManager.getCountries()
        country = countries.filter(e => e.name == document.getElementById("country").value);
        try {
            StateManager.setCities(country[0].cities);
            cities = StateManager.getCities();
            FormManager.validateField("city", true);
            for (i = 0; i < cities.length; i++) {
                /*check if the item starts with the same letters as the text field value:*/
                if ((cities[i].code.toUpperCase() == val.toUpperCase() && val.length == 2) || (cities[i].name.substr(0, val.length).toUpperCase() == val.toUpperCase() && val.length >= 1)) {
                    /*create a DIV element for each matching element:*/
                    item = document.createElement("DIV");
                    /*make the matching letters bold:*/
                    item.innerHTML = "<strong>" + cities[i].name.substr(0, val.length) + "</strong>";
                    item.innerHTML += cities[i].name.substr(val.length);
        
                    /*insert a input field that will hold the current array item's value:*/
                    item.innerHTML += "<input type='hidden' value='" + cities[i].name + "'>";
                    /*execute a function when someone clicks on the item value (DIV element):*/
                    item.addEventListener("click", function(e) {
                        /*insert the value for the autocomplete text field:*/
                        element = ListManager.getElement();
                        element.value = this.getElementsByTagName("input")[0].value;
                        const code = cities.filter(e => e.name==element.value)[0].code;
                        document.getElementById('city').disabled = cities.map(e => e.name).indexOf(element.value) == -1
                        /*close the list of autocompleted values, (or any other open lists of autocompleted values:*/
                        ListManager.closeAllLists();
                    });
                    itemsList.appendChild(item);
                }
            }
        } catch(e) {}
        
    }

    return {
        keyupCallback: keyupCallback,
        inputCallback: inputCallback,
        inputCallbackCity: inputCallbackCity
    }
})()
