//여기는 ~이런 경우면 안돼게 막는 페이지
$(document).ready(
	function() {
		
		function erroralert(msg) {
			alert(msg);
			history.back();
			//이동한 페이지들의 주소를 갖고 있음 히스토리가
		}
		
		
		// 즐겨찾기 ajax
		$("input[name='addfavbtn']").on(
			"click",
			function(event) {
				var button = $(this);
				var csrfToken = "{{ csrf_token }}";
				$.ajax(
					{
						url : "addfav",
						type : "POST",
						data : {
							stor_id : $("input[name='stor_id']").val(),
							pagenum : $("input[name='pagenum']").val(),
							number  : $("input[name='number']").val(),
							csrfmiddlewaretoken: csrfToken,
						},
						datatype :"text",
						success : function( data ) {
							if ( data == "1" ){
								button.val("즐겨찾기 취소");
							}
							else {
								button.val("즐겨찾기 등록");
							}						
						},
						error : function(request, status, error) {
							alert("서버요청실패");
						}
					}
				)
			}	// function
		);	// $("form[name='addfavform']").on
	}	// function
)	// $(document).ready
		
	




