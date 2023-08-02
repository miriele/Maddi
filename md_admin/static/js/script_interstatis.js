$(function(){
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

})