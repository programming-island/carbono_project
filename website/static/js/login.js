document.getElementById("form-login").addEventListener("submit", function(evento) {
    evento.preventDefault()

    var usuario = document.getElementById("usuario").value
    var senha = document.getElementById("senha").value

    var msgUsuario = document.getElementById("msg-login")
    var msgSenha = document.getElementById("msg-senha")

    if(usuario === "") {
        msgUsuario.style.display = "block"

        setTimeout(function() {
            msgUsuario.style.display = "none"
        }, 10000) //tempo para sumir a mensagem
    }
    
})

