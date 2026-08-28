# Aula 04 — 10/09/2026

Pacote PCA 0.3 corrigido, versão 2, em estado `draft` e com `quality_status: pass`:

`../../../artifacts/aula-04-revisao-codigo/20260828T181834Z/`

Superfície docente consolidada:

`../../../artifacts/aula-04-revisao-codigo/20260828T181834Z/build/pacote_aula.html`

## Materiais

| Arquivo | Uso |
|---|---|
| `aluno.md` | duas passagens: revisão estática e validação dinâmica |
| `docente.md` | gabarito, intervenções e decisões de corte |
| `fala_docente_completa.md` | condução pronunciável dos 200 minutos |
| `bartie-guia-revisao.md` | síntese autoral da fonte principal |
| `rubrica.md` | avaliação formativa em três níveis |
| `consulta.py`, `consulta.js`, `Consulta.java` | fatias locais com cinco defeitos intencionais |

## Execução

Use uma linguagem e execute um comando por vez. Não acesse HTTP e não corrija as funções nesta aula.

```text
python3 consulta.py buscar
python3 consulta.py contar
python3 consulta.py listar
python3 consulta.py regional
python3 consulta.py ativas
```

Os equivalentes de Node e Java estão na folha do aluno. O arquivo `Consulta.class` preexistente não é material canônico; compile a fonte em diretório temporário quando precisar validar Java.
