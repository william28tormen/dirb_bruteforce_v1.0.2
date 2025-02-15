# Dirb Brute Force Scan
Um DIRB Brute Force Scan é uma técnica de varredura de diretórios e arquivos em servidores web, utilizada para descobrir recursos ocultos ou não linkados publicamente. O DIRB é uma ferramenta de código aberto projetada para realizar ataques de força bruta em URLs, testando uma lista de palavras-chave (wordlist) contra um servidor web para identificar diretórios e arquivos existentes.

Como funciona:
Wordlist: O DIRB utiliza uma lista de palavras (wordlist) que contém possíveis nomes de diretórios ou arquivos. Essas listas podem ser personalizadas ou pré-definidas.

Varredura: A ferramenta envia requisições HTTP (GET ou POST) para o servidor, combinando a URL base com cada palavra da lista.

Respostas: Com base nas respostas do servidor (códigos de status HTTP, como 200, 404, 403), o DIRB identifica quais diretórios ou arquivos existem.

Resultados: Os recursos encontrados são listados, permitindo que o usuário identifique possíveis pontos de entrada ou vulnerabilidades.

Objetivo:
Descobrir diretórios ou arquivos não públicos que podem conter informações sensíveis, painéis de administração, backups, ou outros recursos que possam ser explorados.

Auxiliar em testes de penetração (pentests) para avaliar a segurança de um servidor web.

Como usar:
python bruteforce_dirb http://exemplo.com/ /caminho/para/wordlist.txt

Neste exemplo, o DIRB varre o site http://exemplo.com/ usando a wordlist especificada.

Códigos de status comuns:
200 (OK): O recurso foi encontrado.

404 (Not Found): O recurso não existe.

403 (Forbidden): Acesso negado (pode indicar um recurso restrito).

Considerações éticas:
O uso do DIRB ou qualquer ferramenta de brute force sem autorização é ilegal e antiético.

Sempre obtenha permissão por escrito antes de realizar testes em sistemas que não são de sua propriedade.

O DIRB é uma ferramenta poderosa, mas deve ser usada com responsabilidade e dentro dos limites da lei.

William Tormen -> https://williamtormen.com.br