# Docker Volume Persistence Lab

Laboratório prático para demonstrar persistência de dados utilizando Docker Volumes.

## Objetivo

Comprovar que dados gravados por um container podem continuar existindo mesmo após o container ser removido.

## Tecnologias utilizadas

- Linux
- Docker
- Docker Compose
- Alpine Linux
- Volumes bind mount

## Como executar

docker compose up -d

## Ver logs do container

docker logs volume-persistence-test

## Encerrar e remover container

docker compose down

## Verificar persistência dos dados

cat data/log.txt

## Conceito demonstrado

Containers são descartáveis, mas os dados podem ser preservados quando armazenados em volumes.

Neste laboratório, o container grava registros no arquivo:

data/log.txt

Mesmo após executar docker compose down, o arquivo continua disponível no host Linux.

## Competências demonstradas

- Docker Volumes
- Bind Mount
- Persistência de dados
- Docker Compose
- Linux filesystem
- Administração básica de containers

## Autor

Ryan Tepedino
