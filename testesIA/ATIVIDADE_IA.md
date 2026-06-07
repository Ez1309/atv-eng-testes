# Uso de IA para Geração de Cenários de Teste

## 1. Função Escolhida
`calcular_media(lista)`

## 2. Prompt Utilizado
```text
Atue como um professor de Teste de Software. Tenho a seguinte função Python:

def calcular_media(lista):
    if not lista:
        raise ValueError("A lista não pode ser vazia")
    return sum(lista) / len(lista)
    
Quero criar testes unitários usando unittest. Liste pelo menos 6 cenários de teste para essa função. Para cada cenário, informe: nome do cenário, entrada, resultado esperado e tipo do cenário (caso normal, borda ou erro). Não gere código ainda, crie uma tabela de planejamento.
```

## 3. Cenários Sugeridos pela IA

| ID | Cenário | Entrada | Resultado Esperado | Tipo |
| :--- | :--- | :--- | :--- | :--- |
| T01 | Média de inteiros positivos | `[10, 8, 6]` | `8.0` | Normal |
| T02 | Média com decimais | `[2.5, 7.5]` | `5.0` | Normal |
| T03 | Média com números negativos | `[-2, -4, -6]` | `-4.0` | Normal |
| T04 | Lista com apenas um elemento | `[10]` | `10.0` | Borda |
| T05 | Lista contendo apenas zeros | `[0, 0, 0]` | `0.0` | Borda |
| T06 | Lista com strings misturadas | `[10, "A"]` | `TypeError` | Erro |
| T07 | Lista vazia | `[]` | `ValueError` | Erro |

## 4. Análise Crítica dos Cenários
Aceitei os cenários de T01 a T05 e o T07, pois cobrem perfeitamente os casos normais, de borda (zeros e item único) e de erro (`ValueError`). 

**Cenário Removido:** Removi o cenário T06 gerado pela IA (Lista com strings). A função embutida `sum()` do Python já lança um `TypeError` nativamente ao tentar somar inteiros com strings. O objetivo do nosso teste unitário é validar a lógica de negócio da nossa função (como a exceção da lista vazia), e não testar o comportamento nativo do interpretador Python.

## 5. Código Final dos Testes da Função
Os testes foram implementados no arquivo `test_calculadora.py` utilizando o recurso `subTest` para agrupar os casos validados:

```python
    def test_calcular_media_com_varios_casos(self):
        """Testes gerados com apoio de IA e refatorados com subTest."""
        casos = [
            ([10, 8, 6], 8.0),
            ([2.5, 7.5], 5.0),
            ([-2, -4, -6], -4.0),
            ([10], 10.0),
            ([0, 0, 0], 0.0),
        ]
        for lista, esperado in casos:
            with self.subTest(lista=lista):
                self.assertEqual(calcular_media(lista), esperado)

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])
```

## 6. Resultado da Execução
Comando executado no terminal:
```bash
python -m unittest discover
```

Saída obtida confirmando que todos os cenários (agrupados em 8 métodos de teste principais) passaram com sucesso:
```bash
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```
