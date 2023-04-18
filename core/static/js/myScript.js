const searchInput = document.getElementById('search');
const veiculosDiv = document.getElementById('veiculos');

searchInput.addEventListener('keyup', (event) => {
  const query = event.target.value;
  fetch(`/veiculos/buscar?placa=${query}`)
    .then(response => response.json())
    .then(veiculos => {
      veiculosDiv.innerHTML = '';
      veiculos.forEach(veiculo => {
        const div = document.createElement('div');
        div.innerHTML = `
          <p>Placa: ${veiculo.placa}</p>
          <p>Data de entrada: ${veiculo.data_entrada}</p>
        `;
        veiculosDiv.appendChild(div);
      });
    })
    .catch(error => console.error(error));
});
