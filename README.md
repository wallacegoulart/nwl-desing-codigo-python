# DesingDePython

Projeto de estudo desenvolvido com a Rocketseat para praticar conceitos de Python aplicados a uma API web com Flask, organização em camadas, uso de interfaces, factories e injeção de dependência.

## Sobre o projeto

A aplicação expõe três calculadoras diferentes por meio de endpoints REST. Cada uma recebe um tipo de payload e retorna um resultado específico, com tratamento de erros padronizado.

O projeto também inclui um exemplo separado de orientação a interfaces em [interface_raw.py](interface_raw.py), demonstrando o uso de uma classe abstrata para envio de notificações.

## Tecnologias utilizadas

- Python
- Flask
- NumPy
- Pytest

## Estrutura principal

```bash
src/
  calculators/
  drivers/
  errors/
  main/
```

- `calculators/`: regras de negócio das calculadoras.
- `drivers/`: implementações auxiliares, como acesso ao NumPy.
- `errors/`: tratamento de erros da API.
- `main/`: server, rotas e factories.

## Como executar o projeto

### 1. Instale as dependências

Como este repositório não possui `requirements.txt`, instale manualmente:

```bash
pip install flask numpy pytest
```

### 2. Execute a aplicação

```bash
python run.py
```

A API ficará disponível em `http://0.0.0.0:3000`.

### 3. Rode os testes

```bash
pytest
```

## Endpoints

### `POST /calculator/1`

Recebe um corpo com um número:

```json
{
  "number": 1
}
```

Resposta esperada:

```json
{
  "data": {
    "Calculator": 1,
    "result": 14.25
  }
}
```

### `POST /calculator/2`

Recebe uma lista de números:

```json
{
  "numbers": [2.12, 4.62, 1.32]
}
```

Resposta esperada:

```json
{
  "data": {
    "Calculator": 2,
    "result": 0.08
  }
}
```

### `POST /calculator/3`

Recebe uma lista de números:

```json
{
  "numbers": [1, 1, 1, 1, 1000]
}
```

Resposta esperada:

```json
{
  "data": {
    "Calculator": 3,
    "value": 159680.16,
    "sucess": true
  }
}
```

## Tratamento de erros

A API devolve erros estruturados para entradas inválidas:

- `422 Unprocessable Entity` quando o corpo da requisição está mal formatado.
- `400 Bad Request` quando a regra de negócio da calculadora 3 falha.
- `500 Internal Server Error` para erros inesperados.

## Observações

- O projeto usa factories para separar a criação das calculadoras.
- `Calculator2` e `Calculator3` recebem um driver baseado em NumPy por injeção de dependência.
- A rota principal está registrada no arquivo [src/main/server/server.py](src/main/server/server.py).

## Autor

Projeto de estudo para fins educacionais.
