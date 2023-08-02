$(function(){
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
})