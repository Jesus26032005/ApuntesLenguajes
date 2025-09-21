// Document write
//es un método del objeto document que sirve para escribir contenido HTML o texto directamente en la página mientras se está cargando el documento.
//El contenido se puede escribir como texto simple o HTML.
//Todo lo que pongas se insertará en el flujo del documento en el momento de ejecución.
/*
Características importantes

Se usa principalmente al cargar la página.
Si lo llamas después de que la página haya cargado, borra todo el contenido existente.
Acepta HTML y texto.
document.write("<b>Negrita</b> y texto normal");


Se puede usar con variables:
const nombre = "Duda";
document.write("<p>Hola, " + nombre + "!</p>");

Se puede combinar con saltos de línea:
document.write("Linea 1<br>");
document.write("Linea 2<br>");
*/