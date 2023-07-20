//여기는 ~이런 경우면 안돼게 막는 페이지
$(document).ready(
	function() {
		var iderror = "아이디를 입력하세요.";
		
		
		
		function erroralert(msg) {
			alert(msg);
			history.back();
			//이동한 페이지들의 주소를 갖고 있음 히스토리가
		}
		
		//아이디 중복확인
		$("input[name='user_id']").on(
			"keyup",
			function(event) {
				$.ajax(
					{
						url : "idcheck",
						type : "GET",
						data : {
							user_id : $("input[name='user_id']").val()
						},
						datatype :"text",
						success : function( data ) {
							if ( data == 1 ){
								$("#checkid").html("사용 불가 아이디");
								$("#checkid").attr("color", "red");
							} else {
								$("#checkid").html("사용가능 아이디");
								$("#checkid").attr("color", "green");
							}/**/
						},
						error : function(request, status, error) {
							//alert("서버요청실패");
							$("#checkid").html("서버요청실패");
						}
					}
				)
			}//function
		);//on
		
		// 닉네임 중복확인
		$("input[id='iuser_nick']").on(
			"keyup",
			function(event) {
				$.ajax(
					{
						url : "nickcheck",
						type : "GET",
						data : {
							iuser_nick : $("input[id='iuser_nick']").val()
						},
						datatype :"text",
						success : function( data ) {
							if ( data == 1 ){
								$("#checknick").html("사용 불가 닉네임");
								$("#checknick").attr("color", "red");
							} else {
								$("#checknick").html("사용가능 닉네임");
								$("#checknick").attr("color", "green");
							}/**/
						},
						error : function(request, status, error) {
							//alert("서버요청실패");
							$("#checknick").html("서버요청실패");
						}
					}
				)
			}//function
		);//on
		
	}	//function
)	//ready
		
	




