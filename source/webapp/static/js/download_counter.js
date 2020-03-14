const baseUrl = 'http://localhost:8000/api/v1/';


function setUpIncrementButtons(){
    let buttons = $('.download-link');
    buttons.each(function(index){
        let link = $(this);
        link.on('click', function(event){
            makeRequest(`file/${link.attr('id')}/increment/`, 'patch').done(function(data, status, message){
                console.log(data);
                console.log(status);
                console.log(message);
            }).fail(function (response, message, data){
                console.log(response);
                console.log(message);
                console.log(data);
                }
            )
        })
    })
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path;
}

function makeRequest(path, method, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    return $.ajax(settings);
}

$(document).ready(function() {
    setUpIncrementButtons();
});