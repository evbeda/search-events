const querySt = function(param) {
    hu = window.location.search.substring(1);
    gy = hu.split("&");

    for (i=0;i<gy.length;i++) {
        ft = gy[i].split("=");
        if (ft[0] == param) {
            return ft[1].replace(/\+/g, " ");
        }
    }
}
