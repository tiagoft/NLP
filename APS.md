# APS

## Parte 0: Um chatbot para o Discord

* O chatbot deve responder a solicitações realizadas em um chat privado
* O comando `!source` retorna um link para o repositório onde está o código-fonte do chatbot.
* O comando `!author` retorna o nome e e-mail do autor do chatbot.
* O chatbot deve responder *educadamente* com a informação requisitada.

Entregas:

* Chatbot executando em background em sua VM. Se precisar, use o `nohup` ou o `screen` para deixar o bot executando mesmo quando você não estiver 
* No github, deve haver um `README.md` que explica como rodar o servidor localmente.
* O arquivo `README.md` deve linkar para outro arquivo, `ensaio_0.md`, no qual cada aluno explica como foi o processo de fazer o chatbot (como foi o plano, que dificuldades foram encontradas, quais foram as fontes consultadas, como foi a interação com chatGPT, se houver, etc.). O formato do `ensaio_0.md` é livre, e pode ser tanto um ensaio propriamente dito quanto uma tabela.

Avaliação:

* 100%: o chatbot e os arquivos de texto cumprem todos os requisitos
* 0%: faltam requisitos a serem cumpridos

Deadline: 19/fevereiro

## Parte 1: Chatbot faz pequenos queries em um serviço externo como mapa, clima, bolsa de valores, etc.

* O chatbot deve cumprir todos os requisitos da entrega anterior, com as adições colocadas aqui.
* Chatbot recebe comandos do tipo: `!run xxx xxx xxx`, em que `xxx` são parâmetros relevantes.
* O chatbot deve reconhecer, usando regex, se os argumentos `xxx` não são válidos.
* O chatbot deve responder a um comando `!help` explicando como usar o comando `!run` e explicitando de onde vêm os dados (exemplo: `!help` retorna `!run nome_da_cidade: retorna a temperatura atual na cidade - dados fornecidos pelo site www.meusitedeclima.com.br`).
* Cada aluno deve escolher alguma operação que faça sentido para algum caso de aplicação.

Entregas:

* Chatbot executando em background em sua VM. Se precisar, use o `nohup` ou o `screen` para deixar o bot executando mesmo quando você não estiver 
* No github, deve haver um `README.md` que explica como rodar o servidor localmente.
* O arquivo `README.md` deve linkar para outro arquivo, `ensaio_1.md`, no qual cada aluno explica como foi o processo de fazer essa etapa, com as mesmas diretrizes anteriores, e especialmente *explicando seu caso de uso* (ou seja: quem seria, hipoteticamente, seu usuário-alvo?). O formato do `ensaio_1.md` é livre, e pode ser tanto um ensaio propriamente dito quanto uma tabela.

Avaliação:

* 100%: o chatbot e arquivos de texto cumprem todos os requisitos
* 90%: cumpre todos os requisitos exceto pela justificativa do caso de uso
* 50%: `!run` e `!help` foram implementados, mas o `ensaio_1.md` está incompleto.
* 0%: o comando `!run` não faz consultas a um servidor externo ou o `!help` não foi implementado

Deadline: 5/março

## Parte 2: Chatbot faz webscrapping, guarda bases de dados e responde a queries de busca.


* Chatbot deve poder receber comandos do tipo `!crawl xxx`, onde `xxx` é uma URL. Ele deve então adicionar o conteúdo da URL em seu banco de dados, e começar um processo de crawling à partir daí.
* O chatbot deve receber comandos `!search xxx`, em que o usuário busca por um termo ou conceito. A resposta deve ser buscada usando um índice invertido.
* O chatbot deve receber comandos `!wn_search xxx`, em que faz uma busca por todos os documentos armazenados, usando um índice de semelhança ligado à Wordnet, isto é, o sistema pode buscar por termos semelhantes.

## Parte 3: Chatbot filtra conteúdo inadequado e só responde usando páginas com sentimento positivo.

* As páginas que foram colocadas no banco de dados usando `!crawl` passam a ser classificadas de acordo com seu sentimento, onde `-1` é o "mais negativo" e `1` é o "mais positivo". Os usuários podem optar por filtrar as buscas por sentimento usando `!search xxx th=0.3` ou `!wn_search xxx th=0.3`.

## Parte 4: Chatbot gera conteúdo à partir de sua base de dados.

* O chatbot deve responder à query `!generate xxx` que faz uma busca estilo `!search` pelo termo `xxx` e retorna uma frase gerada à partir dos textos.
* A query `!wn_generate xxx` faz o mesmo, mas usa a busca no estilo `!wn_search`.

## Parte 5: Chatbot integra com GPT-3.

* O chatbot usa a API do GPT-3 para realizar ao menos uma das tarefas anteriores.