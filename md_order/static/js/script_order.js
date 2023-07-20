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