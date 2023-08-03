//input 클릭하면 초기화
function clearInput(input) {
        input.value = '';
    }
    
function clearInput(input) {
    input.value = '';
}

function plus() {
    var inputElement = document.querySelector('input[name="menu_name"]');
    var currentValue = parseInt(inputElement.value);
    if (!isNaN(currentValue)) {
        inputElement.value = currentValue + 1;
    } else {
        inputElement.value = 1;
    }
}

function minus() {
    var inputElement = document.querySelector('input[name="menu_name"]');
    var currentValue = parseInt(inputElement.value);
    if (!isNaN(currentValue) && currentValue > 1) {
        inputElement.value = currentValue - 1;
    } else {
        inputElement.value = 1;
    }
}

/*
document.addEventListener("DOMContentLoaded", function () {
	const incrementButton = document.getElementById("incrementButton");
	const bucknumInput = document.getElementById("bucknum");

	incrementButton.addEventListener("click", function () {
		let currentBucknum = parseInt(bucknumInput.value);
		currentBucknum += 1;
		bucknumInput.value = currentBucknum;
	});
});
*/

//메뉴 수량증가
function count_plus(){
	var num   = parseInt($("input[name=num]").val()) + 1;
	var price = parseInt($(".menu_price").text());
	
	$("input[name=num]").val(num);
	$("input[name=buck_num]").val(num);
	$("input[name=ordr_num]").val(num);
	$("#price_sum").text(price*num);
//	console.log(price);
//	console.log(num);
}

//메뉴 수량감소
function count_minus(){
	var num = parseInt($("input[name=num]").val()) - 1;
	var price = parseInt($(".menu_price").text());
	
	$("input[name=num]").val(num);
	$("input[name=buck_num]").val(num);
	$("input[name=ordr_num]").val(num);
	$("#price_sum").text(price*num);
	
//	console.log(num);
}
