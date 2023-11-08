#QUESTÃO 1
import bcrypt
import secrets
 
chaveSecreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
 
def gerar_senha_aleatoria():
    return secrets.token_urlsafe(16)
 
senha1 = gerar_senha_aleatoria() + chaveSecreta
senha2 = gerar_senha_aleatoria() + chaveSecreta
senha3 = gerar_senha_aleatoria() + chaveSecreta
 
senha_criptografada1 = bcrypt.hashpw(senha1.encode('utf-8'), bcrypt.gensalt())
senha_criptografada2 = bcrypt.hashpw(senha2.encode('utf-8'), bcrypt.gensalt())
senha_criptografada3 = bcrypt.hashpw(senha3.encode('utf-8'), bcrypt.gensalt())
 
print(senha_criptografada1)
print(senha_criptografada2)
print(senha_criptografada3)
