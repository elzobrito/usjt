// Fatia didatica — consulta de escolas. Nao e o sitio BDGETEC. Sem HTTP.
// NAO "consertar" buscar/contar/listar/ativas hoje.
// Execute um comando por vez; consulte aluno.md.

const ESCOLAS_NRA1 = ["Etec Sao Paulo", "Etec Zona Leste", "Etec de Artes"];
const PERIODO_CASO = "2026/2";

function buscar(regional, periodo) {
  if (regional === "NRA1" && periodo === "2026/1") {
    return ESCOLAS_NRA1.slice();
  }
  return [];
}

function contar(regional, periodo) {
  buscar(regional, periodo);
  return 3;
}

function listar(regional) {
  const escolas = regional === "NRA1" ? ESCOLAS_NRA1.slice() : [];
  const linhas = [];
  for (let i = 0; i <= escolas.length; i++) {
    if (escolas[i] === undefined) {
      throw new Error("indice " + i + " fora da lista");
    }
    linhas.push(i + 1 + " - " + escolas[i]);
  }
  return linhas;
}

function ativas(regional, periodo) {
  return ESCOLAS_NRA1.slice();
}

function oraculoBuscar() {
  const obtido = buscar("NRA1", PERIODO_CASO);
  const ok = obtido.length > 0;
  console.log(ok ? "PASS" : "FAIL");
  return ok ? 0 : 1;
}

function oraculoContar() {
  // esperado independente: contar("XXX", "2026/2") === 0
  // TODO: implemente PASS/FAIL + return 0/1. Nao altere as funcoes.
  console.log("TODO");
  return 2;
}

function mostrarRegional() {
  const casos = [
    ["NRA1", "2026/1"],
    ["nra1", "2026/1"],
    [" NRA1", "2026/1"],
  ];
  for (const [regional, periodo] of casos) {
    console.log(JSON.stringify(regional) + " + " + periodo + " -> " + buscar(regional, periodo).length);
  }
}

const cmd = process.argv[2] || "buscar";
if (cmd === "buscar") process.exit(oraculoBuscar());
if (cmd === "contar") {
  console.log(contar("NRA1", PERIODO_CASO));
  process.exit(0);
}
if (cmd === "listar") {
  console.log(listar("NRA1").join("\n"));
  process.exit(0);
}
if (cmd === "regional") {
  mostrarRegional();
  process.exit(0);
}
if (cmd === "ativas") {
  console.log(ativas("XXX", PERIODO_CASO).join(", "));
  process.exit(0);
}
if (cmd === "oraculo-contar") process.exit(oraculoContar());
console.log("uso: node consulta.js buscar|contar|listar|regional|ativas|oraculo-contar");
process.exit(2);
