# Instalação 
	1.1 - Faça o download do Python 3.x -> https://www.python.org/downloads/
	1.2 - Intale o Django 3.x -> Abra o cmd e digite "pip install django==3.0.6"

# Criando usuário admin e acessando área de admin -> Nessa área, é possível ver todos os usuários cadastrados
	<br />
	2.1 - Abra o cmd na pasta raíz do projeto
	2.2 - Digite "python3 manage.py createsuperuser"
	2.3 - Insira o "username" e dê enter
	2.4 - Insira o "Email address" e dê enter
	2.5 - Insira o "Password" (deve ter no mínimo 8 caracteres) e dê enter
	2.6 - Repita o password e dê enter
	2.7 - Abra o browser e acesse http://localhost:8000/admin
	2.8 - Logue com o usuário criado
	
# Criando as migrações (Banco de dados)
	3.1 - Abra o cmd na pasta raíz do projeto
	3.2 - Digite "python3 manage.py makemigrations" e dê enter
	3.3 - Digite "python3 manage.py migrate" e dê enter

# Subindo o servidor
	4.1 - Entre na raiz do projeto
	4.2 - Inicie o servidor do django -> Abra o cmd e digite "python manage.py runserver"
	4.3 - Após rodar o projeto abra o browser e acesse http://localhost:8000/