function esconderMensagem(mensagemId) {
    var mensagem = document.getElementById(mensagemId);
    if (mensagem) {
        setTimeout(function() {
            mensagem.style.display = "none";
        }, 5000);
    }
}
esconderMensagem("msg-login");
esconderMensagem("msg-senha");
esconderMensagem("senha-errada-msg");
