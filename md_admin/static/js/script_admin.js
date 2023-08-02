$(function() {
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
	 var euserday = $('#exlist').text()

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
	  
 })