$(function() {
/*성별통계*/
	//hidden으로 인원수 리스트,성별이름리스트 불러오기
	var data = $('#inwon').text();
	var labels = $('#gend').text();
	
	//배열형태의 string을 array로 변환
	var arraydata = data.replace("[","").replace("]","").split(',');
	//console.log("수:" + arraydata)
	//배열형태의 string을 array로 변환
	var arraylabel = labels.replace("[","").replace("]","").split(',');
	//console.log("수:" + arraylabel)
	
	//console.log("수:" + data)
	//console.log("인원:" + labels)
	
	const gender = document.getElementById('gender')
	
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
	 
	 /*연령통계*/
	 var agecount = $('#agecount').text()
	 var arrayage = agecount.replace("[","").replace("]","").split(',');
	 
	 const age = document.getElementById('age')
	 
	 new Chart(age, {
	    type: 'pie',
	    data: {
	      labels: ['10대','20대','30대','40대','50대','60대이상'], //labels
	      datasets: [{
	        label: '# of Votes',
	        data: arrayage, //data
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