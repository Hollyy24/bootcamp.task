
var burgerButton = document.querySelector(".nav_button");
var closeButton = document.querySelector(".close_nav");
var menu = document.querySelector(".menu");
var word = document.querySelector("#first_section");

burgerButton.addEventListener('click',function(){
    menu.classList.add("is_active");
    closeButton.classList.add("is_active");
})


closeButton.addEventListener('click',function(){
    menu.classList.remove("is_active");
    closeButton.classList.remove("is_active");
})


