# Web Scraping de Comentarios de Reddit (r/chile)

Este script de Python realiza web scraping de comentarios en la comunidad de Reddit r/chile. Utiliza Selenium, una biblioteca de automatización del navegador, para navegar por la página web y extraer los comentarios junto con la información del autor y la fecha.

## Funcionalidades

- Navega por la página de Reddit y carga los comentarios dinámicamente.
- Extrae los comentarios, el autor y la fecha de publicación.
- Almacena los datos en una estructura de lista para su posterior procesamiento.

## Requisitos

- Python 3.12.3
- Selenium
- WebDriver para Chrome (incluido en el repositorio)

## Uso

1. Clona el repositorio o descarga el script `scrape_reddit_comments.py`.
2. Instala las dependencias de Python: `pip install selenium`.
3. Ejecuta el script: `python scrape_reddit_comments.py`.

## Notas

- Es posible que necesites ajustar los selectores CSS si la estructura HTML de Reddit cambia.
