$(document).ready(function() {
  table = $('#tabela').DataTable( {
      "columnDefs": [
          {
              "targets": [ 5 ],
              "visible": false,
              "searchable": false
          },
      ]
  } );
} );