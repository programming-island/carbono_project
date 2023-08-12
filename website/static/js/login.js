document.getElementById("direciona-home").addEventListener("click", function(evento) {
    evento.preventDefault()

    var usuario = document.getElementById("usuario").value
    var senha = document.getElementById("senha").value

    var msgUsuario = document.getElementById("msg-login")
    var msgSenha = document.getElementById("msg-senha")

    if(usuario === "") {
        msgUsuario.style.display = "block"
        msgSenha.style.display = "none"

        setTimeout(function() {
            msgUsuario.style.display = "none"
        }, 10000) //tempo para sumir a mensagem
    }
    else if(senha === "") {
        msgSenha.style.display = "block"
        msgUsuario.style.display = "none"

        setTimeout(function() {
            msgSenha.style.display = "none"
        }, 10000)
    }
})

