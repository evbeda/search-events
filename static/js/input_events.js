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
            currentFocus = ListManager.getCurrentFocus()
            if (currentFocus > -1 && x) x[currentFocus].click();
        }
    }

    const inputCallback = function(e) {
        let itemsList, item, val = this.value;
        /*close any already open lists of autocompleted values*/
        ListManager.closeAllLists();
        if (!val) { return false; }
        /*create a DIV element that will contain the items (values):*/
        itemsList = document.createElement("DIV");
        itemsList.setAttribute("id", this.id + "autocomplete-list");
        itemsList.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(itemsList);
    
        arr = ListManager.getArr();
        for (i = 0; i < arr.length; i++) {
            /*check if the item starts with the same letters as the text field value:*/
            if ((arr[i].alpha2Code.toUpperCase() == val.toUpperCase() && val.length == 2) || (arr[i].name.substr(0, val.length).toUpperCase() == val.toUpperCase() && val.length >= 3)) {
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
                    element = ListManager.getElement();
                    element.value = this.getElementsByTagName("input")[0].value;
                    /*close the list of autocompleted values, (or any other open lists of autocompleted values:*/
                    ListManager.closeAllLists();
                });
                itemsList.appendChild(item);
            }
        }
    }

    return {
        keyupCallback: keyupCallback,
        inputCallback: inputCallback,
    }
})()
