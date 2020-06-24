function salvaDados() {

  // If sessionStorage is storing default values (ex. name), exit the function and do not restore data
  if (sessionStorage.getItem('nome') == "nome") {
      return;
  }

  // If values are not blank, restore them to the fields
  var name = sessionStorage.getItem('nome');
  if (name !== null) $('#inputNome').val(nome);

  var email = sessionStorage.getItem('cpf');
  if (email !== null) $('#cpf').val(cpf);

  var subject= sessionStorage.getItem('sexo');
  if (subject!== null) $('#slctSexo').val(sexo);

  var message= sessionStorage.getItem('depto');
  if (message!== null) $('#slctDepto').val(message);

  var message= sessionStorage.getItem('admissao');
  if (message!== null) $('#inputAdmissao').val(message);

  var message= sessionStorage.getItem('cargo');
  if (message!== null) $('#inputCargo').val(message);

  var message= sessionStorage.getItem('salario');
  if (message!== null) $('#dinheiro').val(message);

  window.onbeforeunload = function() {
    sessionStorage.setItem("nome", $('#inputNome').val());
    sessionStorage.setItem("cpf", $('#cpf').val());
    sessionStorage.setItem("sexo", $('#slctSexo').val());
    sessionStorage.setItem("depto", $('#slctDepto').val());
    sessionStorage.setItem("admissao", $('#inputAdmissao').val());
    sessionStorage.setItem("cargo", $('#inputCargo').val());
    sessionStorage.setItem("salario", $('#dinheiro').val());
}
}