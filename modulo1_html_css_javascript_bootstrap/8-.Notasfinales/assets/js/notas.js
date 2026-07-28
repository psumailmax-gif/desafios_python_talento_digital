let nombre = prompt("Ingrese su nombre ");
        let carrera = prompt("Ingrese su carrera");
        let notaUno = prompt("Ingrese nota 1");
        let notaDos = prompt("Ingrese nota 2");
        let notaTres = prompt("Ingrese nota 3");
        let promedio =(parseFloat(notaUno)+parseFloat(notaDos)+parseFloat(notaTres))/3;

        let notaUnocss = prompt("Ingrese nota 1 css");
        let notaDoscss = prompt("Ingrese nota 2 css");
        let notaTrescss = prompt("Ingrese nota 3 css");
        let promedioCss =(parseFloat(notaUnocss)+parseFloat(notaDoscss)+parseFloat(notaTrescss))/3;

        let notaUnojs = prompt("Ingrese nota 1 js");
        let notaDosjs = prompt("Ingrese nota 2 js");
        let notaTresjs = prompt("Ingrese nota 3 js");
        let promedioJs =(parseFloat(notaDosjs)+parseFloat(notaDosjs)+parseFloat(notaTresjs))/3;

        document.writeln("<h1>Notas finales</h1>");
        document.writeln("<h6> Nombre: "+nombre+"</h6>");
        document.writeln("<h6> Carrera: "+carrera+"</h6>");
        document.writeln("<table border=\"1\">")
        document.writeln("<tr><th>Ramo</th><th>Nota 1</th><th>Nota 2</th><th>Nota 3</th><th>Promedio</th></tr>")
        document.writeln("<tr><th>Html</th><td>"+notaUno+
            "</td><td>"+notaDos+
            "</td><td>"+notaTres+
            "</td><td>"+promedio+
            "</td></tr>")
        document.writeln("<tr><th>css</th><td>"+notaUnocss+
            "</td><td>"+notaDoscss+
            "</td><td>"+notaTrescss+
            "</td><td>"+promedioCss+
            "</td></tr>")
        document.writeln("<tr><th>Js</th><td>"+notaUnojs+
            "</td><td>"+notaDosjs+
            "</td><td>"+notaTresjs+
            "</td><td>"+promediojs+
            "</td></tr>")
            document.writeln("</table>")
