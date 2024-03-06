class Usuario:
    # Método de inicialização (construtor)
    def __init__(self, nome, idade, genero, turma):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.turma = turma

    # Método para mostrar informações do usuário
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Genero: {self.genero}")
        print(f"Turma: {self.turma}")
        print()

# Criar objetos
usuario1 = Usuario("Lara", 17, "Feminino", "1Pi")
usuario2 = Usuario("Alexandre", 16, "Masculino", "2Pi")
usuario3 = Usuario("Rodrigo", 16, "Indefinido", "2Pi")
usuario4 = Usuario("Pedro", 18, "Masculino", "3Pi")

# Usar polimorfismo para mostrar informações
usuarios = [usuario1, usuario2, usuario3, usuario4]

# Iteração da lista de usuários
for usuario in usuarios:
    # Chamar o método mostrar_informacoes, o qual funciona de maneira polimórfica
    usuario.mostrar_informacoes()
