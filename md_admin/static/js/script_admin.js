$(function() {
	//성별통계(전체)
	//hidden으로 인원수 리스트,성별이름리스트 불러오기
	var data = $('#inwon').text();
	var labels = $('#gend').text();
	
	//배열형태의 string을 array로 변환
	var arraydata = data.replace("[","").replace("]","").split(',');
	
	//배열형태의 string을 array로 변환
	var arraylabel = labels.replace("[","").replace("]","").split(',');
	var gender = $('#gender')
	
	new Chart(gender, {
	    type: 'pie',
	    data: {
	      labels: arraylabel, //labels
	      datasets: [{
	        label: '# of Votes',
	        data: arraydata, //data
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	 //남성회원 연령대 분포
	 var managecount = $('#man_agecount').text()
	 var manarrayage = managecount.replace("[","").replace("]","").split(',');
	 
	 var gender_man = $('#gender_man')
	 
	 new Chart(gender_man, {
	    type: 'bar',
	    data: {
	      labels: ['10대','20대','30대','40대','50대','60대이상'],
	      datasets: [{
	        label: '# of Votes',
	        data: manarrayage, 
	        borderWidth: 1,
	        borderColor: '#36A2EB',
	        backgroundColor: '#9BD0F5',
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	 //여성회원 연령대 분포
	 var womanagecount = $('#woman_agecount').text()
	 var womanarrayage = womanagecount.replace("[","").replace("]","").split(',');
	 
	 var gender_woman = $('#gender_woman')
	 
	 new Chart(gender_woman, {
	    type: 'bar',
	    data: {
	      labels: ['10대','20대','30대','40대','50대','60대이상'],
	      datasets: [{
	        label: '# of Votes',
	        data: womanarrayage, 
	        borderWidth: 1,
	        backgroundColor: '#F08080'
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	 //연령통계(전체)
	 var agecount = $('#agecount').text()
	 var arrayage = agecount.replace("[","").replace("]","").split(',');
	 
	 var age = $('#age')
	 
	 new Chart(age, {
	    type: 'pie',
	    data: {
	      labels: ['10대','20대','30대','40대','50대','60대이상'],
	      datasets: [{
	        label: '# of Votes',
	        data: arrayage, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	 //관심사통계(전체)
	 var listinter = $('#list_inter').text()
	 var inter_name = $('#inter_name').text()
	 
	 var interarray = listinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter = $('#inter')
	 
	 new Chart(inter, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: interarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	 //관심사통계(남성10대)
	 var mteenlistinter = $('#manteen_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var mtinterarray = mteenlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_manteen = $('#inter_manteen')
	 
	 new Chart(inter_manteen, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtinterarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		

	 //관심사통계(남성20대)
	 var mtwelistinter = $('#mantwe_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var mtweinterarray = mtwelistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_mantwe = $('#inter_mantwe')
	 
	 new Chart(inter_mantwe, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtweinterarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		

	 //관심사통계(남성30대)
	 var mthrlistinter = $('#manthr_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var mthrinterarray = mthrlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_manthr = $('#inter_manthr')
	 
	 new Chart(inter_manthr, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mthrinterarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		

	 //관심사통계(남성40대)
	 var mfoulistinter = $('#manfou_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var mfouinterarray = mfoulistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_manfou = $('#inter_manfou')
	 
	 new Chart(inter_manfou, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtinterarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		
	 
	 //관심사통계(남성50대)
	 var mfivlistinter = $('#manfiv_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var mfivinterarray = mfivlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_manfiv = $('#inter_manfiv')
	 
	 new Chart(inter_manfiv, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfivinterarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		
	 
	 //관심사통계(남성60대 이상)
	 var mordlistinter = $('#manord_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var mordinterarray = mordlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_manord = $('#inter_manord')
	 
	 new Chart(inter_manord, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mordinterarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });

	 //관심사통계(여성10대)
	 var wmteenlistinter = $('#womanteen_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var wmtinterarray = wmteenlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_womanteen = $('#inter_womanteen')
	 
	 new Chart(inter_womanteen, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmtinterarray, 
	        borderWidth: 1,
	        backgroundColor: '#F08080'
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		

	 //관심사통계(여성20대)
	 var wmtwelistinter = $('#womantwe_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var wmtweinterarray = wmtwelistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_womantwe = $('#inter_womantwe')
	 
	 new Chart(inter_womantwe, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmtweinterarray, 
	        borderWidth: 1,
	        backgroundColor: '#F08080'
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		

	 //관심사통계(여성30대)
	 var wmthrlistinter = $('#womanthr_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var wmthrinterarray = wmthrlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_womanthr = $('#inter_womanthr')
	 
	 new Chart(inter_womanthr, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmthrinterarray, 
	        borderWidth: 1,
	        backgroundColor: '#F08080'
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		

	 //관심사통계(여성40대)
	 var wmfoulistinter = $('#womanfou_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var wmfouinterarray = wmfoulistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_womanfou = $('#inter_womanfou')
	 
	 new Chart(inter_womanfou, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfouinterarray, 
	        borderWidth: 1,
	        backgroundColor: '#F08080'
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		
	 
	 //관심사통계(여성50대)
	 var wmfivlistinter = $('#womanfiv_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var wmfivinterarray = wmfivlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_womanfiv = $('#inter_womanfiv')
	 
	 new Chart(inter_womanfiv, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfivinterarray, 
	        borderWidth: 1,
	        backgroundColor: '#F08080'
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		
	 
	 //관심사통계(여성60대 이상)
	 var wmordlistinter = $('#womanord_list').text()
	 var inter_name = $('#inter_name').text()
	 
	 var wmordinterarray = wmordlistinter.replace("[","").replace("]","").split(',');
	 var inamearray = inter_name.replace("[","").replace("]","").split(',');
	 
	 var inter_womanord = $('#inter_womanord')
	 
	 new Chart(inter_womanord, {
	    type: 'bar',
	    data: {
	      labels: inamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmordinterarray, 
	        borderWidth: 1,
	        backgroundColor: '#F08080'
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });	 
	 
	 		 	 	 	 	
	//입맛통계(전체)
	 var tastcount = $('#list_tast').text()
	 var tastname = $('#tast_n').text()
	 
	 var tastearray = tastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var taste = $('#taste')
	 
	 new Chart(taste, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: tastearray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	 //매장현황(전체)
	 var storcount = $('#stor_count').text()
	 var storcarray = storcount.replace("[","").replace("]","").split(',');
	 
	 var stor = $('#stor')
	 
	 new Chart(stor, {
	    type: 'pie',
	    data: {
	      labels: ['개인','프랜차이즈'], 
	      datasets: [{
	        label: '# of Votes',
	        data: storcarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	//회원디저트취향(전체)
	 var dsrtcount = $('#list_dsrt').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var dsrtarray = dsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var stor = $('#dsrt')
	 
	 new Chart(stor, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: dsrtarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });

	//회원음료취향(전체)
	 var drnkcount = $('#list_drnk').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var drnkarray = drnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk = $('#drnk')
	 
	 new Chart(drnk, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: drnkarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	//구매기반음료취향(전체)
	 var bdrnkcount = $('#list_bdrnk').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var bdrnkarray = bdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');

	 var bdrnk = $('#bdrnk')
	 
	 new Chart(bdrnk, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: bdrnkarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	 //구매기반디저트취향(전체)
	 var bdsrtcount = $('#list_bdsrt').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var bdsrtarray = bdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtkarray = bdsrtname.replace("[","").replace("]","").split(',');

	 var bdsrt = $('#bdsrt')
	 
	 new Chart(bdsrt, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: bdsrtarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	//회원유입
	 var wusercount = $('#list_welmaddi').text()
	 var wuserday = $('#upwelyearlist').text()
	 
	 var wuserarray = wusercount.replace("[","").replace("]","").split(',');
	 var wuserdayarray = wuserday.replace("[","").replace("]","").split(',');

	 var iao = $('#iao')
	 
	 new Chart(iao, {
	    type: 'line',
	    data: {
	      labels: wuserdayarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wuserarray, 
	        borderWidth: 1
	      }]
	    },
	    options: {
			responsive: false,
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
	 
	//키워드 워드클라우드
	 var data_list = $('#data_list').text()
	 //console.log(data_list)
	 var dataarray = data_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var jsonData = dataarray.replace(/'/g, '"');
	 var data = jsonData.replace(/^"|"$/g, "");
	 var validJsonString = data.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	 //console.log(validJsonString)
	
	 var resultObject = JSON.parse(validJsonString);
	 //console.log((resultObject));
	 
	 var wordCloudData = [];
	 
	 //형식에 맞게 출력
	 for (var i = 0; i < resultObject.length; i++) {
            wordCloudData.push({
                "x": resultObject[i].x,
                "value": resultObject[i].weight
            });
        }
        
	 //console.log(wordCloudData)
	 
	 // WordCloud를 생성하고 데이터를 설정
	 var chart = anychart.tagCloud(wordCloudData);
	 //console.log(resultObject);

	
	  // WordCloud가 그려질 컨테이너를 지정
	 chart.container("container");
	
	  // 차트를 그림
	 chart.draw();
	 
 })