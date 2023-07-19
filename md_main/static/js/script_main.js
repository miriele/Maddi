$(document).ready(
	function(){	
		if ("geolocation" in navigator) {	/* geolocation으로 내 위치를 경도로 받아옴 */
			navigator.geolocation.getCurrentPosition(
				function(data) {	
					var lat = data.coords.latitude;
					var long = data.coords.longitude;																			
			$("input[name='prelocate']").on( //현재위치설정시 내위치에 해당하는 지도정보와 주소출력 이벤트
				"click",
				function(event){
					if($(".map_wrap").css("display")==='none'){
						$(".map_wrap").show();
					}else{
						$(".map_wrap").hide();
					}
					
					var mapContainer = document.getElementById('map'), // 지도
					    mapOption = {
					        center: new kakao.maps.LatLng(lat, long), // 지도
					        level: -1 // 지도의 확대 레벨
					    };  
					
					// 지도를 생성
					var map = new kakao.maps.Map(mapContainer, mapOption); 
					
					// 주소-좌표 변환
					var geocoder = new kakao.maps.services.Geocoder();
							
					// 현재 지도 중심좌표로 주소를 검색해서 지도 좌측 상단에 표시합니다
					searchDetailAddrFromCoords(map.getCenter(), displayPresentInfo);
					
					function searchDetailAddrFromCoords(coords, callback) {
					    // 좌표로 지번 상세 주소 정보를 요청합니다
					    geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
					}
					
					// 지도 하단에 내위치에 대한 지번주소를 표출하는 함수입니다
					function displayPresentInfo(result, status) {
					    if (status === kakao.maps.services.Status.OK) {
					        var infoDiv = document.getElementById('centerAddr');
							infoDiv.innerHTML = result[0].address.address_name;
							//console.log('지번주소 : ' + result[0].address.address_name);
	        				//console.log('행정구역 코드 : ' + result[0].code);
	
					    }    
					}										                        					 
				}
			)					
					
		}, function(error) {
			alert(error);
		}, {
			enableHighAccuracy: true,
			timeout: Infinity,
			maximumAge: 0
		});
		} else {	/* geolocation 사용 불가능 */
			alert('geolocation 사용 불가능');
		}	
		
		$("input[name='differlocate']").on(//다른위치설정 클릭시 위치설정 템플릿으로
			"click",
			function(event){
			    new daum.Postcode({
			      oncomplete: function (data) {
			        var address = data.jibunAddress; // 지번 주소
			        document.getElementsByName("address")[0].value = address;//지번주소 출력
			        address.innerHTML
			      }
			    }).open();		
			}
		)
}//function
)//on;

