function myFunction() {
    var x = document.getElementById("url").value;
    var expression = /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;
    var regex = new RegExp(expression);
    // var url = 'www.geeksforgeeks.org';
    // el_up.innerHTML = "URL = '" + url + "'";
    var res = "";
    if (x.match(regex)) {
        res = "Valid URL";
    } else {
        res = "Invalid URL";
    }
    // el_down.innerHTML = res;
    document.getElementById("display").innerHTML = res;
}