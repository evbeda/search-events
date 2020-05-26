const loginManager = (function() {
$('form').submit(function(e){ e.preventDefault(); });
    function login() {
        $('#login_btn').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').addClass('disabled');
    };

    return {
        login: login
    }
})()