$(function() {
	setLayoutSize();

	// initialize kakaomap
	// : https 가 아닌 상황에서는 getCurrentPosition() 이 제대로 동작하지 않아서
	// : 처음에는 기본 값으로 초기화 해주고 시작
	initializeMap('kakaomap', null);

	// get geolocation
	if("geolocation" in navigator) {
		navigator.geolocation.getCurrentPosition(
			function(data) {
				// initializeMap('kakaomap', data.coords);
				var moveLatLon = new kakao.maps.LatLng(data.coords.latitude, data.coords.longitude)
				kakaomap.panTo(moveLatLon);
			}
		)	// navigator.geolocation.getCurrentPosition(
	} else {
		// alert('geolocation 사용 불가능');
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

	$("input[name='search_word']").on(
		"keyup",
		function(event) {
			if(event.key === "Enter") {
				closeKeywords();
				$("input[name='main_btn_search']").click();
				return;
			} else if(event.key === "Escape") {
				closeKeywords();
				return;
			}

			$.ajax(
				{
					url  : "searchword",
					type : "POST",
					data : {
						search_word : $("input[name='search_word']").val(),
						csrfmiddlewaretoken: "{{ csrf_token }}",
					},	// data : {
					datatype : "text",
					success : function(data) {
						$(".rel-srch-words").empty();
						
						var menu_list = Object.values(data);
						//console.log(menu_list);
						
						const $ul = $("<ul>");
						
						for(let menu of menu_list) {
							$ul.append("<li>" + menu + "</li>");
						}
						
						$(".rel-srch-words").append($ul);
						$(".rel-srch-words").show();
					},	// success : function(data) {
					error : function(request, status, error) {
						console.log(error);
						//$("").html("서버요청실패");
					}	// error : function(request, status, error)
				}
			)	// $.ajax(
		}	// function(event) {
	);	// $("input[name='search_word']").on(
	
	$(document).on(
		"click",
		function(event) {
			const hasSearchWord = event.target.closest(".rel-srch-words");
			if(!hasSearchWord && $(".rel-srch-words").css("display")==="block") {
				closeKeywords();
			}
		}	// function(event)
	);	// $(document).on(
	
	$(document).on(
		"keydown",
		function(event) {
			if(event.key === "Enter") {
				event.preventDefault();
			}
		}	// function(event)
	);	// $(document).on(
	
	$(".rel-srch-words").on(
		"click",
		function(event) {
			$("input[name='search_word']").val(event.target.textContent);
			closeKeywords();
		}	// function(event)
	);	// $("input[name='search_word']").on(

/*
	$("input[name='main_btn_search']").on(
		"click",
		function(event) {
			$.ajax(
				{
					url  : "searchlist",
					type : "POST",
					data : {
						search_word : $("input[name='search_word']").val(),
						bjd_name    : $("input[name='bjd_name']").val(),
						csrfmiddlewaretoken: "{{ csrf_token }}",
					},	// data : {
					datatype : "text",
					success : function(data) {
						//console.log(data);
						var content = `
							<h3>[${data.menu_name}] 판매 매장 : ${data.count}</h3>
							${data.count === 0 ? '판매 중인 매장이 없습니다.' : `
								${data.store_list.map(function(store, index) {
									return `
										<div class="main_search_result_item" style="cursor:pointer" onclick="location.href='/md_store/storeuser?stor_id=${store.stor_id}'">
											<table>
												<tr>
													<td rowspan="2"><img src="/media/${store.stor_img}" class="main_search_result_img"></td>
													<td>${store.stor_name}</td>
												</tr>
												<tr>
													<td>${store.area_t_name}</td>
												</tr>
											</table>
										</div>
									`;
								}).join('')}
							`}
							`;
						$('.main_search_result').html(content);
					},	// success : function(data) {
					error : function(request, status, error) {
						console.log(error);
						//$("").html("서버요청실패");
					}	// error : function(request, status, error)
				}
			)	// $.ajax(
		}	// function(event) {
	);	// $("input[name='search_word']").on(
*/
});	// $(function()



////////// 검색 //////////
function setMenuName(menuName) {
	$("input[name='search_word']").val(menuName);
}

function performSearch() {
	var bounds		= kakaomap.getBounds();
	var swLatLng	= bounds.getSouthWest();
	var neLatLng	= bounds.getNorthEast();

	$.ajax(
		{
			url  : "searchlist",
			type : "POST",
			data : {
				search_word : $("input[name='search_word']").val(),
				bjd_name    : $("input[name='bjd_name']").val(),
				latiSouth   : swLatLng.getLat(),
				latiNorth   : neLatLng.getLat(),
				longWest    : swLatLng.getLng(),
				longEast    : neLatLng.getLng(),
				csrfmiddlewaretoken: "{{ csrf_token }}",
			},	// data : {
			datatype : "text",
			success : function(data) {
				//console.log(data);
				var content = `
					<h3>[${data.menu_name}] 판매 매장 : ${data.count}</h3>
					${data.count === 0 ? '판매 중인 매장이 없습니다.' : `
						${data.store_list.map(function(store, index) {
							return `
								<div class="main_search_result_item" style="cursor:pointer" onclick="location.href='/md_store/storeuser?stor_id=${store.stor_id}'">
									<table>
										<tr>
											<td rowspan="2"><img src="/media/${store.stor_img}" class="main_search_result_img"></td>
											<td>${store.stor_name}</td>
										</tr>
										<tr>
											<td>${store.area_t_name}</td>
										</tr>
									</table>
								</div>
							`;
						}).join('')}
					`}
					`;
				$('.main_search_result').html(content);
			},	// success : function(data) {
			error : function(request, status, error) {
				console.log(error);
				//$("").html("서버요청실패");
			}	// error : function(request, status, error)
		}
	)	// $.ajax(
}	// function(event) {


////////// 연관 검색어 //////////
function closeKeywords() {
	$(".rel-srch-words").empty();
	$(".rel-srch-words").hide();
}


////////// 카카오 맵 //////////
var windowHeight	= $(window).height();
var	windowWidth		= $(window).width();

$(window).on('resize', function() {
	windowHeight	= $(window).height();
	windowWidth		= $(window).width();

	//console.log(windowHeight);
	
	setLayoutSize();
});

function setLayoutSize() {
	let MAX_SIZE	= 450;
	let width		= windowWidth*0.25;
	let height		= windowHeight*0.4;
	let	mapWidth	= width >MAX_SIZE ? MAX_SIZE : width; 
	let	mapHeight	= height>MAX_SIZE ? MAX_SIZE : height;
	//console.log(height, mapHeight)

	$('.kakaomap').css({'width' : mapWidth +'px'});
	$('.kakaomap').css({'height': mapHeight+'px'});
	$('.recommend-list').css({'width' : windowWidth-mapWidth +'px'});
	
	
	let searchInput	= $('.search_input');
	let relWidth	= searchInput[0].offsetWidth;
	let relHeight	= searchInput[0].offsetHeight;
	let relPosX		= searchInput[0].offsetLeft;
	let relPosY		= searchInput[0].offsetTop;
//	console.log(elementRel);
//	console.log(relWidth, relHeight, relPosX, relPosY);
//	console.log("setLayoutSize");
	
	$('.rel-srch-words').css({'top': relPosY+relHeight+'px'});
	$('.rel-srch-words').css({'left': relPosX+'px'});
	$('.rel-srch-words').css({'width' : relWidth +'px'});
}


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
//	var zoomControl = new kakao.maps.ZoomControl();
//	kakaomap.addControl(zoomControl, kakao.maps.ControlPosition.BOTTOMRIGHT);

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
		var cur_loc =  result[0].address.address_name;

		infoDiv.innerHTML = cur_loc; 
		
		// 검색할 때 법정동 코드 얻기 위해 법정동 설정
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
		//console.log(bjd_name);
		
		element_bjd.val(bjd_name);
		//console.log(element_bjd.val())
		//console.log(kakaomap.getLevel())
	}    
}


window.onload = function() {
	  const images = document.querySelectorAll('.img');
	  let current = 0;

	  function showSlide() {
	    for (let i = 0; i < images.length; i++) {
	      images[i].classList.remove('on');
	    }
	    current++;
	    if (current > images.length) {
	      current = 3;
	    }
	    images[current - 1].classList.add('on');
	    setTimeout(showSlide, 2000);
	  }

	  showSlide();
	};