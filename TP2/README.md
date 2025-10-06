# TP2: Conversor de MarkDown para HTML
Feito por:
Marco António Ferreira Abreu, A108578

![image_alt](https://github.com/MarcoAbreu11/PLC2025/blob/main/Imagem/minha_imagem.jpg?raw=true)

## Objetivo do Exercício

O **TPC3** teve como objetivo desenvolver um conversor de **MarkDown para HTML** em Python, capaz de transformar os elementos da sintaxe MarkDown nos seus equivalentes em HTML. O conversor deveria processar os seguintes elementos:

- **Cabeçalhos** (`#`, `##`, `###`) → `<h1>`, `<h2>`, `<h3>`
- **Texto em negrito** (`**texto**`) → `<b>texto</b>`
- **Texto em itálico** (`*texto*`) → `<i>texto</i>`
- **Listas numeradas** (`1. item`) → `<ol><li>item</li></ol>`
- **Links** (`[texto](url)`) → `<a href="url">texto</a>`
- **Imagens** (`![alt](src)`) → `<img src="src" alt="alt"/>`

## Como Resolvi o Problema
Desenvolvi a solução utilizando **expressões regulares** em Python para identificar e substituir os padrões MarkDown. A estratégia foi:

1. **Processar listas primeiro** - por requererem lógica especial multi-linha
2. **Depois processar elementos inline** - usando substituições simples com regex
3. **Garantir a ordem correta** - especialmente entre imagens e links

Assim cheguei ao código que se encontra [codigo.py](codigo.py). Para verificar se o código estava correto realizei um teste que se encontra [teste_realizado.txt](teste_realizado.txt) onde podemos verificar o seu output em [output_esperado.png](output_esperado.png).
