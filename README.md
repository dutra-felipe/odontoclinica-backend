# 🦷 OdontoClínica - Backend

Back-end do sistema de gestão para clínicas odontológicas, desenvolvido com **Django** e **PostgreSQL**, containerizado com **Docker**. Permite o gerenciamento completo de pacientes, dentistas, consultas, prontuários, tratamentos, pagamentos e agendas.

## 🚀 Tecnologias
- [Python 3.12](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker + Docker Compose](https://docs.docker.com/compose/)
- [Django REST Framework](https://www.django-rest-framework.org/) (opcional, para API)

## 📁 Estrutura do Projeto
```
odontoclinica-backend/
├── odontoclinica/    # Projeto Django (configurações)
├── core/             # Aplicações (pacientes, dentistas, consultas, etc.)
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── .env
```

## ⚙️ Configuração com Docker

### 1. Crie o arquivo `.env`:
```env
DB_NAME=odontoclinica
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### 2. Suba os containers:
```bash
docker-compose up --build
```

Acesse: http://localhost:8000

## 🛠️ Comandos úteis

### Migrar o banco de dados
```bash
docker-compose exec web python manage.py migrate
```

### Criar superusuário
```bash
docker-compose exec web python manage.py createsuperuser
```

### Acessar o shell Django
```bash
docker-compose exec web python manage.py shell
```

## 🔐 Acesso ao Admin
Após criar um superusuário, acesse:
http://localhost:8000/admin

## ✅ Funcionalidades planejadas
- Cadastro de usuários (admin, recepção, dentistas)
- Gerenciamento de pacientes e convênios
- Controle de consultas e agendamentos
- Prontuários com anotações e imagens
- Tratamentos e orçamentos
- Pagamentos e status
- Agenda personalizada por dentista

## 🤝 Contribuindo
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request
