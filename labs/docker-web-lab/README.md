# Docker Web Lab

Laboratório prático de infraestrutura Linux utilizando Docker Engine, Docker Compose e Nginx.

## Objetivo

Publicar uma página web personalizada em um contêiner Docker, utilizando Docker Compose e um bind mount somente para leitura.

## Tecnologias

- Ubuntu Server 26.04 LTS
- Docker Engine
- Docker Compose
- Nginx Alpine
- Git

## Estrutura do projeto

- compose.yaml: configuração do serviço Nginx
- site/index.html: página web personalizada

## Como executar

1. Instalar Docker Engine e Docker Compose.
2. Clonar ou baixar este projeto.
3. Executar: sudo docker compose up -d
4. Testar: curl http://127.0.0.1:8081/

## Validação realizada

- Contêiner iniciado com sucesso.
- Serviço HTTP retornando status 200.
- Página HTML personalizada publicada corretamente.
- Bind mount configurado como somente leitura.

## Segurança

A porta 8081 está vinculada ao endereço 127.0.0.1, restringindo o acesso à própria máquina que executa o Docker.

## Observação

Projeto desenvolvido em ambiente de laboratório para estudos e demonstração prática de competências em administração Linux e infraestrutura.
