# Aula 03 — 03/09/2026

Oráculo `FAIL` na língua da máquina; produto vs processo.

## Imprimir / enviar

| Arquivo | Quem |
|---|---|
| `aluno.md` | 1 página · turma |
| `docente.md` | 1 página · você |
| `bartie-trecho.md` | WhatsApp / Moodle **antes** da aula |
| `oraculo.py` `oraculo.js` `Oraculo.java` | laboratório · o aluno abre **um** |

## Conferir os oráculos (devem falhar)

```bash
python3 oraculo.py ; echo exit:$?
node oraculo.js ; echo exit:$?
javac Oraculo.java && java Oraculo ; echo exit:$?
```

Esperado: uma linha `FAIL` e código `1` nos três.

Maven/JUnit **não** entram nesta noite. O projeto `../java-testes/consulta-escolas` continua sendo a fatia completa; estes três arquivos são o sotaque autocontido da sala.
