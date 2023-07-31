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

	//입맛통계(10대남성)
	 var teentastcount = $('#manteen_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var teentastearray = teentastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_manteen = $('#tast_manteen')
	 
	 new Chart(tast_manteen, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: teentastearray, 
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
	 
	//입맛통계(20대남성)
	 var twetastcount = $('#mantwe_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var twetastearray = twetastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_mantwe = $('#tast_mantwe')
	 
	 new Chart(tast_mantwe, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: twetastearray, 
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
	 
	//입맛통계(30대남성)
	 var thrtastcount = $('#manthr_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var thrtastearray = thrtastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_manthr = $('#tast_manthr')
	 
	 new Chart(tast_manthr, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: thrtastearray, 
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
	 
	//입맛통계(40대남성)
	 var foutastcount = $('#manfou_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var foutastearray = foutastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_manfou = $('#tast_manfou')
	 
	 new Chart(tast_manfou, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: foutastearray, 
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
	 
	//입맛통계(50대남성)
	 var fivtastcount = $('#manfiv_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var fivtastearray = fivtastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_manfiv = $('#tast_manfiv')
	 
	 new Chart(tast_manfiv, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: fivtastearray, 
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
	 
	//입맛통계(60대이상남성)
	 var ordtastcount = $('#manord_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var ordtastearray = ordtastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_manord = $('#tast_manord')
	 
	 new Chart(tast_manord, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: ordtastearray, 
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

	//입맛통계(10대여성)
	 var wteentastcount = $('#womanteen_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var wteentastearray = wteentastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_womanteen = $('#tast_womanteen')
	 
	 new Chart(tast_womanteen, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wteentastearray, 
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
	 
	//입맛통계(20대여성)
	 var wtwetastcount = $('#womantwe_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var wtwetastearray = wtwetastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_womantwe = $('#tast_womantwe')
	 
	 new Chart(tast_womantwe, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wtwetastearray, 
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
	 
	//입맛통계(30대여성)
	 var wthrtastcount = $('#womanthr_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var wthrtastearray = wthrtastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_womanthr = $('#tast_womanthr')
	 
	 new Chart(tast_womanthr, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wthrtastearray, 
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
	 
	//입맛통계(40대여성)
	 var wfoutastcount = $('#womanfou_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var wfoutastearray = wfoutastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_womanfou = $('#tast_womanfou')
	 
	 new Chart(tast_womanfou, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wfoutastearray, 
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
	 
	//입맛통계(50대여성)
	 var wfivtastcount = $('#womanfiv_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var wfivtastearray = wfivtastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_womanfiv = $('#tast_womanfiv')
	 
	 new Chart(tast_womanfiv, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wfivtastearray, 
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
	 
	//입맛통계(60대이상여성)
	 var wordtastcount = $('#womanord_tlist').text()
	 var tastname = $('#tast_n').text()
	 
	 var wordtastearray = wordtastcount.replace("[","").replace("]","").split(',');
	 var tnamearray = tastname.replace("[","").replace("]","").split(',');
	 
	 var tast_womanord = $('#tast_womanord')
	 
	 new Chart(tast_womanord, {
	    type: 'pie',
	    data: {
	      labels: tnamearray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wordtastearray, 
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
	 
	 var dsrt = $('#dsrt')
	 
	 new Chart(dsrt, {
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

	//남성회원디저트취향(10대)
	 var mteendsrtcount = $('#manteen_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var mteendsrtarray = mteendsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_manteen = $('#dsrt_manteen')
	 
	 new Chart(dsrt_manteen, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mteendsrtarray, 
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
	 
	//남성회원디저트취향(20대)
	 var mtwedsrtcount = $('#mantwe_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var mtwedsrtarray = mtwedsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_mantwe = $('#dsrt_mantwe')
	 
	 new Chart(dsrt_mantwe, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtwedsrtarray, 
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
	 
	//남성회원디저트취향(30대)
	 var mthrdsrtcount = $('#manthr_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var mthrdsrtarray = mthrdsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_manthr = $('#dsrt_manthr')
	 
	 new Chart(dsrt_manthr, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mthrdsrtarray, 
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
	 
	//남성회원디저트취향(40대)
	 var mfoudsrtcount = $('#manfou_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var mfoudsrtarray = mfoudsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_manfou = $('#dsrt_manfou')
	 
	 new Chart(dsrt_manfou, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfoudsrtarray, 
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
	 
	//남성회원디저트취향(50대)
	 var mfivdsrtcount = $('#manfiv_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var mfivdsrtarray = mfivdsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_manfiv = $('#dsrt_manfiv')
	 
	 new Chart(dsrt_manfiv, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfivdsrtarray, 
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
	 
	//남성회원디저트취향(60대이상)
	 var morddsrtcount = $('#manord_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var morddsrtarray = morddsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_manord = $('#dsrt_manord')
	 
	 new Chart(dsrt_manord, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: morddsrtarray, 
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

	//여성회원디저트취향(10대)
	 var wmteendsrtcount = $('#womanteen_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var wmteendsrtarray = wmteendsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_womanteen = $('#dsrt_womanteen')
	 
	 new Chart(dsrt_womanteen, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmteendsrtarray, 
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
	 
	//여성회원디저트취향(20대)
	 var wmtwedsrtcount = $('#womantwe_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var wmtwedsrtarray = wmtwedsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_womantwe = $('#dsrt_womantwe')
	 
	 new Chart(dsrt_womantwe, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmtwedsrtarray, 
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
	 
	//여성회원디저트취향(30대)
	 var wmthrdsrtcount = $('#womanthr_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var wmthrdsrtarray = wmthrdsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_womanthr = $('#dsrt_womanthr')
	 
	 new Chart(dsrt_womanthr, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmthrdsrtarray, 
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
	 
	//여성회원디저트취향(40대)
	 var wmfoudsrtcount = $('#womanfou_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var wmfoudsrtarray = wmfoudsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_womanfou = $('#dsrt_womanfou')
	 
	 new Chart(dsrt_womanfou, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfoudsrtarray, 
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
	 
	//여성회원디저트취향(50대)
	 var wmfivdsrtcount = $('#womanfiv_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var wmfivdsrtarray = wmfivdsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_womanfiv = $('#dsrt_womanfiv')
	 
	 new Chart(dsrt_womanfiv, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfivdsrtarray, 
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
	 
	//여성회원디저트취향(60대이상)
	 var wmorddsrtcount = $('#womanord_dslist').text()
	 var dsrtname = $('#dsrt_n').text()
	 
	 var wmorddsrtarray = wmorddsrtcount.replace("[","").replace("]","").split(',');
	 var ndsrtarray = dsrtname.replace("[","").replace("]","").split(',');
	 
	 var dsrt_womanord = $('#dsrt_womanord')
	 
	 new Chart(dsrt_womanord, {
	    type: 'bar',
	    data: {
	      labels: ndsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmorddsrtarray, 
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
	 
	  	 	 	 	 
	//전체회원음료취향
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

	//남성회원음료취향(10대)
	 var mteendrnkcount = $('#manteen_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var mteendrnkarray = mteendrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_manteen = $('#drnk_manteen')
	 
	 new Chart(drnk_manteen, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mteendrnkarray, 
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
	 
	//남성회원음료취향(20대)
	 var mtwedrnkcount = $('#mantwe_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var mtwedrnkarray = mtwedrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_mantwe = $('#drnk_mantwe')
	 
	 new Chart(drnk_mantwe, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtwedrnkarray, 
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
	 
	//남성회원음료취향(30대)
	 var mthrdrnkcount = $('#manthr_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var mthrdrnkarray = mthrdrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_manthr = $('#drnk_manthr')
	 
	 new Chart(drnk_manthr, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mthrdrnkarray, 
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
	 
	//남성회원음료취향(40대)
	 var mfoudrnkcount = $('#manfou_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var mfoudrnkarray = mfoudrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_manfou = $('#drnk_manfou')
	 
	 new Chart(drnk_manfou, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfoudrnkarray, 
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
	 
	//남성회원음료취향(50대)
	 var mfivdrnkcount = $('#manfiv_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var mfivdrnkarray = mfivdrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_manfiv = $('#drnk_manfiv')
	 
	 new Chart(drnk_manfiv, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfivdrnkarray, 
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
	 
	//남성회원음료취향(60대이상)
	 var morddrnkcount = $('#manord_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var morddrnkarray = morddrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_manord = $('#drnk_manord')
	 
	 new Chart(drnk_manord, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: morddrnkarray, 
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

	//여성회원음료취향(10대)
	 var wmteendrnkcount = $('#womanteen_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var wmteendrnkarray = wmteendrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_womanteen = $('#drnk_womanteen')
	 
	 new Chart(drnk_womanteen, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmteendrnkarray, 
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
	 
	//여성회원음료취향(20대)
	 var wmtwedrnkcount = $('#womantwe_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var mtwedrnkarray = wmtwedrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_womantwe = $('#drnk_womantwe')
	 
	 new Chart(drnk_womantwe, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtwedrnkarray, 
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
	 
	//여성회원음료취향(30대)
	 var wmthrdrnkcount = $('#womanthr_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var wmthrdrnkarray = wmthrdrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_womanthr = $('#drnk_womanthr')
	 
	 new Chart(drnk_womanthr, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmthrdrnkarray, 
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
	 
	//여성회원음료취향(40대)
	 var wmfoudrnkcount = $('#womanfou_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var wmfoudrnkarray = wmfoudrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_womanfou = $('#drnk_womanfou')
	 
	 new Chart(drnk_womanfou, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfoudrnkarray, 
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
	 
	//여성회원음료취향(50대)
	 var wmfivdrnkcount = $('#womanfiv_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var wmfivdrnkarray = wmfivdrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_womanfiv = $('#drnk_womanfiv')
	 
	 new Chart(drnk_womanfiv, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfivdrnkarray, 
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
	 
	//여성회원음료취향(60대이상)
	 var wmorddrnkcount = $('#womanord_drlist').text()
	 var drnkname = $('#drnk_n').text()
	 
	 var wmorddrnkarray = wmorddrnkcount.replace("[","").replace("]","").split(',');
	 var ndrnkarray = drnkname.replace("[","").replace("]","").split(',');
	 
	 var drnk_womanord = $('#drnk_womanord')
	 
	 new Chart(drnk_womanord, {
	    type: 'bar',
	    data: {
	      labels: ndrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmorddrnkarray, 
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


	//구매기반음료취향(전체)
	 var bdrnkcount = $('#bdrnk_list').text()
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

	//남성구매기반음료취향(10대)
	 var mteenbdrnkcount = $('#manteen_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var mteenbdrnkarray = mteenbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_manteen = $('#bdrnk_manteen')
	 
	 new Chart(bdrnk_manteen, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mteenbdrnkarray, 
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
	 
	//남성구매기반음료취향(20대)
	 var mtwebdrnkcount = $('#mantwe_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var mtwebdrnkarray = mtwebdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_mantwe = $('#bdrnk_mantwe')
	 
	 new Chart(bdrnk_mantwe, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtwebdrnkarray, 
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
	 
	//남성구매기반음료취향(30대)
	 var mthrbdrnkcount = $('#manthr_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var mthrbdrnkarray = mthrbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_manthr = $('#bdrnk_manthr')
	 
	 new Chart(bdrnk_manthr, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mthrbdrnkarray, 
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
	 
	//남성구매기반음료취향(40대)
	 var mfoubdrnkcount = $('#manfou_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var mfoubdrnkarray = mfoubdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_manfou = $('#bdrnk_manfou')
	 
	 new Chart(bdrnk_manfou, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfoubdrnkarray, 
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
	 
	//남성구매기반음료취향(50대)
	 var mfivbdrnkcount = $('#manfiv_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var mfivbdrnkarray = mfivbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_manfiv = $('#bdrnk_manfiv')
	 
	 new Chart(bdrnk_manfiv, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfivbdrnkarray, 
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
	 
	//남성구매기반음료취향(60대이상)
	 var mordbdrnkcount = $('#manord_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var mordbdrnkarray = mordbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_manord = $('#bdrnk_manord')
	 
	 new Chart(bdrnk_manord, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mordbdrnkarray, 
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

	//여성구매기반음료취향(10대)
	 var wmteenbdrnkcount = $('#womanteen_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var wmteenbdrnkarray = wmteenbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_womanteen = $('#bdrnk_womanteen')
	 
	 new Chart(bdrnk_womanteen, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmteenbdrnkarray, 
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
	 
	//여성구매기반음료취향(20대)
	 var wmtwebdrnkcount = $('#womantwe_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var wmtwebdrnkarray = wmtwebdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_womantwe = $('#bdrnk_womantwe')
	 
	 new Chart(bdrnk_womantwe, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmtwebdrnkarray, 
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
	 
	//여성구매기반음료취향(30대)
	 var wmthrbdrnkcount = $('#womanthr_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var wmthrbdrnkarray = wmthrbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_womanthr = $('#bdrnk_womanthr')
	 
	 new Chart(bdrnk_womanthr, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmthrbdrnkarray, 
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
	 
	//여성구매기반음료취향(40대)
	 var wmfoubdrnkcount = $('#womanfou_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var wmfoubdrnkarray = wmfoubdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_womanfou = $('#bdrnk_womanfou')
	 
	 new Chart(bdrnk_womanfou, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfoubdrnkarray, 
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
	 
	//여성구매기반음료취향(50대)
	 var wmfivbdrnkcount = $('#womanfiv_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var wmfivbdrnkarray = wmfivbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_womanfiv = $('#bdrnk_womanfiv')
	 
	 new Chart(bdrnk_womanfiv, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfivbdrnkarray, 
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
	 
	//여성구매기반음료취향(60대이상)
	 var wmordbdrnkcount = $('#womanord_bdrlist').text()
	 var bdrnkname = $('#bdrnk_n').text()
	 
	 var wmordbdrnkarray = wmordbdrnkcount.replace("[","").replace("]","").split(',');
	 var nbdrnkarray = bdrnkname.replace("[","").replace("]","").split(',');
	 
	 var bdrnk_womanord = $('#bdrnk_womanord')
	 
	 new Chart(bdrnk_womanord, {
	    type: 'bar',
	    data: {
	      labels: nbdrnkarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmordbdrnkarray, 
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

	 //구매기반디저트취향(전체)
	 var bdsrtcount = $('#bdsrt_list').text()
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
	 
	//남성구매기반디저트취향(10대)
	 var mteenbdsrtcount = $('#manteen_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var mteenbdsrtarray = mteenbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_manteen = $('#bdsrt_manteen')
	 
	 new Chart(bdsrt_manteen, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mteenbdsrtarray, 
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
	 
	//남성구매기반디저트취향(20대)
	 var mtwebdsrtcount = $('#mantwe_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var mtwebdsrtarray = mtwebdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_mantwe = $('#bdsrt_mantwe')
	 
	 new Chart(bdsrt_mantwe, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mtwebdsrtarray, 
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
	 
	//남성구매기반디저트취향(30대)
	 var mthrbdsrtcount = $('#manthr_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var mthrbdsrtarray = mthrbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_manthr = $('#bdsrt_manthr')
	 
	 new Chart(bdsrt_manthr, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mthrbdsrtarray, 
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
	 
	//남성구매기반디저트취향(40대)
	 var mfoubdsrtcount = $('#manfou_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var mfoubdsrtarray = mfoubdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_manfou = $('#bdsrt_manfou')
	 
	 new Chart(bdsrt_manfou, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfoubdsrtarray, 
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
	 
	//남성구매기반디저트취향(50대)
	 var mfivbdsrtcount = $('#manfiv_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var mfivbdsrtarray = mfivbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_manfiv = $('#bdsrt_manfiv')
	 
	 new Chart(bdsrt_manfiv, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mfivbdsrtarray, 
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
	 
	//남성구매기반디저트취향(60대이상)
	 var mordbdsrtcount = $('#manord_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var mordbdsrtarray = mordbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_manord = $('#bdsrt_manord')
	 
	 new Chart(bdsrt_manord, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: mordbdsrtarray, 
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

	//여성구매기반디저트취향(10대)
	 var wmteenbdsrtcount = $('#womanteen_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var wmteenbdsrtarray = wmteenbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_womanteen = $('#bdsrt_womanteen')
	 
	 new Chart(bdsrt_womanteen, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmteenbdsrtarray, 
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
	 
	//여성구매기반디저트취향(20대)
	 var wmtwebdsrtcount = $('#womantwe_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var wmtwebdsrtarray = wmtwebdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_womantwe = $('#bdsrt_womantwe')
	 
	 new Chart(bdsrt_womantwe, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmtwebdsrtarray, 
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
	 
	//여성구매기반디저트취향(30대)
	 var wmthrbdsrtcount = $('#womanthr_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var wmthrbdsrtarray = wmthrbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_womanthr = $('#bdsrt_womanthr')
	 
	 new Chart(bdsrt_womanthr, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmthrbdsrtarray, 
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
	 
	//여성구매기반디저트취향(40대)
	 var wmfoubdsrtcount = $('#womanfou_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var wmfoubdsrtarray = wmfoubdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_womanfou = $('#bdsrt_womanfou')
	 
	 new Chart(bdsrt_womanfou, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfoubdsrtarray, 
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
	 
	//여성구매기반디저트취향(50대)
	 var wmfivbdsrtcount = $('#womanfiv_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var wmfivbdsrtarray = wmfivbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_womanfiv = $('#bdsrt_womanfiv')
	 
	 new Chart(bdsrt_womanfiv, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmfivbdsrtarray, 
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
	 
	//여성구매기반디저트취향(60대이상)
	 var wmordbdsrtcount = $('#womanord_bdslist').text()
	 var bdsrtname = $('#bdsrt_n').text()
	 
	 var wmordbdsrtarray = wmordbdsrtcount.replace("[","").replace("]","").split(',');
	 var nbdsrtarray = bdsrtname.replace("[","").replace("]","").split(',');
	 
	 var bdsrt_womanord = $('#bdsrt_womanord')
	 
	 new Chart(bdsrt_womanord, {
	    type: 'bar',
	    data: {
	      labels: nbdsrtarray, 
	      datasets: [{
	        label: '# of Votes',
	        data: wmordbdsrtarray, 
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
	 
	 //회원이탈
	 var eusercount = $('#list_exmaddi').text()
	 var euserday = $('#upwelyearlist').text()
	 
	 var wuserarray = eusercount.replace("[","").replace("]","").split(',');
	 var euserdayarray = euserday.replace("[","").replace("]","").split(',');

	 var exiao = $('#exiao')
	 
	 new Chart(exiao, {
	    type: 'line',
	    data: {
	      labels: euserdayarray, 
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
	 
	 //키워드 워드클라우드 - 전체사용자
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
	 
	 //키워드 워드클라우드 - 회원
	 var memdata_list = $('#memdata_list').text()
	 var memdataarray = memdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var memjsonData = memdataarray.replace(/'/g, '"');
	 var memdata = memjsonData.replace(/^"|"$/g, "");
	 var memvalidJsonString = memdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var memresultObject = JSON.parse(memvalidJsonString);
	 
	 var memwordCloudData = [];
	 
	 //형식에 맞게 출력
	 for (var i = 0; i < memresultObject.length; i++) {
            memwordCloudData.push({
                "x": memresultObject[i].x,
                "value": memresultObject[i].weight
            });
        }
        
	 // WordCloud를 생성하고 데이터를 설정
	 var chart = anychart.tagCloud(memwordCloudData);

	 // WordCloud가 그려질 컨테이너를 지정
	 chart.container("container_mem");
	 // 차트를 그림
	 chart.draw();

	 //키워드 워드클라우드 - 비회원
	 var nmemdata_list = $('#nmemdata_list').text()
	 var nmemdataarray = nmemdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var nmemjsonData = nmemdataarray.replace(/'/g, '"');
	 var nmemdata = nmemjsonData.replace(/^"|"$/g, "");
	 var nmemvalidJsonString = nmemdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var nmemresultObject = JSON.parse(nmemvalidJsonString);
	 
	 var nmemwordCloudData = [];
	 
	 //형식에 맞게 출력
	 for (var i = 0; i < nmemresultObject.length; i++) {
            nmemwordCloudData.push({
                "x": nmemresultObject[i].x,
                "value": nmemresultObject[i].weight
            });
        }
        
	 // WordCloud를 생성하고 데이터를 설정
	 var chart = anychart.tagCloud(nmemwordCloudData);

	 // WordCloud가 그려질 컨테이너를 지정
	 chart.container("container_nmem");
	 // 차트를 그림
	 chart.draw();

	 //키워드 워드클라우드 - 남성10대
	 var manteen_list = $('#manteen_list').text()
	 var mteendataarray = manteen_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mteenjsonData = mteendataarray.replace(/'/g, '"');
	 var mteendata = mteenjsonData.replace(/^"|"$/g, "");
	 var mteenvalidJsonString = mteendata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mteenresultObject = JSON.parse(mteenvalidJsonString);
	 
	 var mteenwordCloudData = [];
	 
	 for (var i = 0; i < mteenresultObject.length; i++) {
            mteenwordCloudData.push({
                "x": mteenresultObject[i].x,
                "value": mteenresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mteenwordCloudData);
	 chart.container("container_manteen");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성20대
	 var mtwedata_list = $('#mantwe_list').text()
	 var mtwedataarray = mtwedata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mtwejsonData = mtwedataarray.replace(/'/g, '"');
	 var mtwedata = mtwejsonData.replace(/^"|"$/g, "");
	 var mtwevalidJsonString = mtwedata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mtweresultObject = JSON.parse(mtwevalidJsonString);
	 
	 var mtwewordCloudData = [];
	 
	 for (var i = 0; i < mtweresultObject.length; i++) {
            mtwewordCloudData.push({
                "x": mtweresultObject[i].x,
                "value": mtweresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mtwewordCloudData);
	 chart.container("container_mantwe");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성30대
	 var mthrdata_list = $('#manthr_list').text()
	 var mthrdataarray = mthrdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mthrjsonData = mthrdataarray.replace(/'/g, '"');
	 var mthrdata = mthrjsonData.replace(/^"|"$/g, "");
	 var mthrvalidJsonString = mthrdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	 var mthrresultObject = JSON.parse(mthrvalidJsonString);
	 var mthrwordCloudData = [];
	 
	 for (var i = 0; i < mthrresultObject.length; i++) {
            mthrwordCloudData.push({
                "x": mthrresultObject[i].x,
                "value": mthrresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mthrwordCloudData);
	 chart.container("container_manthr");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성40대
	 var mfoudata_list = $('#manfou_list').text()
	 var mfoudataarray = mfoudata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mfoujsonData = mfoudataarray.replace(/'/g, '"');
	 var mfoudata = mfoujsonData.replace(/^"|"$/g, "");
	 var mfouvalidJsonString = mfoudata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mfouresultObject = JSON.parse(mfouvalidJsonString);
	 
	 var mfouwordCloudData = [];
	 
	 for (var i = 0; i < mfouresultObject.length; i++) {
            mfouwordCloudData.push({
                "x": mfouresultObject[i].x,
                "value": mfouresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mfouwordCloudData);
	 chart.container("container_manfou");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성50대
	 var mfivdata_list = $('#manfiv_list').text()
	 var mfivdataarray = mfivdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mfivjsonData = mfivdataarray.replace(/'/g, '"');
	 var mfivdata = mfivjsonData.replace(/^"|"$/g, "");
	 var mfivvalidJsonString = mfivdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mfivresultObject = JSON.parse(mfivvalidJsonString);
	 var mfivwordCloudData = [];
	 
	 for (var i = 0; i < mfivresultObject.length; i++) {
            mfivwordCloudData.push({
                "x": mfivresultObject[i].x,
                "value": mfivresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mfivwordCloudData);
	 chart.container("container_manfiv");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성60대이상
	 var morddata_list = $('#manord_list').text()
	 var morddataarray = morddata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mordjsonData = morddataarray.replace(/'/g, '"');
	 var morddata = mordjsonData.replace(/^"|"$/g, "");
	 var mordvalidJsonString = morddata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mordresultObject = JSON.parse(mordvalidJsonString);
	 
	 var mordwordCloudData = [];

	 for (var i = 0; i < mordresultObject.length; i++) {
            mordwordCloudData.push({
                "x": mordresultObject[i].x,
                "value": mordresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mordwordCloudData);
	 chart.container("container_manord");
	 chart.draw();	 	 	 	 	 	 
	 
	 //키워드 워드클라우드 - 여성10대
	 var womanteen_list = $('#womanteen_list').text()
	 var womteendataarray = womanteen_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womteenjsonData = womteendataarray.replace(/'/g, '"');
	 var womteendata = womteenjsonData.replace(/^"|"$/g, "");
	 var womteenvalidJsonString = womteendata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womteenresultObject = JSON.parse(womteenvalidJsonString);
	 
	 var womteenwordCloudData = [];
	 
	 for (var i = 0; i < womteenresultObject.length; i++) {
            womteenwordCloudData.push({
                "x": womteenresultObject[i].x,
                "value": womteenresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womteenwordCloudData);
	 chart.container("container_womanteen");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성20대
	 var womtwedata_list = $('#womantwe_list').text()
	 var womtwedataarray = womtwedata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womtwejsonData = womtwedataarray.replace(/'/g, '"');
	 var womtwedata = womtwejsonData.replace(/^"|"$/g, "");
	 var womtwevalidJsonString = womtwedata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womtweresultObject = JSON.parse(womtwevalidJsonString);
	 
	 var womtwewordCloudData = [];
	 
	 for (var i = 0; i < womtweresultObject.length; i++) {
            womtwewordCloudData.push({
                "x": womtweresultObject[i].x,
                "value": womtweresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womtwewordCloudData);
	 chart.container("container_womantwe");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성30대
	 var womthrdata_list = $('#womanthr_list').text()
	 var womthrdataarray = womthrdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womthrjsonData = womthrdataarray.replace(/'/g, '"');
	 var womthrdata = womthrjsonData.replace(/^"|"$/g, "");
	 var womthrvalidJsonString = womthrdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womthrresultObject = JSON.parse(womthrvalidJsonString);
	 
	 var womthrwordCloudData = [];
	 
	 for (var i = 0; i < womthrresultObject.length; i++) {
            womthrwordCloudData.push({
                "x": womthrresultObject[i].x,
                "value": womthrresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womthrwordCloudData);
	 chart.container("container_womanthr");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성40대
	 var womfoudata_list = $('#womanfou_list').text()
	 var womfoudataarray = womfoudata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womfoujsonData = womfoudataarray.replace(/'/g, '"');
	 var womfoudata = womfoujsonData.replace(/^"|"$/g, "");
	 var womfouvalidJsonString = womfoudata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womfouresultObject = JSON.parse(womfouvalidJsonString);
	 
	 var womfouwordCloudData = [];
	 
	 for (var i = 0; i < womfouresultObject.length; i++) {
            womfouwordCloudData.push({
                "x": womfouresultObject[i].x,
                "value": womfouresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womfouwordCloudData);
	 chart.container("container_womanfou");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성50대
	 var womfivdata_list = $('#womanfiv_list').text()
	 var womfivdataarray = womfivdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womfivjsonData = womfivdataarray.replace(/'/g, '"');
	 var womfivdata = womfivjsonData.replace(/^"|"$/g, "");
	 var womfivvalidJsonString = womfivdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womfivresultObject = JSON.parse(womfivvalidJsonString);
	 var womfivwordCloudData = [];
	 
	 for (var i = 0; i < womfivresultObject.length; i++) {
            womfivwordCloudData.push({
                "x": womfivresultObject[i].x,
                "value": womfivresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womfivwordCloudData);
	 chart.container("container_womanfiv");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성60대이상
	 var womorddata_list = $('#womanord_list').text()
	 var womorddataarray = womorddata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womordjsonData = womorddataarray.replace(/'/g, '"');
	 var womorddata = womordjsonData.replace(/^"|"$/g, "");
	 var womordvalidJsonString = womorddata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womordresultObject = JSON.parse(womordvalidJsonString);
	 
	 var womordwordCloudData = [];

	 for (var i = 0; i < womordresultObject.length; i++) {
            womordwordCloudData.push({
                "x": womordresultObject[i].x,
                "value": womordresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womordwordCloudData);
	 chart.container("container_womanord");
	 chart.draw();	 	 
 })