const FilterManager = (function() {
    
    const FILTERS_BY_DEFAULT = {
        "country": "United States",
        "language": "en",
        "online": "",
        "format": "",
        "category": "",
        "price": "",
        "currency": "USD",
        "city": "",
        "event_name": "",
        "organizer": "",
        "buyer": "",
        "venue": "",
        "datefilter": "",
        "card": ""
    }

    const VALUES_TO_HIDE = {
        "online": {
           "value": "on",
           "divsToHide": ["divCountry", "divCity"],
           "inputs": ["country", "city"]
        },
        "price": {
            "value": "free",
            "divsToHide": ["divCurrency"],
            "inputs": ["currency"]
         }
    }
    
    const FILTER_IDS = ["country", "online", "language", "format", "category", "price", "currency", "city", "event_name", "organizer", "buyer", "venue", "datefilter", "card"];
    const LATEST_FILTERS = {}
    
    function reloadLastFilters() {
        try {
            FILTER_IDS.forEach(function(filter) {
                const lastValue =  querySt(filter);
                if(lastValue !== undefined){
                    document.getElementById(filter).value = decodeURIComponent(lastValue).trim();
                } else if (FILTERS_BY_DEFAULT[filter]) {
                    document.getElementById(filter).value = FILTERS_BY_DEFAULT[filter];
                }
            });
            
            validateConstraint("online");
            validateConstraint("price");

           
            features = querySt("feature");
            if(features) selectLastFeatures("feature", features);
        } catch(e) {}
    }

    function reloadLastState() {
        document.getElementById("city").disabled = document.getElementById("country").value ? false : true;
    }

    function validateConstraint(domId) {
        domElement = document.getElementById(domId)
        if (domElement.value == VALUES_TO_HIDE[domId]["value"]){
            toggleDisable(domId);
        }  
    }

    function toggleDisable(domId) {
        const valuesToHide = VALUES_TO_HIDE[domId];
        const changedDomElement = document.getElementById(domId);
        const divToHideIds = valuesToHide["divsToHide"];
        const inputToChangeValueIds = valuesToHide["inputs"];
        for(let i = 0; i < divToHideIds.length; i++) {
            const divId = divToHideIds[i];
            const div = document.getElementById(divId);
            const previousVisibility = div.style.visibility;
            changeFilterVisibility(div, changedDomElement);
            const inputId = inputToChangeValueIds[i];
            updateInputValue(inputId, div.style.visibility, previousVisibility);
        }
    }
    
    function changeFilterVisibility(domElement, changedDomElement) {
        const actualValue = changedDomElement.value;
        const valueToHide = VALUES_TO_HIDE[changedDomElement.id]["value"];
        domElement.style.visibility = actualValue == valueToHide ? 'hidden' : 'visible';
    }

    function updateInputValue(inputId, newVisibility, previousVisibility='visible') {
        const input = document.getElementById(inputId);
        if(previousVisibility !== newVisibility) {
            if(newVisibility === 'hidden') {
                LATEST_FILTERS[inputId] = input.value;
                input.value = '';
            } else if(LATEST_FILTERS[inputId]){
                input.value = LATEST_FILTERS[inputId];
            }
        }
    }
    
    function selectLastFeatures(domId, stringFeatures) {
        const options = document.getElementById(domId).options;
        const features = stringFeatures.split("-");
    
        for(var i = 0; i < options.length; i++){
            const option = options[i];
            if(features.indexOf(option.value) !== -1) option.selected = true;
        }
    }
    
    function clearFilters() {
        restoreFilterValuesByDefault();
        showFilters(["divCountry", "divCurrency", "divCity"]);
        clearSelectedFeatures();
    }

    function restoreFilterValuesByDefault () {
        try {
            FILTER_IDS.forEach(function (id) {
                filter = document.getElementById(id);
                $('#'+id).val(FILTERS_BY_DEFAULT[id]).trigger('change');
                ColorManager.changeColor('country', true)
                filter.disabled = false;
            });
        } catch (e) {}
    }

    function showFilters(show_ids){
        show_ids.forEach(function(id) {
            filter = document.getElementById(id);
            filter.style.visibility = "visible";
        });
    }

    function clearSelectedFeatures() {
        try {
            const domElement = document.getElementById("feature");
            $('#feature').val('').trigger('change')
            const options = domElement.options;
        
            for(let i = 0; i < options.length; i++) {
              options[i].selected = false;
            }
            
            $(domElement.nextSibling).addClass('bs-placeholder');
            document.getElementsByClassName("filter-option-inner-inner")[0].innerText = domElement.title;
        } catch(e) {}
    }

    function toggleFilterVisibility() {
        if($('#collapseOne').hasClass('show')) {
            document.getElementById('collapseIcon').innerText = 'visibility_off';
            document.getElementById('collapseText').innerText = 'Show Filters';
        } else {
            document.getElementById('collapseIcon').innerText = 'visibility';
            document.getElementById('collapseText').innerText = 'Hide Filters';
        }    
    }

    return {
        clearFilters,
        reloadLastFilters,
        toggleDisable,
        reloadLastState,
        toggleFilterVisibility
    }
})()
