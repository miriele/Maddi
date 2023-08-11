//여기는 ~이런 경우면 안돼게 막는 페이지
$(document).ready(
	function() {
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
							comb_id 		: $("input[name='comb_id']").val(),
							user_img 		: $("input[name='user_img']").val(),
							user_nick 		: $("input[name='user_nick']").val(),
							c_reply_cont 	: $("textarea[name='c_reply_cont']").val(),
							csrfmiddlewaretoken: csrfToken,
						},
						datatype :"text",
						success : function( data ) {
							//location.reload();
							console.log(data);
							var content = `
								<table>
									<tr>
										<td>
											<img src="/media/${data.user_img}" width="50" height="50" border-radius="50%" >
											${data.user_nick} / ${data.rep_ts}
										</td>
									</tr>
									<tr>
										<td>
											${data.rep_cont}
										</td>
									</tr>
								</table>
							`;
							$("#new_repl").html(content);
						},
						error : function(request, status, error) {
							//alert("서버요청실패");
							$("#check").html("서버요청실패");
							$("#check").attr("color", "red");
						}
					}//ajax
				)
			}//function
		);//on
		//${data(function(){} ).join('')}
		
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
		
	




