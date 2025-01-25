# gerenciadorPokemonNoSQL

O **gerenciadorPokemonNoSQL** é um projeto desenvolvido para importar, processar e organizar dados contidos em arquivos JSON, armazenando-os eficientemente em um banco de dados MongoDB. Ele é ideal para cenários em que é necessário estruturar dados, gerenciar relações e evitar duplicatas durante o armazenamento.

---

## **Principais Funcionalidades**

1. **Leitura e processamento de dados JSON**:
   - Lê dados de um arquivo JSON contendo informações sobre entidades relacionadas, como nome, tipos, habilidades, habitat e evoluções.

2. **Armazenamento organizado no MongoDB**:
   - Insere ou atualiza informações em coleções distintas para manter os dados estruturados e relacionáveis:
     - **`pokemons`**: Dados principais de cada entidade (ex.: ID, nome, peso, altura, habilidades, tipos, habitat e evoluções).
     - **`types`**: Tipos únicos relacionados à entidade (ex.: fogo, água, elétrico).
     - **`abilities`**: Habilidades únicas (ex.: Levitate, Overgrow).
     - **`habitats`**: Habitats únicos (ex.: floresta, caverna).
     - **`evolutions`**: Relacionações de evolução entre as entidades.

3. **Manutenção da integridade dos dados**:
   - Evita duplicatas utilizando operações como `upsert` no MongoDB, que insere ou atualiza documentos conforme necessário.

4. **Criação de relações**:
   - Gerencia relações complexas, como evoluções, vinculando entidades através de seus IDs.

---

## **Configuração e Execução**

### **Pré-requisitos**
- Python 3.8 ou superior.
- MongoDB rodando localmente ou em um servidor remoto.
- Dependências Python:
  - `pymongo`
  - `python-dotenv`

### **Instalação**

1. Clone o repositório:

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env` com as credenciais do MongoDB:
   ```env
   MONGODB_URI=mongodb+srv://usuario:senha@cluster.mongodb.net
   MONGODB_DB_NAME=seu_banco
   ```

### **Execução**

1. Certifique-se de que o MongoDB está rodando corretamente.
2. Execute o script principal para importar os dados do JSON:
   ```bash
   python main.py
   ```
   Por padrão, o script irá processar o arquivo `lista_pokemon.json`. Caso utilize outro arquivo, atualize o caminho no código ou passe como argumento.

---

## **Estrutura de Arquivos**

- **`main.py`**: Script principal para leitura do JSON e inserção dos dados no MongoDB.
- **`lista_pokemon.json`**: Arquivo JSON com os dados a serem processados (exemplo fornecido).
- **`.env`**: Arquivo de configuração para credenciais do MongoDB (não incluído no repositório).
- **`requirements.txt`**: Lista de dependências Python do projeto.

---

## **Fluxo do Projeto**

1. **Leitura do JSON**:
   - O script lê os dados do arquivo JSON fornecido e os organiza para processamento.

2. **Processamento de dados**:
   - Verifica duplicatas nas coleções (`types`, `abilities`, `habitats`, `evolutions`).
   - Cria ou atualiza documentos relacionados com IDs exclusivos.

3. **Inserção no MongoDB**:
   - Os dados processados são armazenados no MongoDB de forma estruturada e eficiente.

---


