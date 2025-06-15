export function activarBuscador(callback) {
  const form = document.getElementById("formBusqueda");
  const input = document.getElementById("barraBusqueda");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const termino = input.value.toLowerCase();
    const res = await fetch("/api/bosses");
    const data = await res.json();
    const filtrado = data.filter(b => b.name.toLowerCase().includes(termino));
    callback(filtrado);
  });
}
