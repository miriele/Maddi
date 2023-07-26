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
	
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });		 			 		
 })