# Readme
<p>
Este es el documento de diseño central y diario de registro para el reto de ZIENideas realizado en el campus 42 de Málaga.
<p>
Como identificativo, este proyecto ha sido redactado por **Laureano Cuevas (lcuevas-) en 42**.  
Aunque se ha trabajado en concierto con otros compañeros, la entrega se ha realizado de forma dividida para su revisión.

<p>
La idea central es realiar un cuentacuentos bajo unos parámetros determinados. En este documento se narrará el flujo de trabajo realizado para el producto.
</p>



<h2>Primeros pasos</h2>
<p>Como se nos ha sugerido lo primero es montar un esquema de trabajo con los tiempos necesarios, esto es lo que se nos recomienda:</p>
<ul>
<li>Fase 1: Entrada de Datos<br>
Recibir el input del relato de forma simple (archivo, línea de comandos o formulario). 15–20 min</li>
<li>Fase 2: Validación<br>
Verificar que el texto cumple con los criterios: longitud de ~500 palabras (±10%), estructura en 3 partes (presentación, nudo, desenlace) y al menos 3 personajes distintos. 30–40 min</li>
<li>Fase 3: Iteración y Trazas<br>
Repetir el proceso de generación o ajuste hasta cumplir los criterios de validación. Se deben dejar logs o trazas que muestren las iteraciones. 40–50 min</li>
<li>Fase 4: Exportación a PDF<br>
Exportar el relato final en un archivo PDF (sin necesidad de portada en esta fase). 15–20 min (Opcional)</li>
<li>Fase 5: Portada Automática<br>
Generar una portada simple relacionada con el tema del relato y añadirla al PDF final. 15–20 min (Opcional)</li>
  </ul>

<p>Siguinedo esta lista de trabajo inicial empezaremos el flujo de trabajo que se nos recomienda igualmente:<br>
[Entrada] -> [Generación] -> [Validación] -> [Iteración] -> [Exportación] -> [Portada]
</p>

<p>El lenguaje base sera python por familiaridad con el mismo y se procederá a ralizar durante la siguiente fase del trabajo un programa capaz de recibir el imput necesario.</p>

EL flujo de trabajo presentado es bastante útil como estructura básica. Así que se intentarán hacer varios pasos repetitivos.
[Prompt] -> [Generación] -> [Validación] -> [Iteración] -> [Exportación] -> [Portada]



<h2>Preparación del promt</h2>
<p>Los primeros comits presentan un programa capaz de extraer el imput e integrarlo en un json junto con una serie de reglas para la IA generativa. Iniciamos segunda gase del proceso para la generación del cuento</p>
<p>Para esto solo necesitamos un import json en python</p>

<h2>Preparación del promt</h2>
<p>El siguiente paso de trabajo es intentar mandar dicho prompt a una IA generativa capaz de interpretarlo para devolver el cuento en unas 500 palabras. EL mismo promt lleva una serie de limitaciones e instrucciones añadidas para ello.</p>
<p>Para mantener una aproximacion minima sin instalaciones hemos importado urllib.request para la conexión con los modelos, pudiendo usar nuestra API key de forma local </p>

<h2>Validación</h2>
<p>Llegados a este punto la idea era poder obtener un resultado e iniciar ingeniría de prompts para lograr un resultado deseado y despues pasar a importar a PDF. Lamentablemente no hemos podido hacer funcionar las APIs</p>

<h2>Exportación</h2>
<p>Se ejecutaría de forma simple con pdf-lib</p>





