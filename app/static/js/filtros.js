export async function cargarBosses() {
  const contenedor = document.getElementById("resultados");
  const res = await fetch("/api/bosses");
  const data = await res.json();
  renderizar(data, contenedor, "jefe");
}

export async function cargarItems() {
  const contenedor = document.getElementById("resultados");
  const res = await fetch("/api/items");
  const data = await res.json();
  renderizar(data, contenedor, "objeto");
}

export async function cargarCreatures() {
  const contenedor = document.getElementById("resultados");
  const res = await fetch("/api/creatures");
  const data = await res.json();
  renderizar(data, contenedor, "monstruo");
}

export async function cargarNpcs() {
  const contenedor = document.getElementById("resultados");
  const res = await fetch("/api/npcs");
  const data = await res.json();
  renderizar(data, contenedor, "npc");
}



function renderizar(lista, contenedor, tipo = "jefe") {
  const orden = document.getElementById("ordenSelect").value;

  if (orden === "az") {
    lista.sort((a, b) => a.name.localeCompare(b.name));
  } else if (orden === "za") {
    lista.sort((a, b) => b.name.localeCompare(a.name));
  }

  contenedor.innerHTML = "";

  const badgeClases = {
    jefe: "badge",
    objeto: "badge objeto",
    monstruo: "badge monstruo",
    npc: "badge npc"
  };

  lista.forEach(e => {
    const card = document.createElement("div");
    card.className = "tarjeta";

    card.innerHTML = `
      <div class="tarjeta-cabecera">
        <h3>${e.name}</h3>
        <span class="${badgeClases[tipo]}">${tipo.charAt(0).toUpperCase() + tipo.slice(1)}</span>
      </div>
      ${e.image ? `<img src="${e.image}" alt="${e.name}">` : ""}
      ${e.description ? `<p>${e.description}</p>` : ""}
      ${e.location ? `<p><strong>Ubicación:</strong> ${e.location}</p>` : ""}
      ${e.quote ? `<p><em>${e.quote}</em></p>` : ""}
      ${e.drops ? `<p><strong>Drops:</strong> ${e.drops}</p>` : ""}
      ${e.effect ? `<p><strong>Efecto:</strong> ${e.effect}</p>` : ""}
      ${e.type ? `<p><strong>Tipo:</strong> ${e.type}</p>` : ""}
    `;

    contenedor.appendChild(card);
  });
}

export { renderizar };

