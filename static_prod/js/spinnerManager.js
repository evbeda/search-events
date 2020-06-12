const SpinnerManager = (function() {
    
    function showSpinner(){
		document.getElementById("submit-form").style.display = "none";
		document.getElementById("table-events").style.display = "none";
		document.getElementById("accordion").style.display = "none";
		document.getElementById("spin").style.display = "block";
    }
    
    return {
		showSpinner
	}
})()
