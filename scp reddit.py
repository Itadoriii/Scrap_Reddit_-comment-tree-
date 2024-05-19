from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from supabase import create_client, Client
from datetime import datetime

minero = 'Sebastian Castro'
#-----CONFIGURACIONES SELENIUM-----

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
#-----DESCOMENTAR Y CAMBIAR URL DE SCRAPING-----
#driver.get("https://www.reddit.com/r/chile/comments/1csug68/la_normalizaci%C3%B3n_de_las_drogas_est%C3%A1_dejando_la/")

#-----Funcion para hacer scroll a la parte inferior de la pagina y esperar 3 segundos-----
def Scroll_Down_Page():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

#-----Funcion que presiona un boton de comentarios-----
def Presionar_boton_mas_comentarios():
    try:
        boton = driver.find_element(By.CSS_SELECTOR, "#comment-tree > faceplate-partial > div:nth-child(2) > button")
        boton.click()
        time.sleep(3)
        print('Boton presionado')
        Scroll_Down_Page()
        return True
    except:
        return False

#-----Carga primeros comentarios-----
for _ in range(2):
    Scroll_Down_Page()

#-----Verifica la existencia del boton mas comentarios y de existir lo presiona hasta que no encuentre uno-----
while Presionar_boton_mas_comentarios():
    pass
print('No hay botón de más comentarios: esperando para scrapear datos')

#-----Se buscan los comentarios a traves de un selector css y se define un arreglo para guardarlos -----
comentarios = driver.find_elements(By.CSS_SELECTOR, "#comment-tree > shreddit-comment")
comentarios_array = []

#-----Se recupera el usuario y comentario a traves de un selector css-----
for comentario in comentarios:
    try:
        autor_element = comentario.find_element(By.CSS_SELECTOR, "div > div > div > faceplate-hovercard > div.flex.flex-row.items-center.overflow-hidden > faceplate-tracker > a")
        autor_comentario = autor_element.get_attribute("innerHTML")
    except:
        continue
    texto_comentario = comentario.find_element(By.CSS_SELECTOR, ".md").text

#-----Se recupera la fecha a traves de un selector css-----
    try:
        fecha_element = comentario.find_element(By.CSS_SELECTOR, "a > faceplate-timeago > time")
        fecha_comentario = fecha_element.get_attribute("title")
    except:
        fecha_comentario = "Fecha no disponible"
    
    #print(f"Autor: {autor_comentario}")
    #print(f"Comentario: {texto_comentario}")
    #print(f"Fecha: {fecha_comentario}")
    #print()
#-----Se guardan los datos solo si existen (en la lista commentarios_array)-----
    if autor_comentario and texto_comentario and fecha_comentario:
            comentarios_array.append({
                "autor": autor_comentario,
                "comentario": texto_comentario,
                "fecha": fecha_comentario
            })

driver.quit()
print(comentarios_array)
print('Cantidad de comentarios =', len(comentarios_array))


#-----Guardar los comentarios limpios en una base de datos -----
url = ""
key = ""

supabase = create_client(url, key)

def insertar_comentarios(comentarios_array, url, key, minero):
    try:
        for comentario in comentarios_array:
            supabase.table('Comentarios').insert({
                'usuario': comentario['autor'],
                'comentario': comentario['comentario'],
                'fecha_com': comentario['fecha'],
                'minero': minero,  # Agregar el minero al comentario
                'fecha_add': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }).execute()

        print("Comentarios a;adidos .")
    
    except Exception as e:
        print("Error :", e)

#insertar_comentarios(comentarios_array,url,key,minero) ESTA COMENTADO PORQUE NECESITA METODOS DE VALIDACION (QUE NO SE REPITA LA URL) 
