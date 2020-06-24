function ValidarCPF(Objcpf){
  var cpf = Objcpf.value;
  exp = /\.|\-/g
  cpf = cpf.toString().replace( exp, "" );
  var digitoDigitado = eval(cpf.charAt(9)+cpf.charAt(10));
  var soma1=0, soma2=0;
  var vlr =11;

  for(i=0;i<9;i++){
          soma1+=eval(cpf.charAt(i)*(vlr-1));
          soma2+=eval(cpf.charAt(i)*vlr);
          vlr--;
  }
  soma1 = (((soma1*10)%11)==10 ? 0:((soma1*10)%11));
  soma2=(((soma2+(2*soma1))*10)%11);

  var digitoGerado=(soma1*10)+soma2;
  if(digitoGerado!=digitoDigitado ||
        cpf == "00000000000" ||
        cpf == "11111111111" ||
        cpf == "22222222222" ||
        cpf == "33333333333" ||
        cpf == "44444444444" ||
        cpf == "55555555555" ||
        cpf == "66666666666" ||
        cpf == "77777777777" ||
        cpf == "88888888888" ||
        cpf == "99999999999"){
          alert('CPF Invalido!');
          document.getElementById('cpf').value = ""
          return false;
  }
  else
        return true;
}
