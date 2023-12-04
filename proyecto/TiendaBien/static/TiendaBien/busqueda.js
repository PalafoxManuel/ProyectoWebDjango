document.addEventListener('DOMContentLoaded', function () {
    const nombreUsuario = localStorage.getItem('nombreUsuario');
    const labelNombreUsuario = document.getElementById('nombreUsuario');
    labelNombreUsuario.textContent = nombreUsuario;

    const usuariosRegistrados = JSON.parse(localStorage.getItem('usuarios')) || [];
    const usuarioActual = usuariosRegistrados.find(usuario => usuario.correo === localStorage.getItem('correo'));

    const producto = {
        crearProducto: function (urlImagen, nombre, precio,id) {
            return {
                urlImagen: urlImagen,
                nombre: nombre,
                precio: precio,
                idProducto: id,
                cantidad: 1
            };
        },
        agregarAlCarrito: function (usuarioActual, nuevoProducto) {
            // Verificar si usuarioActual es undefined antes de acceder a su propiedad carrito
            if (usuarioActual && usuarioActual.carrito) {
                const productoEnCarrito = usuarioActual.carrito.find(producto => producto.idProducto === nuevoProducto.idProducto);

                if (productoEnCarrito) {
                    productoEnCarrito.cantidad += 1;
                } else {
                    usuarioActual.carrito.push(nuevoProducto);
                }

                const index = usuariosRegistrados.findIndex(u => u.correo === usuarioActual.correo);
                if (index !== -1) {
                    usuariosRegistrados[index] = usuarioActual;
                }

                localStorage.setItem('usuarios', JSON.stringify(usuariosRegistrados));

                alert('Producto agregado al carrito');
            } else {
                console.error('El usuario actual no está definido o no tiene la propiedad "carrito".');
            }
        }
    };
    const btnAgregarCarrito = document.querySelectorAll('.agregarCarritoBtn');
    btnAgregarCarrito.forEach(btn => {
        btn.addEventListener('click', function () {
            const idProducto = this.getAttribute('data-producto-id');
            const nombreProducto = this.getAttribute('data-producto-nombre');
            const precio = this.getAttribute('data-producto-precio');
            const urlImagen = this.getAttribute('data-producto-urlimagen');

            const nuevoPro = producto.crearProducto(urlImagen,nombreProducto,precio,idProducto);
            producto.agregarAlCarrito(usuarioActual, nuevoPro);
            console.log('Producto agregado al carrito con ID:', idProducto);
        });
    });

    const btnComprar = document.querySelectorAll('.compraBtn');

    btnComprar.forEach(btn => {
        btn.addEventListener('click', function () {
            const idProducto = this.getAttribute('data-producto-id');
            const nombreProducto = this.getAttribute('data-producto-nombre');
            const precio = this.getAttribute('data-producto-precio');
            const urlImagen = this.getAttribute('data-producto-urlimagen');

            const nuevoPro = producto.crearProducto(urlImagen,nombreProducto,precio,idProducto);
            producto.agregarAlCarrito(usuarioActual, nuevoPro);
            window.location.href = "{% url 'carrito' %}";
            console.log('Redirigiendo a la página del carrito');
        });
    });
});
