import { cargarBosses, cargarItems, cargarCreatures, cargarNpcs } from './filtros.js';

document.addEventListener("DOMContentLoaded", () => {
  cargarBosses(); // carga inicial
  marcarActivo("jefes");

  document.querySelector("button[data-tipo='jefes']").addEventListener("click", () => {
    cargarBosses();
    marcarActivo("jefes");
  });

  document.querySelector("button[data-tipo='objetos']").addEventListener("click", () => {
    cargarItems();
    marcarActivo("objetos");
  });

  document.querySelector("button[data-tipo='monstruos']").addEventListener("click", () => {
    cargarCreatures();
    marcarActivo("monstruos");
  });

  document.querySelector("button[data-tipo='npc']").addEventListener("click", () => {
    cargarNpcs();
    marcarActivo("npc");
  });
});

function marcarActivo(tipo) {
  const botones = document.querySelectorAll("button[data-tipo]");
  botones.forEach(btn => btn.classList.remove("filtro-activo"));

  const botonActivo = document.querySelector(`button[data-tipo='${tipo}']`);
  if (botonActivo) {
    botonActivo.classList.add("filtro-activo");
  }
}
