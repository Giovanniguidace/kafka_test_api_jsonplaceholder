# Criando um Producer e Consumer utilizando Kafka e Python

## :orange_book: <b>Desafio da aplicação</b>

O desafio é criar um container com Kafka e outro com o Zookeeper, utilizando Docker. Criar uma aplicação para ser o Producer e outra para ser o Consumer, utilizando a linguagem Python, onde o Producer enviará e o Consumer irá receber dados recebidos da API gratuita da JSONPLACEHOLDER.

## <b>:dart: Objetivo da Aplicação </b>

Realizar testes da funcionalidade do Kafka, com cunho didático.


## <b>⚙️ Tecnologias Adotadas na Solução:</b>

* Python 3.8.10
* Kafka 2.13-2.7.1
* Zookeeper 3.4.13
* Docker 20.10.7

## :books: Bibliotecas Utilizadas

* kafka-python
* requests (Nativo Python)

## :hammer: Construindo o Projeto

### Criação de containers do Kafka e Zookeeper utilizando o docker-compose:

Deverá ser criado um arquivo chamado docker-compose.yml contendo o seguinte conteúdo:

```docker
version: '3'

services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
  kafka:
    image: wurstmeister/kafka
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
```

Com o conteúdo acima, será criado um container para o Kafka na porta 9092(padrão do kafka) e um container para o Zookeeper na porta 2181. O enviroment KAFKA_ZOOKEEPER_CONNECT terá como parâmetro o nome do container do zookeeper e a porta, para que o kafka consiga se comunicar com os serviços do mesmo.

Pelo terminal, acesse a pasta onde está localizado o arquivo docker-compose.yml criado anteriormente e execute o seguinte comando:

```
docker-compose up -d
```

Após a criação dos containers, verifique se estão ativos com o seguinte comando:

```
docker ps
```

Deverá aparecer da seguinte forma:

![image](https://user-images.githubusercontent.com/62898187/145446073-cd58d652-1255-45c8-a0ae-4fc190f1a687.png)
Neste momento, temos os containers do Kafka e do Zookeeper. Agora, estamos aptos para realizar a criação do Topic de testes chamado "python-topic"

Para criamos este Topic deveremos acessar o container do Kafka e executar comandos. Para isso, digite o comando abaixo:

```
docker exec -it kafka /bin/sh
```
Após acessar o Kafka, vamos acessar a pasta do kafka que está localizada em /opt/ com o seguinte comando:

```
cd /opt/kafka_VERSÃODOKAFKA/bin
```

Após acessar a pasta bin do kafka, digite o seguinte comando para criar o Topic:

```
kafka-topics --create --zookeeper localhost:2181 --topic python-topic --replication-factor 1 --partitions 3
```

Com este comando, iremos criar o Topic que a aplicação fará conexão. Foi determinado apenas um único replication factor porque estamos criando a aplicação em apenas um único broker(server). Criaremos 3 partições, para que tenhamos uma rapidez maior na consulta dos dados e maior segurança no armazenamento dos dados.


Com os passos acima, poderemos executar os arquivos producer.py e consumer.py via terminal. 

Para que os arquivos sejam executados corretamente, é necessário estar com o virtualenv ativado e com a lib kafka-python instalada.


