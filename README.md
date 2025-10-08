# 🌐 Projeto Flask — Aplicação com deploy no Render

Aplicação web minimalista construída com **Python (Flask)** para demonstrar:
- estrutura de projeto,
- renderização de páginas HTML com templates,
- criação de rotas (incluindo uma API JSON),
- e **deploy em produção** no **Render.com** usando **Gunicorn**.

> **Importante:** esta aplicação é **exemplificativa e estática**. Os botões/cards da home são **elementos visuais** (UI) para simular um site real, mas **não executam ações**.  
> O foco é arquitetura, design e deploy.

---

## 🚀 Tecnologias & Serviços
- **Backend:** Python 3.11 · Flask · Gunicorn  
- **Frontend:** HTML + CSS 
- **Hospedagem/CI:** Render.com (Web Service conectado ao GitHub)  
- **Outros:** Git/GitHub, ambiente virtual (`venv`)

---

## 🔗 Demo online
Acesse: **https://flask-projeto-myriam.onrender.com/**

Rotas úteis:
- `/` — página inicial estilizada (estática)  
- `/api` — resposta **JSON** de exemplo  
- `/health` — verificação simples (retorna `ok`)

---

## 🧭 Funcionalidades
- Página inicial com UI moderna (tema azul/violeta/dourado)  
- API JSON de demonstração  
- Rota de saúde para monitoramento  
- Deploy automatizado via GitHub → Render  

---

## 🎯 Objetivo do Projeto
Este projeto foi desenvolvido com fins **educacionais** para demonstrar:
- Estruturação de aplicações Flask;
- Renderização de templates HTML;
- Criação de rotas e endpoints;
- Deploy completo em ambiente real (Render.com).

---

## 🧩 Como rodar localmente
```bash
# 1) Clonar
git clone https://github.com/MyriamHeusi/render_projeto.git
cd render_projeto

# 2) Criar e ativar venv
# Windows
python -m venv venv_render
venv_render\Scripts\activate

# Mac/Linux
# python3 -m venv venv_render
# source venv_render/bin/activate

# 3) Instalar dependências
pip install -r requirements.txt

# 4) Executar
python app.py
