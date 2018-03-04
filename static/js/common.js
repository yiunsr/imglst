
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var _$dialog = jQuery(
		  '<div class="modal fade"  id="loadingModal" data-backdrop="static" data-keyboard="false" tabindex="-1" role="dialog" aria-hidden="true" style="padding-top:15%;">' +
		  '<div class="modal-dialog modal-m">' +
		  '<div class="modal-content">' +
		    '<div class="modal-header"><h3 style="margin:0;" class="loading"></h3></div>' +
		    '<div class="modal-body">' +
		      '<div class="progress">' +
		        '<div class="progress-bar bg-success progress-bar-striped progress-bar-animated" style="width: 100%"></div></div>' +
		    '</div>' +
		  '</div></div></div>');

_$dialog.appendTo( "body" );

function _loading(bShow ){
	var message = "Loading";

	
	_$dialog.find('.progress-bar').css("width", 100 + "%");
   
    if(bShow){
        var settings = jQuery.extend({
        dialogSize: 'm',
        progressType: '',
        onHide: null // This callback runs after the dialog was hidden
        });
        
        if (settings.progressType) {
        	_$dialog.find('.progress-bar').addClass('progress-bar-' + settings.progressType);
    }
    _$dialog.find('h3').text(message);
    // Adding callbacks
    if (typeof settings.onHide === 'function') {
        _$dialog.off('hidden.bs.modal').on('hidden.bs.modal', function (e) {
            settings.onHide.call(_$dialog);
        });
    }
    
    // Opening dialog
    _$dialog.modal('show');
    console.log("loading dialog show");

}
  
else {
  _$dialog.modal('hide');
  console.log("loading dialog hide");
    }
  }