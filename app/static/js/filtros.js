export async function cargarBosses() {
  const contenedor = document.getElementById("resultados");
  const res = await fetch("/api/bosses");
  const data = await res.json();
  renderizar(data, contenedor);
}

export async function cargarItems() {
  const contenedor = document.getElementById("resultados");
  const res = await fetch("/api/items");
  const data = await res.json();
  renderizar(data, contenedor);
}

// Agrega las demás funciones aquí...

function renderizar(lista, contenedor) {
  contenedor.innerHTML = "";
  lista.forEach(e => {
    const card = document.createElement("div");
    card.className = "tarjeta";

    card.innerHTML = `
      <div class="tarjeta-cabecera">
        <h3>${e.name}</h3>
        <span class="badge">Jefe</span>
      </div>
      ${e.image ? `<img src="${e.image}" alt="${e.name}">` : ""}
      <p>${e.description || "Sin descripción disponible."}</p>
      ${e.location ? `<p><strong>Ubicación:</strong> ${e.location}</p>` : ""}
      ${e.drops ? `<p><strong>Drops:</strong> ${e.drops}</p>` : ""}
    `;

    contenedor.appendChild(card);
  });
}

