# Phascot

Este proyecto es una aplicación web de catálogo de zapatillas llamada **StepUp**, desarrollada como ejercicio académico para una materia universitaria.

## Descripción

El sistema consiste en un backend realizado en Java usando el framework Javalin, el cual se encarga de servir archivos estáticos y gestionar rutas básicas para las diferentes secciones de la tienda. El frontend está construido en HTML y CSS, con un diseño responsivo y ejemplos de productos, categorías y marcas populares.

## Estructura del Proyecto

```
phascot/
└── demo/
    ├── src/
    │   └── main/
    │       ├── java/
    │       │   └── electiva/
    │       │       └── taller/
    │       │           └── Server/
    │       │               └── Servidor.java
    │       └── resources/
    │           └── Public/
    │               ├── index.html
    │               ├── styleet.css
    │               └── img/
    └── target/
        └── classes/
            └── Public/ (idéntico al de resources)
```

- **Servidor.java:** Contiene la lógica del servidor y define las rutas de la aplicación.
- **index.html:** Página principal del catálogo.
- **styleet.css:** Hojas de estilo para el frontend.
- **img/**: Carpeta con imágenes de productos y marcas.

## Instalación y Ejecución

1. Clona este repositorio.
2. Asegúrate de tener Java instalado.
3. Abre el proyecto en tu IDE y ejecuta la clase `Servidor.java`.
4. Accede a `http://localhost:7000/` en tu navegador.

## Funcionalidad

- **Rutas principales:**
  - `/` → Redirige a `/Public/index.html`
  - `/hombre`, `/mujer`, `/niños`, `/marcas`, `/ofertas`, `/cuenta`, `/carrito` → Secciones de la tienda (por ahora muestran mensajes estáticos).
  - `/buscar?q=palabra` → Simula una búsqueda.
  - `/running`, `/casual`, `/nike`, `/adidas`, `/puma` → Categorías y marcas.
  - `/test` → Responde con texto plano para probar el servidor.

- **Frontend:**
  - Página principal con productos destacados, categorías y marcas populares.
  - Navegación simple, buscador (no funcional a nivel de backend), enlaces a secciones y marcas.
  - Footer con enlaces rápidos y formulario de suscripción (no funcional).

## Créditos

- Imágenes de productos obtenidas de Unsplash y otras fuentes libres.
- Desarrollado como parte de una materia universitaria.

---