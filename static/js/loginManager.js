const loginManager = (function() {
    
    function login() {
        $('#login_btn').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').addClass('disabled');
        document.getElementById("login_btn").disabled = true;
    };

    return {
        login
    }
})()
