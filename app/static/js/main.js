import { renderizar } from './filtros.js';

let ultimoTipo = "jefe";
let ultimoData = [];

document.addEventListener("DOMContentLoaded", async () => {
  const data = await fetchData("/api/bosses");
  actualizarVista(data, "jefe");
});

document.querySelectorAll("button[data-tipo]").forEach(btn => {
  btn.addEventListener("click", async () => {
    const tipo = btn.getAttribute("data-tipo");
    const rutas = {
      jefe: "/api/bosses",
      objeto: "/api/items",
      monstruo: "/api/creatures",
      npc: "/api/npcs"
    };
    const data = await fetchData(rutas[tipo]);
    actualizarVista(data, tipo);
  });
});

document.getElementById("ordenSelect").addEventListener("change", () => {
  if (ultimoData.length > 0) {
    renderizar(ultimoData, document.getElementById("resultados"), ultimoTipo);
  }
});

function marcarActivo(tipo) {
  document.querySelectorAll("button[data-tipo]").forEach(btn => {
    btn.classList.remove("filtro-activo");
    if (btn.getAttribute("data-tipo") === tipo) {
      btn.classList.add("filtro-activo");
    }
  });
}

function actualizarVista(data, tipo) {
  ultimoTipo = tipo;
  ultimoData = data;
  marcarActivo(tipo);
  renderizar(data, document.getElementById("resultados"), tipo);
}

async function fetchData(url) {
  const res = await fetch(url);
  return await res.json();
}
