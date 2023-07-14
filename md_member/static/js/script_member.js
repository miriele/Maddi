//여기는 ~이런 경우면 안돼게 막는 페이지
$(document).ready(
	function() {
		var iderror = "아이디를 입력하세요.";
		var passwderror = "비밀번호를 입력하세요.";
		var nameerror = "이름을 입력하세요.";
		var nickerror = "이메일을 입력하세요.";
		var birerror = "생년월일을 입력하세요.";
		
		var inputerror = "회원가입에 실패했습니다.\n 잠시 후 다시 시도하세요.";
		var idxerror ="입력하신 아이디가 없습니다.\n다시 확인하세요.";
		var passerror ="입력하신 비밀번호가 다릅니다.\n다시 확인하세요.";
		var deleteerror ="회원탈퇴에 실패했습니다\n 잠시후 다시 시도하세요.";
		var modifyerror ="회원정보수정에 실패했습니다\n 잠시후 다시 시도하세요.";
		
		
		function erroralert(msg) {
			alert(msg);
			history.back();
			//이동한 페이지들의 주소를 갖고 있음 히스토리가
		}
		/* 
		
		//회원정보 수정
		function modifycheck() {
			if( ! modifyform.passwd.value) {
				alert(passwderror);
				modifyform.passwd.focus();
				return false;
			}else if (modifyform.passwd.value != modifyform.repasswd.value) {
				alert(repasswderror);
				modifyform.passwd.focus();
				return false;
			}
		}
		//빈칸인 상태에서 수정 버튼 누르면 넘어가지 말아라
		$("input[value='수정']").on(
			"click", 
			function (event) {
				if( ! passwdform.passwd.value) {
					alert(passwderror);
					passwdform.passwd.focus();
					return false;
				}
			}
		);
		
		
		
		// 회원탈퇴
		$("input[value='탈퇴']").on(
			"click", 
			function (event) {
				if( ! passwdform.passwd.value) {
					alert(passwderror);
					passwdform.passwd.focus();
					return false;
				}
			}
		);
			
		
		//아이디 중복확인
		$("input[value='중복확인']").on(
			"click",
			function (event) {
				var id = $("input[name='id']").val();
				if( ! id ) {
					alert(iderror);
					inputform.id.focus();
				} else {			//새팝업을 띄워라
					url = "confirm?id=" + id;	//여기도 url주소가 들어가는 자리
					open(url, "confirm", "scrollbar=no, statusbar=no, titlebar=no, menubar=no, width=400px, height=250px");
				}
			}//function
		);//on
		
		//중복체크 할 때 빈칸이면 넘어가지 말라고
		//제이쿼리로>자바스크립트랑 섞어써도 동작함 어차피 제이쿼리도 자바스크립트라서 
		$( "input[value='확인']").on (
			"click",
			function (event) {
				if( ! confirmform.id.value ) {
					alert(iderror);
					confirmform.id.focus();
					return false;
				}
			}
		);
		
		//가능 아이디를 확인 누르면 아이디 칸에 들어가게 하는거
		$( "input[value='사용']").on (
			"click",
			function (event) {
				opener.document.inputform.id.value = $("td span").text();	//출력된 글자 가져오려면 텍스트나 html사용	
				//=id;이렇게 잡으면 이쪽에서 아이디를 넘길 수 없음?
				opener.document.inputform.check.value = "1";		
				// 중복확인 학 위해 히든으로 된 체크란 변수 필요
				window.close();
			}
		);
		*/
		
		//가입페이지
		$("form[name='inputform']").on(
			"submit",
			function() {
				var bdate = document.getElementById("user_bir").value;
				if( ! $( "input[name='user_id']").val() ) {
					alert(iderror);
					inputform.user_id.focus();
					return false;	
				} else if(! $( "input[name='user_pass]").val() ) {
					alert( passwderror);
					inputform.user_pass.focus();
					return false;	
				}else if ( ! $( "input[name='user_name']").val() ) {
					alert(nameerror);
					inputform.user_name.focus();
					return false;	
				} else if( ! $( "input[name='user_nick']").val() ) {
					alert(nickerror);
					inputform.user_name.focus();
					return false;
				}else if(bdate == null ) {
					alert(birerror);
					inputform.user_bir.focus();
					return false;
				}
				//3칸 데이터가 없거나 짧으면>데이터가 다 있으면
				
			}//function
		);//on	
		
	
	
		
		//메인페이지>로그인 화면에서 아이디 비번 입력안 했음 경고창을 띄어라
		$("form[name='loginform']").on(
			"submit", 
			function( event ) {
				if( ! $( "input[name='user_id']").val() ) {	//아이디에 값이 없을떄는 경고창 띄워라
					alert( iderror );
					$("input[name='user_id']").focus();
					return false;
				} else if ( ! $("input[name='user_pass']").val() ) {
					alert( passwderror );
					$("input[name='user_pass']").focus();
					return false;
				}
			}
		);
	
	
	}	//function
)	//ready