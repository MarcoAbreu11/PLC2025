# TP3: Analiziador lexico de Query SparQL
Feito por:
Marco António Ferreira Abreu, A108578

![image_alt](https://github.com/MarcoAbreu11/PLC2025/blob/main/Imagem/minha_imagem.jpg?raw=true)

## Objetivo do Exercício

O objetivo deste trabalho foi desenvolver um **analisador léxico** para a linguagem de consulta **SPARQL** utilizando a biblioteca **PLY** em Python. O analisador deve ser capaz de:

- **Reconhecer e tokenizar** os elementos fundamentais da linguagem SPARQL
- **Identificar palavras-chave** como `SELECT`, `WHERE`, `FILTER`
- **Reconhecer variáveis SPARQL** (ex: `?x`, `?nome`)
- **Processar URIs** prefixadas e default (ex: `rdf:type`, `:Person`)
- **Identificar operadores** de comparação (`=`, `!=`, `<`, `>`, `<=`, `>=`)
- **Reconhecer literais** como strings e números inteiros
- **Lidar com símbolos especiais** como `{`, `}`, `(`, `)`, `.`
- **Gerar mensagens de erro** para caracteres ilegais
- **Manter o controlo** dos números de linha durante a análise

## Como Resolvi o Problema

Para resolver este problema, segui as seguintes etapas:

### 1. **Definição dos Tokens**
Criei uma tupla com todos os tokens necessários para a linguagem SPARQL, incluindo operadores, palavras-chave e símbolos.

### 2. **Implementação das Regras Lexicais**
Desenvolvi funções para cada token usando expressões regulares:
- **`t_TOKENNAME`** para definir padrões regex de cada elemento
- **Priorização correta**: operadores multi-caractere primeiro (`!=`, `<=`, `>=`)
- **Token especial**: `A_KEYWORD` para reconhecer o `a` do SPARQL

### 3. **Processamento de Literais**
- **Para `STRING`**: utilizei `r'"[^"]*"'` para capturar qualquer texto entre aspas
- **Para `INTEGER`**: converti o valor para inteiro com `int(t.value)`

### 4. **Gestão de Espaços e Linhas**
- **`t_ignore = ' \t'`** para ignorar espaços e tabs
- **`t_newline`** para atualizar o contador de linhas

### 5. **Controlo de Erros**
- **`t_error`** para detetar e reportar caracteres ilegais

### 6. **Interface com o Utilizador**
Criei uma função que recebe input e mostra os tokens reconhecidos com seus tipos, valores e números de linha.

---

O analisador resultante é capaz de **processar consultas SPARQL complexas** e fornecer **feedback detalhado** sobre a estrutura léxica das mesmas, demonstrando uma implementação robusta e funcional do analisador léxico.

Assim cheguei ao código que se encontra [analisador_lexico_queryQL.py](analisador_lexico_queryQL.py). Para verificar se o código estava correto realizei vários testes, sendo eles:

- [teste1.txt](teste1.txt) tendo o [output esperado do teste 1](output_esperado_teste1.png)
- [teste2.txt](teste2.txt) tendo o [output esperado do teste 2](output_esperado_teste2.png) 
- [teste3.txt](teste3.txt) tendo o [output esperado do teste 3](output_esperado_teste3.png)
