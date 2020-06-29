$(document).ready(function() {
    DatePickerManager.loadDatePickers();

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
        ColorManager.reloadFiltersColor();
    } catch(e) {}
    
    if(window.location.href.indexOf("FindFeature")!= -1) {
        $("#find_specific").removeClass('active');
        $("#find_feature").addClass('active');
    } else if(window.location.href.indexOf("SpecificEvent")!= -1) {
        $("#find_feature").removeClass('active');
        $("#find_specific").addClass('active');
    }
    
    $(window).keydown(function(event) {
        if(event.keyCode == KEY_CODES.ENTER) {
            event.preventDefault();
            return false;
        }
    });
});
