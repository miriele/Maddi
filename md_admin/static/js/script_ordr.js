//admin/ordr.js
$(document).ready(
	function() {
		$("input[name='ordr_done']").on(
			"click",
			function(event) {
				var button = $(this);
				var csrfToken = "{{ csrf_token }}";
				$.ajax(
					{
						url : "order",
						type : "POST",
						data : {
							ordr_id : $(this).attr('id'),
							csrfmiddlewaretoken: csrfToken,
						},
						datatype :"text",
						success : function( data ) {
							//location.reload();
							console.log(data);
							btnId = '#ordr_id_' + data.ordr_id;
							//tdId  = '#td_id_' + data.ordr_id;

							eleInput = $(btnId);
							//eleTd    = $(tdId);

							eleInput.attr('value', '주문 완료');
							eleInput.attr('disabled', true);
							//eleTd.text(data.comTime);
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
		