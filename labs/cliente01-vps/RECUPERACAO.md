# Recuperacao do Cliente01

## Objetivo

Documentar a recuperacao da aplicacao Python, do Nginx, do servico systemd e dos certificados TLS a partir dos backups.

## Arquivos protegidos

- /opt/cliente01-app/
- /etc/nginx/sites-available/cliente01
- /etc/systemd/system/cliente01-app.service
- /etc/ssl/cliente01/

## Armazenamento

- Local: /var/backups/cliente01/
- Remoto: Backblaze B2, via rclone.

## Verificacao realizada

Em 12/10/2026, foi confirmada a presenca dos arquivos no backup e a integridade de leitura do arquivo tar.gz mais recente.

## Cuidados na recuperacao

A restauracao deve ser realizada em ambiente de teste antes de substituir arquivos de um servidor em funcionamento. Os backups incluem uma chave privada TLS e devem permanecer protegidos.

## Restauracao segura em ambiente de teste

1. Identificar o backup local mais recente:

```bash
sudo ls -lt /var/backups/cliente01/cliente01-*.tar.gz
```

2. Criar um diretorio isolado para a restauracao:

```bash
sudo mkdir -p /tmp/cliente01-restore-test
```

3. Extrair o backup para o diretorio de teste (substituir NOME_DO_BACKUP pelo arquivo escolhido):

```bash
sudo tar -xzf /var/backups/cliente01/NOME_DO_BACKUP -C /tmp/cliente01-restore-test
```

4. Conferir os arquivos restaurados:

```bash
sudo find /tmp/cliente01-restore-test -type f
```

Esses comandos nao substituem arquivos do servidor em funcionamento.

## Recuperacao a partir do Backblaze B2

1. Listar os backups disponiveis:

```bash
sudo rclone lsl backblaze:cliente01-backups-ryan/cliente01
```

2. Baixar o backup escolhido para o diretorio local (substituir NOME_DO_BACKUP):

```bash
sudo mkdir -p /var/backups/cliente01
sudo rclone copyto backblaze:cliente01-backups-ryan/cliente01/NOME_DO_BACKUP /var/backups/cliente01/NOME_DO_BACKUP
```

3. Verificar a integridade do arquivo baixado:

```bash
sudo tar -tzf /var/backups/cliente01/NOME_DO_BACKUP > /dev/null
```

4. Seguir o procedimento de restauracao segura em ambiente de teste descrito anteriormente.

A recuperacao depende de acesso autorizado ao Backblaze B2 e da configuracao do rclone. Nao publicar credenciais nem arquivos de backup no GitHub.
