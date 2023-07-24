//여기는 ~이런 경우면 안돼게 막는 페이지
$(document).ready(
	function() {
		var replyok = "댓글이 등록되었습니다."
		var replyno = "댓글이 등록되지 않아습니다. 다시 시도해 주십시오"		
		
		function erroralert(msg) {
			alert(msg);
			history.back();
			//이동한 페이지들의 주소를 갖고 있음 히스토리가
		}
		
		
		// 댓글 ajax
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
		
		
		// 좋아요 ajax
		$("form[name='clikeform']").on(
			"submit",
			function(event) {
				$.ajax(
					{
						url : "clike",
						type : "POST",
						data : {
							comb_id : $("input[name='comb_id']").val(),
							pagenum : $("input[name='pagenum']").val(),
							number : $("input[name='number']").val(),
						},
						datatype :"text",
						success : function( data ) {
							if ( data == 1 ){
								alert("replyok")
							}
							else {
								alert("replyno")								
							}
						},
						error : function(request, status, error) {
							alert("서버요청실패");
						}
					}
				)
			}	// function
		);	// $("form[name='clikeform']").on
	}	// function
)	// $(document).ready
		
	




