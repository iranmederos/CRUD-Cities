if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            ciudades: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://localhost:5000/ciudades'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.ciudades = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(ciudad) {
                const url = 'http://localhost:5000/ciudades/' + ciudad;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
