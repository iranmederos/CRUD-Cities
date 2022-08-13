var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtNombre2").value = parts[1][1]
document.getElementById("txtImagen2").value = parts[2][1]
document.getElementById("txtDescripcion2").value = parts[3][1]




function modificar() {
    let id = document.getElementById("txtId").value
    let n = document.getElementById("txtNombre2").value
    let d = document.getElementById("txtDescripcion2").value
    let img = document.getElementById("txtImagen2").value
    let ciudad = {
        nombre: n,
        descripcion: d,
        imagen: img
    }
    let url = "http://localhost:5000/ciudades/" + id
    var options = {
        body: JSON.stringify(ciudad),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })
}
