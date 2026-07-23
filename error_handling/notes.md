# Mensagens comuns de erro em Python
O interpretador do python informa os diferentes tipos de erros ao tentar compilar o código.

## SyntaxError
Informa erro de sintaxe.
```python
print("hello, world" # n tem fechamento
```

## NameError
Ocorre quando tentamos utilizar uma variável não definida.

## TypeError
Erro de tipo. Por exemplo, somar uma string com um inteiro.
```Python
5 + "5"
```

## IndexError
Ocorre quando tentamos acessar um índice que não existe em uma lista.

## AttributeError
Ocorre quando tentamos utilizar um método que não existe para aquele tipo de dado.
```Python
num = 42
num.append(5) # append é operação de lista
```

# Exceção
Serve para tratar erros e evitar "crash" no programa. Pega o erro e trata-o. Utilizamos os operadores **try**, **except**, **else** e **finally**.

**try:** serve para antecipar um erro que pode ocorrer. Quando um erro acontece, a execução é interrompida ali mesmo e é jogado para o except.
**except:** esse bloco roda caso houve algum erro no try, a execução é interrompida. Podemos utilizar mais de um no try.

exemplo com dois tipos de exceção. Ocorre quando o usuário informa um valor inválido ou tenta dividir por zero.

```python
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')
```

**else:** roda quando não houve exceção no try.
**finally:** roda não importa o que houve, com exceção ou não.

# Raise Statement
É utilizado como exceção, onde é possível criar exceções personalizadas e que sejam postas em qualquer lugar do programa, sem necessitar do bloco try.

```python
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative
```

Podemos fazer raise dos próprios erros padrões do python. Também é possível fazer algo como: **raise (...) from None**, que lança uma nova exceção (texto do raise) ocultando a mensagem padrão do python.

```python
try:
    int("texto")
except ValueError:
    # Oculta o ValueError original e levanta apenas o RuntimeError
    raise RuntimeError("Falha ao processar o parâmetro") from None
```


