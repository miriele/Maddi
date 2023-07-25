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
		$("input[name='replybtn']").on(
			"click",
			function(event) {
				var button = $(this);
				var csrfToken = "{{ csrf_token }}";
				$.ajax(
					{
						url : "combd",
						type : "POST",
						data : {
							comb_id : $("input[name='comb_id']").val(),
							pagenum : $("input[name='pagenum']").val(),
							number 	: $("input[name='number']").val(),
							c_reply_cont : $("textarea[name='c_reply_cont']").val(),
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
			}//function
		);//on
		
		
		// 좋아요 ajax
		$("input[name='clikebtn']").on(
			"click",
			function(event) {
				var button = $(this);
				var csrfToken = "{{ csrf_token }}";
				$.ajax(
					{
						url : "clike",
						type : "POST",
						data : {
							comb_id : $("input[name='comb_id']").val(),
							pagenum : $("input[name='pagenum']").val(),
							number  : $("input[name='number']").val(),
							csrfmiddlewaretoken: csrfToken,
						},
						datatype :"text",
						success : function( data ) {
							if ( data == "1" ){
								button.val("좋아요 취소");
							}
							else {
								button.val("좋아요");								
							}
						},
						error : function(request, status, error) {
							alert("서버요청실패");
						}
					}
				)
			}	// function
		);	// $("form[name='clikeform']").on
	}	//function
)	//ready
		
	




