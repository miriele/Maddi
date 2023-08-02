$(function(){
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
	
	
	
	
})