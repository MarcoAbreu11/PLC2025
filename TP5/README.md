# Análise Léxica e Sintática de Expressões Aritméticas

## 📋 Objetivo do Exercício

Este projeto tem como objetivo implementar um **analisador léxico e sintático** para expressões aritméticas simples. O sistema deve ser capaz de:

- Reconhecer tokens básicos em expressões matemáticas (números, operadores, parênteses)
- Validar a estrutura sintática das expressões segundo uma gramática definida
- Detetar e reportar erros léxicos e sintáticos
- Processar operações matemáticas com números inteiros e parênteses
- Fornecer um output detalhado do processo de análise

## 🛠️ Como Foi Resolvido

### Estrutura do Projeto

O projeto está organizado em três ficheiros principais:

- **[conta_analex.py](conta_analex.py)**: Implementação do analisador léxico
- **[conta_anasin.py](conta_anasin.py)**: Implementação do analisador sintático  
- **[conta_programa.py](conta_programa.py)**: Programa principal

### Gramática Implementada
p1: Exp -> Term OpExp
p2: OpExp -> Op Exp | ε
p3: Term -> INT | PARENTESES_ABRIR Exp PARENTESES_FECHAR
p4: Op -> SOMA | DIFERENCA | MULTIPLICACAO | DIVISAO

### Análise Léxica

**Ficheiro: [conta_analex.py](código/conta_analex.py)**

- Utiliza a biblioteca **PLY (Python Lex-Yacc)**
- Define tokens para números inteiros, operadores e parênteses
- Implementa funções para reconhecer cada tipo de token
- Inclui tratamento de espaços, tabs e quebras de linha
- Deteta e reporta caracteres ilegais

### Análise Sintática

**Ficheiro: [conta_anasin.py](código/conta_anasin.py)**

- Implementa um **parser recursivo descendente**
- Segue a gramática definida com funções para cada regra de produção
- Utiliza uma abordagem **predictive parsing**
- Inclui tratamento de erros sintáticos
- Fornece output detalhado do processo de reconhecimento

### Ficheiro: [Fluxo de Execução](código/conta_programa.py)

1. O utilizador introduz uma expressão no programa principal
2. O analisador léxico tokeniza a input
3. O analisador sintático valida a estrutura segundo a gramática
4. São mostradas as regras aplicadas durante a análise
5. Erros são reportados quando detetados

## 🧪 Casos de Teste Realizados

### 1. [Teste Simples](testes/teste_simples.png)
**Expressão:** `5+3`
**Objetivo:** Validar o funcionamento básico com uma operação simples
**Resultado:** Análise concluída com sucesso, mostrando todas as regras aplicadas

### 2. [Teste com Múltiplas Operações](testes/teste_com_multiplas_operacoes.png)
**Expressão:** `8/4+2*3`
**Objetivo:** Testar expressões com múltiplos operadores e precedência implícita
**Resultado:** Sistema processou corretamente todas as operações sequencialmente

### 3. [Teste com Parênteses](testes/teste_com_parenteses.png)
**Expressão:** `(10-2)*3`
**Objetivo:** Validar o tratamento de expressões com agrupamento por parênteses
**Resultado:** Parênteses reconhecidos e processados corretamente

### 4. [Teste com Expressão Inválida](testes/teste_expressao_invalida.png)
**Expressão:** `5++3`
**Objetivo:** Verificar a deteção e reporte de erros sintáticos
**Resultado:** Sistema detetou o token inesperado e reportou o erro apropriadamente
