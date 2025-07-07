import { renderizar } from './filtros.js';

let ultimoTipo = 'jefe';
let ultimoData = [];

async function fetchData(url) {
  const res = await fetch(url);
  return await res.json();
}

// Marca el botón activo
function marcarActivo(tipo) {
  document
    .querySelectorAll('button[data-tipo]')
    .forEach(btn => {
      btn.classList.toggle('filtro-activo', btn.dataset.tipo === tipo);
    });
}

// Carga datos y refresca la vista
function actualizarVista(data, tipo) {
  ultimoTipo = tipo;
  ultimoData = data;

  marcarActivo(tipo);
  renderizar(data, document.getElementById('resultados'), tipo);

  console.log(`Vista '${tipo}' renderizada con ${data.length} ítems.`);
}

document.addEventListener('DOMContentLoaded', async () => {
  const data = await fetchData('/api/bosses');
  actualizarVista(data, 'jefe');
});

// Cuando hago click en cualquiera de los botones de filtro
document.querySelectorAll('button[data-tipo]').forEach(btn => {
  btn.addEventListener('click', async () => {
    const tipo = btn.dataset.tipo;
    if (tipo === ultimoTipo) return;            
    const rutas = {
      jefe:     '/api/bosses',
      objeto:   '/api/items',
      monstruo: '/api/creatures',
      npc:      '/api/npcs'
    };
    const data = await fetchData(rutas[tipo]);
    actualizarVista(data, tipo);
  });
});

// Ordenar al cambiar el select
document.getElementById('ordenSelect').addEventListener('change', () => {
  if (!ultimoData.length) return;
  renderizar(ultimoData, document.getElementById('resultados'), ultimoTipo);
});

// Filtro dinamico
document.getElementById('barraBusqueda').addEventListener('input', e => {
  const texto = e.target.value.toLowerCase();
  const filtrado = ultimoData.filter(o =>
    (o.name || '').toLowerCase().includes(texto) ||
    (o.description || '').toLowerCase().includes(texto) ||
    (o.location || '').toLowerCase().includes(texto) ||
    (o.drops || '').toLowerCase().includes(texto) ||
    (o.quote || '').toLowerCase().includes(texto)
  );
  renderizar(filtrado, document.getElementById('resultados'), ultimoTipo);
});
