info_contatos = {
    'nome': "",
    'telefone': 0,
    'email': ""
}

nome = input("\nNome completo do contato: ")
info_contatos['nome'] = nome

telefone = int(input("\nTelefone para contato: "))
info_contatos["telefone"] = telefone

email = input("\nEndereço de email: ")
info_contatos["email"] = email

for chave, valor in info_contatos.items():
    print(chave, valor)
