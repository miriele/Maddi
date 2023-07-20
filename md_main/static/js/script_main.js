$(document).ready(
	function(){	
		if ("geolocation" in navigator) {	/* geolocation으로 내 위치를 경도로 받아옴 */
			navigator.geolocation.getCurrentPosition(
				function(data) {	
					var lat = data.coords.latitude;
					var long = data.coords.longitude;
																												

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
			}//if    
		}//displayPresentInfo										                        					 
					
		}, function(error) {
			alert(error);
		}, {
			enableHighAccuracy: true,
			timeout: Infinity,
			maximumAge: 0
		});
		} 
		else {/* geolocation 사용 불가능 */
			alert('geolocation 사용 불가능');
		}
			
//다른위치설정 클릭시 주소찾기 api 후 해당주소 맵으로 띄우기		
		$("input[name='differlocate']").on(
			"click",		
			function(event){
				if($(".differ_wrap").css("display")==='none'){
					$(".differ_wrap").show();
				
			    new daum.Postcode({
			      oncomplete: 
			      function (data) {
					var RAddress = data.roadAddress //주소찾기 api에서 도로명주소 클릭시 지번주소로변환
					data.jibunAddress = data.roadAddress
			        var address = data.jibunAddress; // 지번 주소
			        document.getElementsByName("address")[0].value = address;//지번주소 출력
			        RAddress.innerHTML
			    	address.innerHTML
			    	}
			    	}).open()		    	
					  			    	
				    var callback = function(result, status) {
				    if (status === kakao.maps.services.Status.OK) {
				        var lat = result[0].road_address.x
				        var lon = result[0].road_address.y
				     }  
				     //console.log("좌표값 :" + result[0].road_address.x)
				    var mapContainer = document.getElementById('map'), // 지도
					    mapOption = {
					        center: new kakao.maps.LatLng(lat, lon), // 지도
					        level: -1 // 지도의 확대 레벨
					};

					
					// 지도를 생성
					var map = new kakao.maps.Map(mapContainer, mapOption); 
					
					// 주소-좌표 변환
					var geocoder = new kakao.maps.services.Geocoder();
							
					// 현재 지도 중심좌표로 주소를 검색해서 지도 좌측 상단에 표시합니다
					searchDetailAddrFromCoords(map.getCenter(), displayPresentInfo);
					
					function searchDetailAddrFromCoords(coords, callback) {
					    geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
					}

					
					
					};
				}//display open
			}//event
		)//input[name='differlocate']
}//function
)//on;

