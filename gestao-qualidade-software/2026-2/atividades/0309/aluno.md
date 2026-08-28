# Aula 03 — O oráculo que falha

**UC:** Gestão da Qualidade de Software (0006960)  
**Data:** 03/09/2026 · quinta  
**Produto:** fatia local da consulta de escolas (não é o sítio BDGETEC)  
**Língua:** a que a máquina responder (`python3`, `node` ou `javac`)

Não acesse https://bdcgetec.cps.sp.gov.br. Não tente login, senha nem carga.

---

No quadro:

> Três escolas voltaram. O oráculo do período **2026/2** passa?

## 1. Protocolo (preencha antes de rodar)

| Peça | Neste caso |
|---|---|
| Dado | regional `NRA1`, período do caso `2026/2` |
| Ação | `consultar(regional, periodo)` no arquivo da sua língua |
| Oráculo | a lista **não** pode vir vazia |
| Evidência | a linha `PASS` ou `FAIL` + código de saída 0 ou 1 |

Comando (só o da máquina):

```text
python3 oraculo.py
node oraculo.js
javac Oraculo.java && java Oraculo
```

Sem interpretador: complete a tabela no papel. O script entra na Aula 08.

**Não corrija a função hoje.** O artefato da noite é o `FAIL`.

Saída que você viu: `PASS` / `FAIL` / papel  
Código de saída (se houver): ______

## 2. Uma letra por linha

**P** produto · **R** processo · **U** uso

| # | Afirmação | Letra |
|---|---|---|
| 1 | O oráculo do período 2026/2 imprimiu `FAIL`. | |
| 2 | Combinamos reler este oráculo quando o período mudar. | |
| 3 | Três pessoas só com teclado não abriram o menu Mapeamento no sítio. | |

## 3. Ticket (3 linhas)

1. Em uma frase: o que o `FAIL` prova?  
2. Em uma frase: o que o `FAIL` **não** prova?  
3. Qual letra faltou na sua tabela, e por quê?

Leve o arquivo (ou a foto da tabela) — é peça 1 do kit A3.
