const searchInput = document.getElementById('search');
const veiculosDiv = document.getElementById('veiculos');

$(document).ready(function () {
  $('#search-button').click(function () {
    var placa = $('#placa-search').val().toUpperCase();
    $('tbody tr').hide();
    $('tbody tr').each(function () {
      var placaVeiculo = $(this).find('td:eq(1)').text().toUpperCase();
      if (placaVeiculo.startsWith(placa)) {
        $(this).show();
      }
    });
  });
});