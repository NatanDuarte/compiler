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
