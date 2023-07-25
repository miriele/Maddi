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
	
	$("input[name='differlocate']").on(
		"click",
		function(){
		    new daum.Postcode({
			    oncomplete : function (data) {
			    	var address  = data.roadAddress; // 도로명 주소
					//var geocoder = new kakao.maps.services.Geocoder();
					geocoder.addressSearch(address, callback);				    					    	
				}
		    }).open();
		    
		    var callback = function(result, status) {
				if (status === kakao.maps.services.Status.OK) {
					long = result[0].road_address.x
					lat  = result[0].road_address.y
					
					//console.log(lat, long)
					var moveLatLon = new kakao.maps.LatLng(lat, long);
					kakaomap.panTo(moveLatLon); 
					
					
				 }
			}	// var callback = function(result, status)
		}
	);	// $("input[name='differlocate']").on(
});	// $(function()

var windowHeight	= $(window).height();
var	windowWidth		= $(window).width();

$(window).on('resize', function() {
	windowHeight	= $(window).height();
	windowWidth		= $(window).width();

	//console.log(windowHeight);
	
	setLayoutSize();
});

function setLayoutSize() {
	height = windowHeight*0.4;
	
	var	mapWidth		= windowWidth; 
	var	mapHeight		= height>300 ? 300 : height;
	
	//console.log(height, mapHeight)

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
		// 위치 권한 허용하지 않으면 비트빌 좌표가 기본값
		lat		= 37.49455001;
		long	= 127.02747878;
	}
	
	//console.log(lat, long)

	var container = document.getElementById(div);	// 지도를 담을 영역의 DOM 레퍼런스
	var options = {									// 지도를 생성할 때 필요한 기본 옵션
		center: new kakao.maps.LatLng(lat, long),	// 지도의 중심좌표
		level: 5									// 지도의 레벨(확대, 축소 정도) : 1~14
	};
	
	kakaomap = new kakao.maps.Map(container, options);	// 지도 생성 및 객체 리턴
	
	// 줌 컨트롤 생성
	var zoomControl = new kakao.maps.ZoomControl();
	kakaomap.addControl(zoomControl, kakao.maps.ControlPosition.BOTTOMRIGHT);

	searchDetailAddrFromCoords(kakaomap.getCenter(), displayCenterInfo);
	
	// 지도가 이동, 확대, 축소로 인해 중심좌표가 변경되는 경우
	kakao.maps.event.addListener(kakaomap, 'center_changed', function() {
		searchDetailAddrFromCoords(kakaomap.getCenter(), displayCenterInfo);
	});	// kakao.maps.event.addListener(kakaomap, 'center_changed', function()
}

var geocoder = new kakao.maps.services.Geocoder();

function searchDetailAddrFromCoords(coords, callback) {
    // 좌표로 법정동 상세 주소 정보 얻기
    geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
}

function displayCenterInfo(result, status) {
	if (status === kakao.maps.services.Status.OK) {
		// 지도에 현재 법정동 위치 표시 해주기
		var infoDiv = document.getElementById('centerAddr');
		var cur_loc = '현재위치 : ' + result[0].address.address_name;
		
		infoDiv.innerHTML = cur_loc; 
		
		// 검색할 때 법정동 코드 얻기 위해 법정도 설정
		var element_bjd = $("input[name='bjd_name']");
		var states_s    = ["경기", "서울", "부산", "경남", "인천",
						   "대구", "경북", "충남", "전북", "광주",
						   "전남", "대전", "강원특별자치도", "충북", "울산",
						   "제주특별자치도", "세종특별자치시"];
		var states_l	= ["경기도", "서울특별시", "부산광역시", "경상남도", "인천광역시",
						   "대구광역시", "경상북도", "충청남도", "전라북도", "광주광역시",
						   "전라남도", "대전광역시", "강원특별자치도", "충청북도", "울산광역시",
						   "제주특별자치도", "세종특별자치시"];
		
		var region1  = result[0].address.region_1depth_name;
		var region2  = result[0].address.region_2depth_name;
		var region3  = result[0].address.region_3depth_name.split(' ');
		
		var bjd_name = states_l[states_s.indexOf(region1)];
		bjd_name += ' ' + region2;
		bjd_name += ' ' + region3[0];

		console.log(bjd_name);
		console.log(kakaomap.getLevel())
		
		element_bjd.value = bjd_name;
	}    
}

function panTo() {
    // 이동할 위도 경도 위치를 생성합니다 
    var moveLatLon = new kakao.maps.LatLng(33.450580, 126.574942);
    
    // 지도 중심을 부드럽게 이동시킵니다
    // 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
    map.panTo(moveLatLon);            
}    