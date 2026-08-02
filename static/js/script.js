// sign up field
const signUp = document.getElementById("signUp");
if (signUp) {
    signUp.addEventListener("submit", function (e) {
        let username = document.getElementById("username").value.trim();
        let password = document.getElementById("password").value;
        let confirm_password = document.getElementById("confirm_pass").value;
        let email = document.getElementById("email").value.trim();

        if (username === "") { 
            alert("Enter your username");
            e.preventDefault();
            return;
        }
        if (password.length < 8) {
            alert("Password must be at least 8 characters");
            e.preventDefault();
            return;
        }
        if (password !== confirm_password) {
            alert("Passwords do not match");
            e.preventDefault();
        }
        if (!email.includes("@")) {
            alert("Invalid email");
            e.preventDefault();
            return;
        }
    });
}

//search about books
const search = document.getElementById("Search");
if (search) {
    search.addEventListener("keyup", function () {
        let value = search.value.toLowerCase();
        let books = document.querySelectorAll(".Book");
        books.forEach(function(book){
            let title = book.innerText.toLowerCase();
            if(title.includes(value)){
                book.style.display = "block";
            }
            else{
                book.style.display = "none";
            }
        });
    });
}

//message to borrow book
const borrowButtons = document.querySelectorAll(".borrow");
borrowButtons.forEach(function(button){
    button.addEventListener("click",function(){
        alert(" The book borrowed is successfully");
    });
});

//message to return book
const returnButtons = document.querySelectorAll(".return");
returnButtons.forEach(function(button){
    button.addEventListener("click",function(){
        alert(" The book is returned successfully");
    });
});


