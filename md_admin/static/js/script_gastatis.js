$(function(){
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
	 
	 //남성회원 연령대 분포
	 var managecount = $('#man_agecount').text()
	 var manarrayage = managecount.replace("[","").replace("]","").split(',');
	 
	 var gender_man = $('#gender_man')
	 
	 new Chart(gender_man, {
	    type: 'bar',
	    data: {
	      labels: ['10대','20대','30대','40대','50대','60대이상'],
	      datasets: [{
	        label: '# of Votes',
	        data: manarrayage, 
	        borderWidth: 1,
	        borderColor: '#36A2EB',
	        backgroundColor: '#9BD0F5',
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
	 
	 //여성회원 연령대 분포
	 var womanagecount = $('#woman_agecount').text()
	 var womanarrayage = womanagecount.replace("[","").replace("]","").split(',');
	 
	 var gender_woman = $('#gender_woman')
	 
	 new Chart(gender_woman, {
	    type: 'bar',
	    data: {
	      labels: ['10대','20대','30대','40대','50대','60대이상'],
	      datasets: [{
	        label: '# of Votes',
	        data: womanarrayage, 
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
})