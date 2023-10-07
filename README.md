# Jornada_Milhas
Projeto feito durante o mês do desafio Challenge#7 BackEnd da Alura.

# API REST com DJANGO REST FRAMEWORK - Challenge Back-End 7 Alura

Este é um projeto de API REST desenvolvida com Django Rest para disponibilizar informações e recursos relacionados a possíveis destinos de viagem, exibindo fotos, textos e depoimentos de outras pessoas viajantes.

# Descrição do Desafio

O desafio proposto é a construção de uma API para gerenciar depoimentos de viagens, permitindo cadastrar novos depoimentos, buscar depoimentos existentes, atualizar e remover depoimentos. Além disso, há um endpoint adicional para obter três depoimentos aleatórios.

## Tecnologias Utilizadas

- Linguagem de Programação: Python
- Framework: Django Rest
- Banco de Dados: SQlite

## Documentação da API
A documentação da API (swagger) esta disponível na rota /swagger/
![image](https://github.com/jotapn/challenge-backend-7-edicao/assets/113472310/825b2fe5-5d22-4e6b-84cf-2c27cfff9a73)


# Funcionalidades
## Depoimentos
- `Cadastrar`: Cadastrar depoimentos através de um `POST /depoimentos/`.

- `Buscar todos`: Busca paginada de todos os depoimentos através de um `GET /depoimentos/`.

- `Buscar por id`: Busca depoimento por ID através de um `GET /depoimentos/{ID}/`, onde *{ID}* é o identificador do depoimento.

- `Atualizar`: Atualizar depoimento através de um `PATCH /depoimentos/{ID}/`, onde *ID* é o identificador do depoimento,
  os novos dados do depoimento devem ser enviados no corpo da requisição.

- `Deletar`: Deletar depoimento através de um `DELETE /depoimentos/{ID}`, onde *{ID}* é o identificador do depoimento.

## Endpoints de Depoimentos

A API oferece os seguintes endpoints para depoimentos:

### Endpoint de Cadastro de Depoimentos

`POST /depoimentos`

Ultilizar este verbo Http (POST) permite cadastrar um novo depoimento. O corpo da requisição deve conter um objeto JSON com os seguintes campos obrigatórios: "nome" (nome do autor do depoimento), "depoimento" (texto do depoimento) e "foto" (URL da foto do autor).

Exemplo de requisição:

```json
{
  "foto": "url_de_imagem.jpg"
  "nome": "Autor da Silva",
  "depoimento": "Um depoimento pessoal.",
}
```

### Endpoint que retorna todos os depoimentos

`GET /depoimentos`

Ultilizar este verbo Http (GET) retorna uma lista contendo todos os depoimentos cadastrados. O corpo da resposta retornada vai conter uma lista de objetos JSON contendo os seguintes campos: "id" (um integer com a indentificação unica do objeto), "nome" (nome do autor do depoimento), "foto" (URL da foto do autor) e "depoimento" (texto do depoimento). 

Exemplo do corpo da resposta:

```json
[
  {
      "id": 1,
      "foto": "../media/depoimentos/Fulano.jpg",
      "nome": "Fulano",
      "depoimento": "Depoimento de Fulano"
  },
  {
      "id": 2,
      "foto": "../media/depoimentos/Cicrano.jpg",
      "nome": "Cicrano",
      "depoimento": "Depoimento de Cicrano"
  },
]
```
### Endpoint para atualização de um depoimento

`PUT /depoimentos`

Ultilizar este verbo Http (PUT) permite atualizar algumas informações de um depoimento através do ID fornecido no corpo da requisição. A requisição deve ser um objeto JSON contendo obrigatoriamente o ID do depoimento que deve ser alterado. Os campos que podem ser alterados são: "nome" (nome do autor do depoimento), "depoimento" (texto do depoimento) e "foto" (URL da foto do autor).

Exemplo de requisição:

```json
{
  "id": 1,
  "foto": "campo opcional"
  "nome": "campo opcional",
  "depoimento": "campo opcional",
}
```
### Endpoint de remoção de depoimento

`DELETE /depoimentos/{id}`

Ultilizar este verbo Http (DELETE) permite remover um depoimento pelo seu ID. A resposta será um codigo 204 (NO_CONTENT) como confirmação de que aquele depoimento não existe mais.

Exemplo de requisição:

`DELETE /depoimentos/1`


### Endpoint adicional: Depoimentos aleatórios

`GET /depoimentos-home`

Ultilizar este verbo Http (GET) retorna até três depoimentos selecionados aleatoriamente no corpo da resposta que será uma lista de objetos JSON.

Exemplo da resposta:

```json
[
  {
    "id": 5,
    "foto": "../media/depoimentos/Fulano.jpg",
    "nome": "Fulano",
    "depoimento": "Depoimento de Fulano"
  },
  {
    "id": 4,
    "foto": "../media/depoimentos/Cicrano.jpg",
    "nome": "Cicrano",
    "depoimento": "Depoimento de Cicrano"
  },
  {
    "id": 7,
    "foto": "../media/depoimentos/Beltrano.jpg",
    "nome": "Beltrano",
    "depoimento": "Depoimento de Beltrano"
  }
]
```
## Endpoints de Destinos

A API oferece os seguintes endpoints para destinos:

### Endpoint de Cadastro de Destinos

`POST /destinos`

Ultilizar este verbo Http (POST) permite cadastrar um novo depoimento. O corpo da requisição deve conter um objeto JSON com os seguintes campos obrigatórios:
"nome" (nome do destino), "preco" (preço da viagem) e "foto" (URL da foto da cidade de destino).

Exemplo de requisição:

```json
{
    "foto": "../media/destinos/Sao_Paulo.jpg",
    "nome": "São Paulo",
    "preco": 1000.0
}
```

### Endpoint que retorna todos os destinos

`GET /destinos`

Ultilizar este verbo Http (GET) retorna uma lista contendo todos os destinos cadastrados. O corpo da resposta retornada vai conter uma lista de objetos JSON contendo os seguintes campos:
"id" (um integer com a indentificação unica do objeto), "nome" (nome do destino), "foto" (URL da foto do destino) e "preco" (preço da viagem). 

Exemplo do corpo da resposta:

```json
[
  {
      "id": 1,
      "foto": null,
      "nome": "../media/destinos/Sao_Paulo.jpg",
      "preco": 1000.0
  },
  {
      "id": 3,
      "foto": "http://127.0.0.1:8000/media/destinos/Teresina.jpeg",
      "nome": "Teresina",
      "preco": 100.0
  },
  {
      "id": 4,
      "foto": "http://127.0.0.1:8000/media/destinos/Rio_de_Janeiro.jpg",
      "nome": "Rio de Janeiro",
      "preco": 1200.0
  }
]
```
### Endpoint para atualização de um depoimento

`PUT /destinos`

Ultilizar este verbo Http (PUT) permite atualizar algumas informações de um destino através do ID fornecido no corpo da requisição. A requisição deve ser um objeto JSON contendo obrigatoriamente o ID do destino que deve ser alterado. Os campos que podem ser alterados são:
"nome" (nome do destino), "preco" (preço da viagem) e "foto" (URL da foto do destino).

Exemplo de requisição:

```json
{
  "id": 1,
  "foto": "campo opcional"
  "nome": "campo opcional",
  "preco": "campo opcional",
}
```
### Endpoint de remoção de destinos

`DELETE /destinos/{id}`

Ultilizar este verbo Http (DELETE) permite remover um destino pelo seu ID. A resposta será um codigo 204 (NO_CONTENT) como confirmação de que aquele destino não existe mais.

Exemplo de requisição:

`DELETE /destinos/3`


### Progresso de desenvolvimeto:

`Concluido`:

*PRIMEIRA SEMANA*:
- [x] CRUD de depoimentos;
- [x] Endpoint de /depoimento-home;
- [x] Configuração de CORS;
- [x] Testes do endpoint /depoimentos.

*SEGUNDA SEMANA*:
- [x] CRUD de destinos;
- [x] Endpoint de busca por /destinos;
- [x] Testes do endpoint /destinos.

`Em andamento`:

*TERCEIRA E QUARTA SEMANAS*: 
- [ ] Atualização do endpoint /destinos;
- [ ] Busca de destinos por ID;
- [ ] Integração com IA.
