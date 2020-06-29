const ColorManager = (function() {
    const FILTER_IDS = ["country", "online", "language", "format", "category", "price", "currency", "city", "event_name", "organizer", "buyer", "venue", "datefilter", "card"];

    function reloadFiltersColor(){
        FILTER_IDS.forEach(filter => {
            const domElement = document.getElementById(filter);
            if(domElement.value){
                $('#'+filter).addClass("selected-orange");
            }
        });
    }
    function changeColor(domId, condition=true) {
        const hasValue = document.getElementById(domId).value != "" && condition;
        $('#'+domId).toggleClass("selected-orange", hasValue);
    }

    function changeColorFeature(condition=true) {
        try{
            const hasValue = document.getElementById('feature').value != "" && condition;
            $(".filter-option-inner-inner").toggleClass("selected-orange", hasValue);
            
        }
        catch(e){}
    }
    return {
        reloadFiltersColor,
        changeColor,
        changeColorFeature,
    }
})()