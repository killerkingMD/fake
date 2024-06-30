import random
from faker import Faker

fake = Faker()

# Função para gerar um CPF válido
def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcular o primeiro dígito verificador
    soma = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    cpf.append((soma * 10) % 11 % 10)

    # Calcular o segundo dígito verificador
    soma = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    cpf.append((soma * 10) % 11 % 10)

    # Formatar o CPF (XXX.XXX.XXX-XX)
    cpf_formatado = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)

    return cpf_formatado

# Gerar dados completos
cpf = gerar_cpf()
nome = fake.name()
data_nascimento = fake.date_of_birth().strftime('%d/%m/%Y')
celular = fake.phone_number()
cep = fake.postcode()
endereco = fake.address()

# Imprimir os dados gerados
print("CPF:", cpf)
print("Nome:", nome)
print("Data de Nascimento:", data_nascimento)
print("Celular:", celular)
print("CEP:", cep)
print("Endereço:", endereco)
