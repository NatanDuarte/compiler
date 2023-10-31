# Compiler

## Modo interativo

```python
python .\main.py -i
```

## Modo arquivo

É possível ler arquivos com a extensão `.txt`.

```python
python .\main.py -f path/to/file
```

## Valid Statements

```python
start # delimits the start of programs scope

var -> identifier -> data_type -> attribution -> identifier | IntegerLiteral | FloatLiteral -> end_statement

identifier -> attribution -> IntegerLiteral | FloatLiteral -> end_statement

identifier -> identifier | IntegerLiteral | FloatLiteral -> operator -> identifier | IntegerLiteral | FloatLiteral -> end_statement

# functions
identifier -> left_parenthesis -> identifier | None -> right_parenthesis -> end_statement

end # delimits the end of programs scope
```

### Tokenizer output example

```python
{
  'kind': 'init', 
  'value': 'init', 
  'position': 4, 
  'line': 2
}
{'kind': 'var', 'value': 'var', 'position': 7, 'line': 3}
{'kind': 'identifier', 'value': 'x', 'position': 62, 'line': 3}
{'kind': 'data_type', 'value': 'int', 'position': 11, 'line': 3}
{'kind': 'attribution', 'value': '=', 'position': 11, 'line': 3}
{'kind': 'integer', 'value': '5', 'position': 14, 'line': 3}
{'kind': 'end_statement', 'value': ';', 'position': 14, 'line': 3}
{'kind': 'var', 'value': 'var', 'position': 7, 'line': 4}
{'kind': 'identifier', 'value': 'y', 'position': 81, 'line': 4}
{'kind': 'data_type', 'value': 'int', 'position': 11, 'line': 4}
{'kind': 'attribution', 'value': '=', 'position': 11, 'line': 4}
{'kind': 'integer', 'value': '5', 'position': 14, 'line': 4}
{'kind': 'end_statement', 'value': ';', 'position': 14, 'line': 4}
{'kind': 'var', 'value': 'var', 'position': 7, 'line': 6}
{'kind': 'identifier', 'value': 'z', 'position': 101, 'line': 6}
{'kind': 'data_type', 'value': 'int', 'position': 11, 'line': 6}
{'kind': 'attribution', 'value': '=', 'position': 11, 'line': 6}
{'kind': 'identifier', 'value': 'x', 'position': 109, 'line': 6}
{'kind': 'operator', 'value': '+', 'position': 14, 'line': 6}
{'kind': 'identifier', 'value': 'y', 'position': 113, 'line': 6}
{'kind': 'end_statement', 'value': ';', 'position': 16, 'line': 6}
{'kind': 'write', 'value': 'write', 'position': 9, 'line': 8}
{'kind': 'left_parenthesis', 'value': '(', 'position': 9, 'line': 8}
{'kind': 'identifier', 'value': 'z', 'position': 127, 'line': 8}
{'kind': 'right_parenthesis', 'value': ')', 'position': 11, 'line': 8}
{'kind': 'end_statement', 'value': ';', 'position': 12, 'line': 8}
{'kind': 'end', 'value': 'end', 'position': 3, 'line': 9}
```

---

## Documentação

Este código é uma implementação simplificada de um compilador para uma linguagem de programação. O compilador é dividido em vários estágios, dois dos quais são tokenização (realizada pelo tokenizer) e  análise (realizada pelo analisador).   

A função compile aceita o programa como uma string (prompt ou arquivo) e faz o seguinte:   

- Chama o Tokenizer para dividir a string do programa em uma lista de tokens. Isso é feito por que token = Tokenizer().tokenize(program). O token é impresso na saída padrão para que você possa ver a representação do token. 

- Token chama o analisador para analisar a lista de tokens que produz. Isso é feito por string parser = Parser(token).  
O resultado da análise obtido é retornado chamando parser.parse().  

Basicamente, a função de compilação marca o programa de entrada, exibe essas tags na saída padrão e, em seguida, passa essas tags ao analisador para garantir que o programa siga a gramática da linguagem especificada. O método parse retorna True se o programa for sintaticamente válido, False caso contrário.

### Analisador Sintático (Parser)

O construtor `__init__` inicializa o objeto Parser com uma lista de tokens e define alguns atributos de estado, como is_error (para rastrear erros) e *token_handlers* (um dicionário que mapeia tipos de tokens para os métodos que os tratam).

O método parse é o ponto de entrada do analisador. Ele chama o método program e verifica se o último token é do tipo "end" (indicando o final do programa) e se não houve erros durante a análise.

Os métodos advance e expect são usados para avançar para o próximo token e verificar se ele é do tipo esperado.

O método program é responsável por analisar a estrutura global do programa, começando com a palavra-chave "awakeHero" e terminando com "sealDarkness". Chama o método commands para analisar as instruções no corpo do programa.

O método commands analisa várias instruções, como declarações de variáveis, escrita de valores, atribuições e identificadores. Ele continua chamando os métodos apropriados com base no tipo do token atual até que um token "end" seja encontrado.

Existem métodos correspondentes para cada tipo de token, como parse_var, parse_write, parse_identifier, etc., que fazem a análise específica para cada tipo de construção na linguagem.

O método expression é usado para analisar expressões matemáticas, incluindo operadores e termos. Ele chama o método term para analisar os termos e lida com a precedência dos operadores.

O método term lida com os termos em uma expressão, que podem ser números inteiros, números de ponto flutuante ou identificadores.

O método error é chamado quando um erro é detectado durante a análise. Ele imprime uma mensagem de erro e define o atributo is_error como True.

### Analise Léxica (tokens)

Importação de funções is_number e is_letter do módulo core.util.

Definição de duas listas:

|                |                                                                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| reserved_words | Contém palavras reservadas da linguagem, como "awakeHero", "sealDarkness", "takeThis", "heyListen" equivalentes a  "init", "end", "var" e "write" respectivamente. |
| data_types     | Contém os tipos de dados permitidos na linguagem, como "rupees" e "zoras", equivalente a "int" e "float" respectivamente.                                          |
|                |                                                                                                                                                                    |

Declaração da classe Tokenizer com um único método estático chamado tokenize.

O método tokenize recebe uma string como entrada e retorna uma lista de tokens.

O código itera pelos caracteres da string usando um loop while até que todos os caracteres tenham sido processados.

Dentro do loop, o código verifica cada caractere individual e toma ações com base em seu valor:

- Os operadores -, +, =, e ponto e vírgula (;) são reconhecidos como tokens separados do tipo correspondente, e as informações relevantes são armazenadas em um dicionário e adicionadas à lista de tokens.(Espaços em branco são ignorados)

- Quebras de linha (\n ou \r) são tratadas atualizando a posição e o número da linha.

- Caracteres numéricos são tratados como parte de números inteiros ou de ponto flutuante, dependendo se um ponto (.) é encontrado no meio do número.

- Caracteres alfabéticos são tratados como parte de identificadores. Se a sequência de caracteres corresponder a uma palavra reservada, ela é classificada como tal. Caso contrário, se corresponder a um tipo de dado da lista data_types, ela é classificada como um "data_type". Caso contrário, é classificada como um "identifier".

- O código também reconhece parênteses esquerdo e direito, adicionando tokens separados para eles.


#### OBS: 

Se um caractere # for encontrado, o código ignora todos os caracteres até encontrar outro #. Isso é usado para ignorar comentários na linguagem.

Se um caractere que não se encaixa em nenhuma das categorias acima for encontrado, ele gera uma exceção SyntaxError, indicando que o caractere é inválido na linguagem.

No final, a lista de tokens é retornada, que contém informações sobre todos os tokens identificados na string de entrada.