# Web Scraping de Comentarios de Reddit (r/chile)

Este script de Python realiza web scraping de comentarios en la comunidad de Reddit r/chile. Utiliza Selenium, una biblioteca de automatización del navegador, para navegar por la página web y extraer los comentarios junto con la información del autor y la fecha. Los comentarios extraídos se almacenan en una base de datos Supabase.

## Funcionalidades

- Navega por la página de Reddit y carga los comentarios dinámicamente.
- Extrae los comentarios, el autor y la fecha de publicación.
- Almacena los datos en una estructura de lista para su posterior procesamiento.
- Inserta los comentarios extraídos en una base de datos Supabase.

## Requisitos

- Python 3.12.3
- Selenium
- WebDriver para Chrome (incluido en el repositorio)
- Supabase Python Client 

## Uso

1. Clona el repositorio o descarga el script `scrape_reddit_comments.py`.
2. Instala las dependencias de Python: `pip install selenium supabase`.
3. Ajusta la URL de Reddit en el script según sea necesario.
4. Proporciona la URL y la clave de tu instancia de Supabase.
5. Ejecuta el script.

## Estructura de la Base de Datos

La tabla `Comentarios` en la base de datos Supabase debe tener las siguientes columnas:

- `id_comentario` (bigint, int8)
- `usuario` (character varying, varchar)
- `comentario` (character varying, varchar)
- `fecha_com` (character varying, varchar)
- `minero` (character varying, varchar)
- `fecha_add` (character varying, varchar)

## Notas

- Es posible que necesites ajustar los selectores CSS si la estructura HTML de Reddit cambia.
- Asegúrate de configurar correctamente la URL y la clave de tu instancia de Supabase en el script.
- La KEY y url esta comentada para evitar que acceddan a la bd debido a la falta de metodos de validacion.