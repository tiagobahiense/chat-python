var email = "user1@email.com"
var password = "1234"

function login() {
    const emailUser = document.getElementById("email").value;
    const passwordUser = document.getElementById("password").value;

    if(emailUser ==="" || password ==="") {
        alert("Preencha todos os campos.")
    } else if(emailUser === email && passwordUser === password) {
        location.href ="/chat.html"
    } else {
        alert("Email ou senha inválidos.")
    }
}