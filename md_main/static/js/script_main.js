$(function() {
	// initialize kakaomap
	setLayoutSize();
	
	// get geolocation
	if("geolocation" in navigator) {
		navigator.geolocation.getCurrentPosition(
			function(data) {
				initializeMap('kakaomap', data.coords);
			}
		)	// navigator.geolocation.getCurrentPosition(
	} else {
		alert('geolocation 사용 불가능');
		initializeMap('kakaomap', null);
	}	// if("geolocation" in navigator)
});	// $(function()

/*
$(document).ready(function() {

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
				)	// $("input[name='differlocate']").on(
					
				console.log(long)
			    console.log(lat)				
				
				var mapContainer = document.getElementById('map');
				var mapOption = {
				        center: new kakao.maps.LatLng(lat,long),
				        level: 5 // 지도의 확대 레벨
				    };    	        					
				
				// 지도 생성
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
					}	// if (status === kakao.maps.services.Status.OK)    
				}	// function displayPresentInfo(result, status)										                        					 			
									
			},
				
			function(error) {
				alert(error);
			}, 
			
			{
				enableHighAccuracy: true,
				timeout: Infinity,
				maximumAge: 0
			}
		);	// navigator.geolocation.getCurrentPosition(
	}	// if ("geolocation" in navigator) 
	else { 
		alert('geolocation 사용 불가능');
	}
}	// function
)	// $(document).ready(
*/

var windowHeight	= $(window).height();
var	windowWidth		= $(window).width();

$(window).on('resize', function() {
	windowHeight	= $(window).height();
	windowWidth		= $(window).width();

	console.log(windowHeight);
	
	setLayoutSize();
});

function setLayoutSize() {
	height = windowHeight*0.4;
	
	var	mapWidth		= windowWidth; 
	var	mapHeight		= height>300 ? 300 : height;
	
	console.log(height, mapHeight)

	$('.areaMap').css({'width' : mapWidth +'px'});
	$('.areaMap').css({'height': mapHeight+'px'});
}


////////// kakaomap //////////
var	kakaomap;

function initializeMap(div, coords) {
	var lat		= 0;
	var long	= 0;

	if(coords) {
		lat		= coords.latitude;
		long	= coords.longitude;
	} else {
		lat		= 37.49455001;
		long	= 127.02747878;
	}
	
	console.log(lat, long)

	var container = document.getElementById(div);	// 지도를 담을 영역의 DOM 레퍼런스
	var options = {									// 지도를 생성할 때 필요한 기본 옵션
		center: new kakao.maps.LatLng(lat, long),	// 지도의 중심좌표
		level: 3									// 지도의 레벨(확대, 축소 정도) : 1~7
	};
	
	kakaomap = new kakao.maps.Map(container, options);				// 지도 생성 및 객체 리턴
	
	// 줌 컨트롤 생성
	var zoomControl = new kakao.maps.ZoomControl();
	kakaomap.addControl(zoomControl, kakao.maps.ControlPosition.BOTTOMRIGHT);
}


