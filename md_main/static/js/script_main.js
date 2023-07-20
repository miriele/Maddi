$(document).ready(
	function(){
		if ("geolocation" in navigator) {	// geolocation으로 내 위치를 경도로 받아옴 
			navigator.geolocation.getCurrentPosition(
				function(data) {
					let lat = data.coords.latitude;
					let long = data.coords.longitude;					
					//console.log(data.coords.longitude);
					//console.log(data.coords.latitude);
					//alert("위도 : " + lat + " 경도 : " + long );\
				$("input[name='differlocate']").on(
					"click",
					function(){
					    new daum.Postcode({
					      oncomplete: 
					      function (data) {
					        var address = data.roadAddress; // 도로명 주소
					       	var geocoder = new kakao.maps.services.Geocoder();
					    	geocoder.addressSearch(address, callback);				    					    	
					    	
					    	}
					    	
					    	}).open()		    	
					    var callback = function(result, status) {
					    if (status === kakao.maps.services.Status.OK) {
					        long = result[0].road_address.x
					        lat = result[0].road_address.y
							//주소찾기로 받아어
					        //console.log(long) //126.710895581433
					       	//console.log(lat)  //37.5240309973244
					     }
					 			}//event						

					}
				)
						console.log(long)
					    console.log(lat)				
					var mapContainer = document.getElementById('map'), // 지도생성
					    mapOption = {
					        center: new kakao.maps.LatLng(lat,long), // 지도
					        level: 5 // 지도의 확대 레벨
					    };    	        					
					// 지도를 생성
					var map = new kakao.maps.Map(mapContainer, mapOption); 
					
					// 주소-좌표 변환
					var geocoder = new kakao.maps.services.Geocoder();
							
					// 현재 지도 중심좌표로 주소를 검색해서 지도 좌측 상단에 표시합니다
					searchAddrFromCoords(map.getCenter(), displayPresentInfo);
					
					function searchAddrFromCoords(coords, callback) {
					    // 좌표로 행정동 주소 정보를 요청합니다
					    geocoder.coord2RegionCode(coords.getLng(), coords.getLat(), callback);         
					}
					
					// 지도 하단에 내위치에 대한 법정동주소를 표출하는 함수입니다
					function displayPresentInfo(result, status) {
					    if (status === kakao.maps.services.Status.OK) {
					        var infoDiv = document.getElementById('centerAddr');
						for(var i = 0; i < result.length; i++) {
		    		// 행정동의 region_type 값은 'H' 이므로
		    				if (result[i].region_type === 'H') {
		        				infoDiv.innerHTML = result[i].address_name;
								}
					}
					//console.log(long)
					}//if    
					}//displayPresentInfo										                        					 			
										
					},
					
			function(error) {
				alert(error);
			}, 
			
			{
				enableHighAccuracy: true,
				timeout: Infinity,
				maximumAge: 0
			});
			
			} 
			else {// geolocation 사용 불가능 
				alert('geolocation 사용 불가능');
			}
						
}//function
)//on;

