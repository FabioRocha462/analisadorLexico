import re

def lexer(code):
    # Definir padrões para os tokens
    token_patterns = [
        ('KEYWORD', r'(if|else|while|for)'),
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),
        ('NUMBER', r'\d+(\.\d+)?|\.\d+'),  # Atualizado para reconhecer ponto flutuante
        ('OPERATOR', r'[\+\-\*/]'),
        ('SYMBOL', r'[=(),;]'),
        ('WHITESPACE', r'\s+')
    ]
    
    # Montar a expressão regular para os tokens
    regex_patterns = '|'.join('(?P<%s>%s)' % pair for pair in token_patterns)
    token_regex = re.compile(regex_patterns)
    
    # Fazer o matching dos tokens no código-fonte
    tokens = []
    for match in token_regex.finditer(code):
        kind = match.lastgroup
        value = match.group()
        tokens.append((kind, value))
    
    return tokens


# Testar o analisador léxico
codigo_fonte = """
if x > 5.25:
    print("x é maior que 5.25")
else:
    print("x é menor ou igual a 5.25")
"""

tokens = lexer(codigo_fonte)

# Exibir os tokens encontrados
for token in tokens:
    kind, value = token
    print(f'Tipo: {kind}, Valor: {value}')
