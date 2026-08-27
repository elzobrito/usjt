# Testes da consulta de escolas (Java)

**UC:** Gestão da Qualidade de Software  
**Produto didático:** fatia Java da consulta de escolas (BDGETEC)  
**Ferramenta:** Java 17+ e JUnit 5  
**ISO:** só citar. **LBI / eMAG:** não se testam neste laboratório (são qualidade em uso).

Não acesse https://bdcgetec.cps.sp.gov.br daqui. Não tente login, senha nem carga.

O desenvolvedor afirma:

> “O programa compilava ontem e a consulta estava funcionando.”

A classe `br.usjt.gqs.bdgetec.ConsultaEscolas` já está no projeto `consulta-escolas`.

## 1. Rodar o teste que já existe

Abra o projeto e execute `ConsultaEscolasTest`.

1. O teste `periodoAtualDevolveEscolas` passou ou falhou?
2. O que o teste **esperava**?
3. O que o código **fez**?
4. Isso prova que o produto tem qualidade suficiente para o período `2026/2`? Por quê?

## 2. Completar os testes

Na mesma classe de teste, implemente os métodos marcados com `TODO`. Cada um precisa falhar enquanto o defeito existir (barra vermelha) — não “ajuste o teste para passar”.

| TODO | O que o teste deve garantir |
|---|---|
| 1 | `buscar(new String("NRA1"), "2026/2")` devolve as três escolas. Não use o literal `"NRA1"` neste teste. |
| 2 | `contar(regional, periodo)` é igual a `buscar(regional, periodo).size()` para o período atual **e** para um período vazio. |
| 3 | `listarLinhas("NRA1")` devolve 3 linhas e **não** lança exceção. |

## 3. Classificar a evidência

No caderno, uma letra por linha: **P** produto, **U** uso, **D** dados.

| # | Afirmação | Letra |
|---|---|---|
| 1 | O teste JUnit `periodoAtualDevolveEscolas` falhou. | P / U / D |
| 2 | Três pessoas só com teclado não abriram o menu Mapeamento no sítio. | P / U / D |
| 3 | `contar` devolve 3 quando `buscar` devolve lista vazia. | P / U / D |

## 4. Limite

Escreva uma frase que este laboratório **não** autoriza concluir. Exemplo do que não vale: “o BDGETEC em produção está correto” ou “o sítio é acessível”.
