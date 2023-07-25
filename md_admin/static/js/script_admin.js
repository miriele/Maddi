$(function() {
/*성별통계*/
	//var data = {{inwon}};
	//var labels = {{gender}};

	const ctx = document.getElementById('gender')

	
	//console.log("수:" + data)
	//console.log("남성:" + labels)
	
	new Chart(ctx, {
	    type: 'pie',
	    data: {
	      labels: ['남성','여성'], //labels
	      datasets: [{
	        label: '# of Votes',
	        data: [79,61], //data
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