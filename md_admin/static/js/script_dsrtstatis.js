$(function() {
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

})