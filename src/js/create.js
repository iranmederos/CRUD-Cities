function guardar() {
 
    let n = document.getElementById("txtNombre").value
    let d = document.getElementById("txtDescripcion").value
    let img = document.getElementById("txtimagen").value
 
    let ciudad = {
        nombre: n,
        descripcion: d,
        imagen: img
    }
    let url = "http://localhost:5000/ciudades"
    var options = {
        body: JSON.stringify(ciudad),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
 
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}
