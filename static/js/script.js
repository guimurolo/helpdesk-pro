console.log("HelpDesk Pro - JavaScript conectado!");

const formulario = document.getElementById("form-chamado");

const mensagem = document.getElementById("mensagem");

function exibirMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = tipo;
}

console.log("Formulário encontrado:", formulario);

formulario.addEventListener("submit", async function(event) {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value.trim();
    if (titulo === "") {
    exibirMensagem("Por favor, informe um título válido.", "mensagem-erro");
    return;

}
    const descricao = document.getElementById("descricao").value.trim();
    if (descricao === "") {
    exibirMensagem("Por favor, informe uma descrição válida.", "mensagem-erro");
    return;
}

    const prioridade = document.getElementById("prioridade").value;

try {
    const response = await fetch("/chamados", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            titulo: titulo,
            descricao: descricao,
            prioridade: prioridade
        })
    });

    const resultado = await response.json();

    if (!response.ok) {
    console.error("Erro retornado pela API:", resultado);
    exibirMensagem("Não foi possível criar o chamado. Verifique os dados.", "mensagem-erro");
    return;
}

    console.log("Chamado criado:", resultado);
    exibirMensagem(resultado.mensagem, "mensagem-sucesso");

    formulario.reset();

} catch (error) {
    console.error("Erro de comunicação:", error);
    exibirMensagem("Não foi possível conectar ao servidor. Tente novamente.", "mensagem-erro");
}


});
