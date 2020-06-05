const FilterManager = (function() {
    
    const FILTERS_BY_DEFAULT = {
        "country": "United States",
        "language": "en",
        "online": "",
        "format": "",
        "category": "",
        "price": "",
        "currency": "USD",
        "city": ""
    }

    const VALUES_TO_HIDE = {
        "online": "on",
        "price": "free"
    }

    const LATEST_FILTERS = {}
    
    function reloadLastFilters() {
        try {
            const filters = ["country", "online", "language", "format", "category", "price", "currency", "city"];
            filters.forEach(function(filter) {
                const lastValue = querySt(filter);
                if(lastValue !== undefined){
                    document.getElementById(filter).value = lastValue;
                } else if (FILTERS_BY_DEFAULT[filter]) {
                    document.getElementById(filter).value = FILTERS_BY_DEFAULT[filter];
                }
            });
    
            validateOnlineConstraint();
            validateFreeConstraint();
    
            features = querySt("feature");
            if(features) selectLastFilters("feature", features);
        } catch(e) {}
    }

    function reloadLastState() {
        document.getElementById("city").disabled = document.getElementById("country").value ? false : true;
    }

    function validateOnlineConstraint() {
        const online_dom = document.getElementById("online");
        if (online_dom.value == "on") toggleDisable(["divCountry", "divCity"], ["country", "city"], online_dom);
    }

    function validateFreeConstraint() {
        const price_dom = document.getElementById("price");
        if (price_dom.value == "free") toggleDisable(["divCurrency"], ["currency"], price_dom);
    }

    function toggleDisable(divToHideIds, inputToChangeValueIds, changedDomElement) {
        for(let i = 0; i < divToHideIds.length; i++) {
            const divId = divToHideIds[i];
            const div = document.getElementById(divId);
            const previousVisibility = div.style.visibility;
            changeFilterVisibility(div, changedDomElement);
            const inputId = inputToChangeValueIds[i];
            updateInputValue(inputId, previousVisibility, div.style.visibility);
        }
    }
    
    function changeFilterVisibility(domElement, changedDomElement) {
        const actualValue = changedDomElement.value;
        const valueToHide = VALUES_TO_HIDE[changedDomElement.id];
        domElement.style.visibility = actualValue == valueToHide ? 'hidden' : 'visible';
    }

    function updateInputValue(inputId, previousVisibility='visible', newVisibility) {
        const input = document.getElementById(inputId);
        if(previousVisibility !== newVisibility) {
            if(newVisibility === 'hidden') {
                LATEST_FILTERS[inputId] = input.value;
                input.value = '';
            } else {
                input.value = LATEST_FILTERS[inputId];
            }
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
        const show_ids = ["divCountry", "divCurrency", "divCity"];
        const clear_ids = ["country", "online", "language", "format", "category", "price", "currency", "city"];
        clear_ids.forEach(function (id) {
             filter = document.getElementById(id);
             filter.value = FILTERS_BY_DEFAULT[id];
             filter.disabled = false;
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
        getDefaultFilters : getDefaultFilters,
        reloadLastState: reloadLastState
    }
})()
