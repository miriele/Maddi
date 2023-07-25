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
	
	const ctx = document.getElementById('gender')
	
	new Chart(ctx, {
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
	      scales: {
	        y: {
	          beginAtZero: true
	        }
	      }
	    }
	 });
 })