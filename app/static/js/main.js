import { cargarBosses, cargarItems, cargarCreatures, cargarNpcs } from './filtros.js';

document.addEventListener("DOMContentLoaded", () => {
  cargarBosses(); // carga inicial

  document.querySelector("button[data-tipo='jefes']").addEventListener("click", cargarBosses);
  document.querySelector("button[data-tipo='objetos']").addEventListener("click", cargarItems);
  document.querySelector("button[data-tipo='monstruos']").addEventListener("click", cargarCreatures);
  document.querySelector("button[data-tipo='npc']").addEventListener("click", cargarNpcs);
});
