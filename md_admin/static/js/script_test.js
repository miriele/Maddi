//admin/test.js
$(document).ready(
	function() {
		$("input[name='ordr_done']").on(
			"click",
			function(event) {
				var button = $(this);
				var csrfToken = "{{ csrf_token }}";
				$.ajax(
					{
						url : "testorder",
						type : "POST",
						data : {
							ordr_id : $("input[name='ordr_id']").val(),
							csrfmiddlewaretoken: csrfToken,
						},
						datatype :"text",
						success : function( data ) {
							location.reload();
						},
						error : function(request, status, error) {
							alert("서버요청실패");
						}
					}
				)
			}	// function
		);	// $("form[name='ordr_done']").on
	}	//function
)	//ready
		