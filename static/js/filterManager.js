const FilterManager = (function() {
    
    const FILTERS_BY_DEFAULT = {
        "country": "United States",
        "language": "en",
        "online": "",
        "format": "",
        "category": "",
        "price": "",
        "currency": "USD",
    }
    
    function reloadLastFilters() {
        try {
            const filters = ["country", "online", "language", "format", "category", "price", "currency"];
            filters.forEach(function(filter) {
                const lastValue = querySt(filter);
                if(lastValue != undefined){
                    document.getElementById(filter).value = lastValue;
                } 
                else if (FILTERS_BY_DEFAULT[filter]) {
                    document.getElementById(filter).value = FILTERS_BY_DEFAULT[filter] ;
                }

            });
    
            validateOnlineConstraint();
            validateFreeConstraint();
    
            features = querySt("feature");
            if(features) selectLastFilters("feature", features);
        } catch(e) {}
    }

    function validateOnlineConstraint() {
        const online_dom = document.getElementById("online");
        if (online_dom.value == "on") toggleDisable("divCountry", "country", online_dom.value, 'on');
    }

    function validateFreeConstraint() {
        const price_dom = document.getElementById("price");
        if (price_dom.value == "free") toggleDisable("divCurrency", "currency", price_dom.value, 'free');
    }

    function toggleDisable(divId, inputId, value, valueToHide) {
        const div = document.getElementById(divId);
        const input = document.getElementById(inputId);
        if(value == valueToHide) input.value = '';
        const visibility = div.style.visibility
        div.style.visibility = value == valueToHide ? 'hidden' : 'visible';
        if(div.style.visibility !== visibility && div.style.visibility === 'visible' && visibility){
            input.value = FILTERS_BY_DEFAULT[inputId];
        }
    }
    
    function selectLastFilters(domId, stringFilters) {
        const options = document.getElementById(domId).options;
        const filters = stringFilters.split("-");
    
        for(var i = 0; i < options.length; i++){
            const option = options[i];
            if(filters.indexOf(option.value) !== -1) option.selected = true;
        }
    }
    
    function clearFilters() {
        const show_ids = ["divCountry", "divCurrency"];
        const clear_ids = ["country", "online", "language", "format", "category", "price", "currency"];
        clear_ids.forEach(function (id) {
             filter = document.getElementById(id);
             filter.value = FILTERS_BY_DEFAULT[id];
        });
        
        show_ids.forEach(function(id) {
            filter = document.getElementById(id);
            filter.style.visibility = "visible";
        });
    
        clearSelected("feature");
    }
    
    function clearSelected(domId) {
        const domElement = document.getElementById(domId);
        domElement.value = "";
        const options = domElement.options;
    
        for(let i = 0; i < options.length; i++) {
          options[i].selected = false;
        }
        
        $(domElement.nextSibling).addClass('bs-placeholder');
        document.getElementsByClassName("filter-option-inner-inner")[0].innerText = domElement.title;
    }
    
    function getDefaultFilters(){
        return FILTERS_BY_DEFAULT
    }

    return {
        clearFilters: clearFilters,
        reloadLastFilters: reloadLastFilters,
        toggleDisable: toggleDisable,
        getDefaultFilters : getDefaultFilters
    }
})()
