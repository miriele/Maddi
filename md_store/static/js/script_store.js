//input 클릭하면 초기화
function clearInput(input) {
        input.value = '';
    }

function handleCateChange() {
    const cateSelect = document.getElementById("cate");
    const typedsrtSelect = document.getElementById("typedsrt");
    const typedrnkSelect = document.getElementById("typedrnk");
    const iceSelect = document.getElementById("ice");

    const selectedValue = parseInt(cateSelect.value);

    if (selectedValue === 1) {
      typedsrtSelect.style.display = "none";
      typedrnkSelect.style.display = "none";
      iceSelect.style.display = "none";
    } else if (selectedValue === 0) {
      typedsrtSelect.style.display = "inline-block";
      typedrnkSelect.style.display = "none";
      iceSelect.style.display = "none";
    } else if (selectedValue === -1) {
      typedsrtSelect.style.display = "none";
      typedrnkSelect.style.display = "inline-block";
      iceSelect.style.display = "inline-block";
    }
  }
  
  