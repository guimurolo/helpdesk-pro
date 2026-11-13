console.log("HelpDesk Pro - JavaScript conectado!");

const formulario = document.getElementById("form-chamado");

console.log("Formulário encontrado:", formulario);

formulario.addEventListener("submit", function(event) {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value.trim();
    if (titulo === "") {
    alert("Por favor, informe um título válido para o chamado.");
    return;
}
    const descricao = document.getElementById("descricao").value.trim();
    if (descricao === "") {
    alert("Por favor, informe uma descrição válida para o chamado.");
    return;
}
    const prioridade = document.getElementById("prioridade").value;

    console.log("Título:", titulo);
    console.log("Descrição:", descricao);
    console.log("Prioridade:", prioridade);

    console.log("Formulário enviado!");
});