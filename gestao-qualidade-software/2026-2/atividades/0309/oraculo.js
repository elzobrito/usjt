// esperado: consultar("NRA1", "2026/2") devolve escolas (lista nao vazia)
// Fatia didatica. Nao e o sitio BDGETEC. Sem HTTP.

function consultar(regional, periodo) {
  if (regional === "NRA1" && periodo === "2026/1") {
    return ["Etec Sao Paulo", "Etec Zona Leste", "Etec de Artes"];
  }
  return [];
}

const PERIODO_CASO = "2026/2";
const obtido = consultar("NRA1", PERIODO_CASO);
const ok = obtido.length > 0;
console.log(ok ? "PASS" : "FAIL");
process.exit(ok ? 0 : 1);
