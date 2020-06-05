$(document).ready(function() {
    FilterManager.reloadLastFilters();
    if(document.getElementById('country').value === '') document.getElementById('city').disabled = true;
    $(window).keydown(function(event){
        if(event.keyCode == KEY_CODES.ENTER) {
            event.preventDefault();
            return false;
        }
    });
});