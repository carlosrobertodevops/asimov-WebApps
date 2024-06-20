![6 (1)](https://user-images.githubusercontent.com/63136680/171276102-ae1e1aa3-42b6-4c2e-8251-4e66ee9871f4.jpg)


# MyBudget

Projeto de um app web de análise financeira pessoal usando apenas Python com base de dados no computador do usuário.

## 🔧 Funções

- Coletar e armazenar receitas do usuário
- Coletar e armazenar despesas do usuário
- Dispor de uma página de Dashboards para análise visual sobre os dados fornecidos
- Dispor de uma página de extratos, para que possa visualizar os dados de forma mais minuciosa e completa

## 💻 Projeto
Para ver as aulas do desenvolvimento do projeto completo em vídeo:

<a href = "https://asimov.academy/courses/dashboards-interativos-com-python/licoes/web-app-de-analise-financeira/"><img src="https://img.shields.io/badge/ASIMOV-Aulas%20do%20projeto-lightgrey" target="_blank"></a> 

Para ver o projeto em tempo real:

<a href = "https://my-budget-dash.herokuapp.com/"><img src="https://img.shields.io/badge/ASIMOV-Projeto%20em%20tempo%20real-lightgrey" target="_blank"></a>

## 👨‍💻 Tecnologias Utilizadas

Utilizando apenas **PYTHON** e as bibliotecas:
> - Dash
> - Dash-Core-Components
> - Dash HTML
> - Dash Bootstrap
> - Plotly
> - Pandas



## 📜 Conteúdo
Para aprender mais sobre como desenvolver projetos de Data Science, AI, Criação de Web Apps e Dashboards, acesse:

<a href = "https://asimov.academy/"><img src="https://img.shields.io/badge/ASIMOV-Saiba%20Mais-lightgrey" target="_blank"></a> 

### 🤝 Suporte/Contato


[![Whatsapp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5551981830833)
[![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/asimov.academy/)
[![Discord Badge](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/W2Nc7bxvk7)


## 👨‍💻 Tecnologias Utilizadas - conda

Para instalar dependências listadas em um arquivo `requirements.txt` usando `conda`, você pode seguir um dos métodos abaixo:

### Método 1: Converter `requirements.txt` para um ambiente Conda

1. **Criar um novo ambiente Conda** (opcional):
   ```bash
   conda create -n meu_ambiente python=3.8
   conda activate meu_ambiente
   ```

2. **Instalar as dependências usando `pip`**:
   ```bash
   pip install -r requirements.txt
   ```
   Essa abordagem instala pacotes usando `pip` dentro de um ambiente Conda.

3. **Exportar o ambiente** para um arquivo YAML (opcional):
   ```bash
   conda env export > environment.yml
   ```

### Método 2: Instalar diretamente com Conda (para pacotes disponíveis no Conda)

Se os pacotes no `requirements.txt` estão disponíveis no Conda, você pode:

1. **Converter `requirements.txt` para um arquivo YAML**:
   - Você pode manualmente converter os pacotes de `requirements.txt` para um `environment.yml` listando os pacotes assim:
     ```yaml
     name: meu_ambiente
     dependencies:
       - python=3.8
       - pacote1
       - pacote2
       - ...
     ```

2. **Criar o ambiente Conda com o YAML**:
   ```bash
   conda env create -f environment.yml
   ```

### Método 3: Usar `conda install` diretamente para pacotes principais

1. **Instalar pacotes listados** em `requirements.txt` usando `conda install`:
   ```bash
   conda install --file requirements.txt
   ```
   Note que isso funciona apenas para pacotes que estão disponíveis nos canais Conda.

### Exemplo de Arquivo YAML

Se você tiver um arquivo `requirements.txt` como este:

```txt
numpy==1.21.2
pandas==1.3.3
scipy==1.7.1
```

Você pode converter para `environment.yml`:

```yaml
name: meu_ambiente
channels:
  - defaults
dependencies:
  - python=3.8
  - numpy=1.21.2
  - pandas=1.3.3
  - scipy=1.7.1
```

E então criar o ambiente:

```bash
conda env create -f environment.yml
```

### Resumo

1. **Usar `pip install -r requirements.txt` dentro de um ambiente Conda**.
2. **Converter `requirements.txt` para `environment.yml`** e criar um ambiente Conda diretamente.

Escolha o método que melhor se adapta às suas necessidades e aos pacotes que você está usando.

✉ contato@asimov.academy

<p align="center">Copyright © 2022 Asimov Academy</p>
