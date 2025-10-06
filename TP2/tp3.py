import re

def conversor_markdown_html(entrada):
    # Processar listas numeradas
    linhas = entrada.split('\n')
    resultado = []
    i = 0
    
    while i < len(linhas):
        linha = linhas[i]
        if re.match(r"^\d+\.\s(.+)", linha):
            lista_items = ['<ol>']
            while i < len(linhas) and re.match(r"^\d+\.\s(.+)", linhas[i]):
                item = re.sub(r"^\d+\.\s(.+)", r"<li>\1</li>", linhas[i])
                lista_items.append(item)
                i += 1
            lista_items.append('</ol>')
            resultado.extend(lista_items)
        else:
            resultado.append(linha)
            i += 1
    
    entrada = '\n'.join(resultado)
    
    # casos dos cabeçalhos
    entrada = re.sub(r"^#\s(.+)$", r"<h1>\1</h1>", entrada, flags=re.MULTILINE)
    entrada = re.sub(r"^##\s(.+)$", r"<h2>\1</h2>", entrada, flags=re.MULTILINE)
    entrada = re.sub(r"^###\s(.+)$", r"<h3>\1</h3>", entrada, flags=re.MULTILINE)

    # casos de negrito e itálico
    entrada = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", entrada)
    entrada = re.sub(r"\*(.+?)\*", r"<i>\1</i>", entrada)

    # casos de links e imagens
    entrada = re.sub(r"\[(.*?)\]\((.+?)\)", r'<a href="\2">\1</a>', entrada)
    entrada = re.sub(r"\!\[(.*?)\]\((.+?)\)", r'<img src="\2" alt="\1"/>', entrada)

    return entrada

# Teste
markdown_grande = """
# Guia de Programação Web

## Introdução ao Desenvolvimento Web

O desenvolvimento web moderno envolve várias tecnologias. **HTML** é a base de qualquer website, enquanto *CSS* cuida do estilo e **JavaScript** adiciona interatividade.

### Tecnologias Fundamentais

1. HTML - Estrutura da página
2. CSS - Estilização e design
3. JavaScript - Comportamento dinâmico

## Recursos Úteis

### Links Importantes

Visitem a [documentação MDN](https://developer.mozilla.org) para referências completas. Também recomendo o [W3Schools](https://www.w3schools.com) para tutoriais.

### Exemplos de Imagens

Aqui está um exemplo de como incluir imagens: ![Logo HTML5](https://example.com/html5.png) e ![Logo CSS3](https://example.com/css3.png).

## Lista de Comandos Git

1. git init - Inicializar repositório
2. git add . - Adicionar todos os ficheiros
3. git commit -m "mensagem" - Fazer commit
4. git push - Enviar para repositório remoto

## Dicas de Formatação

Podem usar **negrito** para ênfase forte e *itálico* para ênfase suave. **Importante**: sempre testem o vosso código!

### Exemplo de Código

Para criar um botão em HTML:
"""

print(conversor_markdown_html(markdown_grande))