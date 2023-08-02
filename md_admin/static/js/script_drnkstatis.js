$(function() {
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
})