# TP4: Máquina de Vending Automática
Feito por:
Marco António Ferreira Abreu, A108578

![image_alt](https://github.com/MarcoAbreu11/PLC2025/blob/main/Imagem/minha_imagem.jpg?raw=true)

## **Objetivo do Exercício**

O objetivo deste trabalho foi desenvolver um **sistema completo de máquina de vending automática** em Python, capaz de simular o funcionamento real de uma máquina de venda automática. O sistema deve ser capaz de:

- **Carregar e guardar o stock** de produtos de forma persistente usando ficheiros JSON
- **Processar inserção de moedas** e calcular saldo em euros e cêntimos
- **Permitir seleção de produtos** com verificação de stock e saldo suficiente
- **Calcular e dispensar troco** de forma otimizada usando as moedas disponíveis
- **Listar produtos disponíveis** com informações detalhadas
- **Adicionar/atualizar produtos** no stock existente
- **Verificar estado do stock** automaticamente no arranque
- **Gerir transações completas** desde a inserção de moedas até à entrega do produto e troco

## **Como Resolvi o Problema**

Para resolver este problema, estruturei a solução em **módulos especializados**:

### 1. **Arquitetura Modular**
Dividi o sistema em ficheiros especializados:
- **`maquina_venda.py`**: Programa principal que coordena toda a operação
- **`tarefas_da_maquina.py`**: Lógica de negócio (seleção, moedas, troco)
- **`carregar_guardar_stock.py`**: Persistência de dados em JSON
- **`verificar_stock.py`**: Verificação inicial do estado do stock
- **`data_atual.py`**: Obtenção da data atual do sistema

### 2. **Gestão de Stock Persistente**
- **Carregamento automático**: `carregar_stock()` lê o ficheiro `stock.json` no arranque
- **Atualização em tempo real**: O stock é atualizado após cada compra bem-sucedida
- **Persistência final**: `guardar_stock()` salva o estado final ao terminar

### 3. **Sistema de Moedas e Saldo**
- **Moedas suportadas**: 1e, 50c, 20c, 10c, 5c, 2c, 1c
- **Cálculo preciso**: `calcular_saldo()` converte moedas para valor decimal
- **Formatação inteligente**: `formatar_saldo()` mostra valores de forma legível (ex: "1e30c")

### 4. **Processamento de Compras**
- **Verificação em tempo real**: `selecionar_produto()` verifica:
  - Existência do produto
  - Stock disponível
  - Saldo suficiente
- **Atualização automática**: Stock é decrementado após compra bem-sucedida

### 5. **Sistema de Troco Otimizado**
- **Algoritmo ganancioso**: `calcular_troco()` usa as moedas de maior valor primeiro
- **Formatação natural**: `formatar_troco()` cria mensagens como "1x 50c, 1x 20c e 2x 2c"
- **Precisão decimal**: Cálculos com `round()` para evitar erros de ponto flutuante

### 6. **Funcionalidade ADICIONAR**
- **Produtos existentes**: Incrementa a quantidade se o código já existe
- **Novos produtos**: Cria entrada completa no stock
- **Validação robusta**: Verifica formatos e valores numéricos

### 7. **Interface de Utilizador**
- **Comandos intuitivos**: LISTAR, MOEDA, SELECIONAR, ADICIONAR, SAIR
- **Feedback claro**: Mensagens detalhadas em português
- **Tratamento de erros**: Mensagens específicas para cada tipo de erro
- **Recuperação graciosa**: Stock é guardado mesmo com interrupção (Ctrl+C)

Onde cheguei aos codigos que se encontram na pasta [codigo](https://github.com/MarcoAbreu11/PLC2025/tree/main/TP4/codigo).

## **Casos de Teste Realizados**

### **Teste 1 - Funcionamento Básico**  
[teste1.txt](Testes/teste1.txt)  
- **Comandos**: MOEDA 1e,50c → LISTAR → SELECIONAR A01 → SAIR  
- **Verificações**:   
  - Saldo inicial correto (1e50c)  
  - Produto dispensado com sucesso  
  - Stock atualizado (A01: 8→7)  
  - Troco calculado corretamente (50c+20c+10c)  
**Output**: [teste1.png](Testes/teste1.png)

### **Teste 2 - Cenários de Erro**  
[teste2.txt](Testes/teste2.txt)  
- **Comandos**: SELECIONAR XYZ → SELECIONAR H02 → MOEDA 10c → SELECIONAR C01 → SAIR  
- **Verificações**:  
  - Produto inexistente (mensagem apropriada)  
  - Produto sem stock (H02 com quant=0)  
  - Saldo insuficiente (10c vs 1.5€ necessário)  
  - Stock permanece inalterado para transações inválidas  
**Output**: [teste2.png](Testes/teste2.png)

### **Teste 3 - Múltiplas Compras**  
[teste3.txt](Testes/teste3.txt)  
- **Comandos**: MOEDA 1e,1e,20c,5c → SELECIONAR D01 → SELECIONAR G02 → SAIR  
- **Verificações**:  
  - Saldo após compras: 55c  
  - Troco otimizado: 1x50c + 1x5c  
  - Stock de D01 e G02 diminuído corretamente  
**Output**: [teste3.png](Testes/teste3.png)

### **Teste 4 - Funcionalidade ADICIONAR**  
[teste4.txt](Testes/teste4.txt)  
- **Comandos**: LISTAR → ADICIONAR K02 BOLO_CHOCOLATE 5 1.8 → LISTAR → MOEDA 2e → SELECIONAR K01 → ADICIONAR K02 3 1.8 → SELECIONAR K01 → SAIR  
- **Verificações**:  
  - Novo produto K02 criado com sucesso  
  - Stock inicial de K01: 8 → 7 após compra  
  - Stock de K02: 5 → 8 após ADICIONAR  
  - Troco final: 20c (2.0€ - 1.8€ = 0.2€)  
**Output**: [teste4_print1.png](Testes/teste4_print1.png) e [teste4_print2.png](Testes/teste4_print2.png)
