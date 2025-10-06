import re

def conversor_markdown_html(entrada):
    # Processar listas numeradas PRIMEIRO (lógica especial)
    linhas = entrada.split('\n')
    resultado = []
    i = 0
    
    while i < len(linhas):
        linha = linhas[i]
        if re.match(r"^\d+\.\s(.+)", linha):  # Detetar início de lista
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

    # casos das imagens e links
    entrada = re.sub(r"\!\[(.*?)\]\((.+?)\)", r'<img src="\2" alt="\1"/>', entrada)
    entrada = re.sub(r"\[(.*?)\]\((.+?)\)", r'<a href="\2">\1</a>', entrada)

    return entrada