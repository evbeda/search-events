$(document).ready(function() {
    document.addEventListener("click", function (e) {
        ListManager.closeAllLists();
    });
    try {
        document.getElementById("country").addEventListener("input", inputEvents.inputCallback, false);
        document.getElementById("country").addEventListener("keyup", inputEvents.keyupCallback, false);
        document.getElementById("city").addEventListener("input", inputEvents.inputCallbackCity, false);
        document.getElementById("city").addEventListener("keyup", inputEvents.keyupCallback, false);
        FilterManager.reloadLastFilters();
        FilterManager.reloadLastState();
    }catch(e){}

    $(window).keydown(function(event) {
        if(event.keyCode == KEY_CODES.ENTER) {
            event.preventDefault();
            return false;
        }
    });
});