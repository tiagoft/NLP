# APS

## Parte 0: Um chatbot para o Discord

* O comando `\source` retorna um link para o repositório onde está o código-fonte do chatbot.
* O comando `\author` retorna o nome e e-mail do autor do chatbot.
* O chatbot deve responder *educadamente* com a informação requisitada.

## Parte 1: Chatbot faz pequenos queries em um serviço externo como mapa, clima, cálculos matemáticos, etc.

* Chatbot recebe comandos do tipo: `\run xxx xxx xxx`, em que `xxx` são parâmetros relevantes.
* O chatbot deve reconhecer, usando regex, se os argumentos `xxx` não são válidos.

## Parte 2: Chatbot faz webscrapping, guarda bases de dados e responde a queries de busca.

* Chatbot deve poder receber comandos do tipo `\crawl xxx`, onde `xxx` é uma URL. Ele deve então adicionar o conteúdo da URL em seu banco de dados, e começar um processo de crawling à partir daí.
* O chatbot deve receber comandos `\search xxx`, em que o usuário busca por um termo ou conceito. A resposta deve ser buscada usando um índice invertido.
* O chatbot deve receber comandos `\wn_search xxx`, em que faz uma busca por todos os documentos armazenados, usando um índice de semelhança ligado à Wordnet, isto é, o sistema pode buscar por termos semelhantes.

## Parte 3: Chatbot filtra conteúdo inadequado e só responde usando páginas com sentimento positivo.

* As páginas que foram colocadas no banco de dados usando `\crawl` passam a ser classificadas de acordo com seu sentimento, onde `-1` é o "mais negativo" e `1` é o "mais positivo". Os usuários podem optar por filtrar as buscas por sentimento usando `\search xxx th=0.3` ou `\wn_search xxx th=0.3`.

## Parte 4: Chatbot gera conteúdo à partir de sua base de dados.

* O chatbot deve responder à query `\generate xxx` que faz uma busca estilo `\search` pelo termo `xxx` e retorna uma frase gerada à partir dos textos.
* A query `\wn_generate xxx` faz o mesmo, mas usa a busca no estilo `\wn_search`.

## Parte 5: Chatbot integra com GPT-3.

* O chatbot usa a API do GPT-3 para realizar ao menos uma das tarefas anteriores.