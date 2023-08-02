$(function(){
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
})