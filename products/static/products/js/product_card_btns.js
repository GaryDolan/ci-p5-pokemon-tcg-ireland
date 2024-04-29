function enableButtons() {
    // Enable all buttons with the class add_to_basket_btn
    var buttons = document.getElementsByClassName("add-btn");
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = false;
    }
}  

function disableButtons() {
    // Disable all buttons with the class add_to_basket_btn
    var buttons = document.getElementsByClassName("add-btn");
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = true;
    }
}

window.onload = function() {
    enableButtons();
    var forms = document.getElementsByClassName("add-product-form");
    for (let i = 0; i < forms.length; i++) {
        forms[i].addEventListener("submit", function() {
            disableButtons();
        });
    }
};