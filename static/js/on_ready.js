$(document).ready(function() {
    FilterManager.reloadLastFilters();

    $(window).keydown(function(event){
        if(event.keyCode == KEY_CODES.ENTER) {
            event.preventDefault();
            return false;
        }
    });
});