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

input in interactive mode: `start var x int = 4; x = x + 2; write(x); end`

```json
[
  {
    "kind": "identifier",
    "value": "start",
    "position": 5,
    "line": 1
  },
  {
    "kind": "var",
    "value": "var",
    "position": 9,
    "line": 1
  },
  {
    "kind": "identifier",
    "value": "x",
    "position": 11,
    "line": 1
  },
  {
    "kind": "data_type",
    "value": "int",
    "position": 15,
    "line": 1
  },
  {
    "kind": "attribution",
    "value": "=",
    "position": 16,
    "line": 1
  },
  {
    "kind": "integer",
    "value": "4",
    "position": 19,
    "line": 1
  },
  {
    "kind": "end_statement",
    "value": ";",
    "position": 19,
    "line": 1
  },
  {
    "kind": "identifier",
    "value": "x",
    "position": 22,
    "line": 1
  },
  {
    "kind": "attribution",
    "value": "=",
    "position": 23,
    "line": 1
  },
  {
    "kind": "identifier",
    "value": "x",
    "position": 26,
    "line": 1
  },
  {
    "kind": "operator",
    "value": "+",
    "position": 27,
    "line": 1
  },
  {
    "kind": "integer",
    "value": "2",
    "position": 30,
    "line": 1
  },
  {
    "kind": "end_statement",
    "value": ";",
    "position": 30,
    "line": 1
  },
  {
    "kind": "identifier",
    "value": "write",
    "position": 37,
    "line": 1
  },
  {
    "kind": "identifier",
    "value": "x",
    "position": 39,
    "line": 1
  },
  {
    "kind": "end_statement",
    "value": ";",
    "position": 40,
    "line": 1
  },
  {
    "kind": "end",
    "value": "end",
    "position": 45,
    "line": 1
  }
]
```
