## Básico
### Cosas importantes a tener en cuenta al escribir tus programas:

Python distingue entre mayúsculas y minúsculas, por lo que es importante que uses el caso correcto; de lo contrario, tu código no funcionará.

Los valores de texto deben aparecer entre comillas ("), pero los números no.

Al nombrar variables (es decir, valores en los que deseas almacenar datos), no puedes utilizar palabras reservadas como `print`, `input`, etc., de lo contrario, tu código no funcionará.

Cuando guardes tus archivos, no los guardes con palabras reservadas que Python ya utilice, como `print`, `input`, etc. Si lo haces, no se ejecutará y tendrás que renombrar el archivo antes de que funcione.

**Códigos de ejemplo**

```python
num1 = 93
```

Establece el valor de una variable. Si no existe una variable ya creada, creará una. Una variable es un contenedor para un valor (en este caso, la variable se llamará "num1" y almacenará el valor 93). El valor almacenado en la variable puede cambiar mientras el programa se esté ejecutando. La variable puede tener el nombre que desees (excepto palabras reservadas de Python como `print`, `save`, etc.) y debe comenzar con una letra en lugar de un número o símbolo y no debe contener espacios.

```python
respuesta = num1 + num2 
```
Suma num1 y num2 y almacena la respuesta en una variable llamada respuesta.

```python
respuesta = num1 - num2
```

Resta num2 de num1 y almacena la respuesta en una variable llamada respuesta.

```python
respuesta = num1 * num2 
```

Multiplica num1 por num2 y almacena la respuesta en una variable llamada respuesta.

```python
respuesta = num1 / num2
```

Divide num1 por num2 y almacena la respuesta en una variable llamada answer.

```python
respuesta = num1 // num2
```
Una división de números enteros (es decir, 9//4 = 2) y almacena la respuesta en una variable llamada respuesta.

```python
print("Este es un mensaje")
```

Muestra el mensaje entre paréntesis. Como el valor que queremos mostrar es un valor de texto, tiene comillas, las cuales no se mostrarán en la salida. Si quisieras mostrar un valor numérico o el contenido de una variable, las comillas no son necesarias.

```python
print("Primera línea\nSegunda Línea")
```

**\n** se utiliza como un salto de línea.

```python
texto = input("Ingresa un texto: ")
```

Muestra la pregunta "Ingresa un texto: " y almacena el valor que el usuario ingresa en una variable llamada texto. El espacio después de los dos puntos permite agregar un espacio antes de que el usuario ingrese su respuesta, de lo contrario, aparecerían juntos de manera poco atractiva.

```python
print("La respuesta es", respuesta)
```

Muestra el texto "La respuesta es" y el valor de la variable `respuesta`.

```python
num = int(input("Ingresa un número: "))
```

Muestra la pregunta "Ingresa un número: " y almacena el valor como un número entero en una variable llamada `num`. Los enteros se pueden utilizar en cálculos, pero las variables almacenadas como texto no.

## Declaración If

**Las declaraciones `if`** permiten que tu programa tome una decisión y cambie la ruta que se toma a través del programa.

A continuación se muestra cómo se vería la declaración `if` para este diagrama de flujo en Python.

```python
if num1 > 10:
  print("Es mayor a 10")
if num1 == 10:
  print("Es igual a 10")
else:
print("Es menor a 10")
```

### Indentar líneas de código

La indentación es muy importante en Python ya que muestra las líneas que dependen de otras, como se muestra en el ejemplo anterior. Para indentar texto puedes usar la tecla **[Tab]** o puedes presionar la tecla **[espacio]** cinco veces. La tecla **[retroceso]** eliminará las indentaciones.

La primera línea de la declaración `if` prueba una condición, y si esa condición se cumple (es decir, la primera condición es verdadera) entonces se ejecutan las líneas de código directamente debajo de ella. Si no se cumple (es decir, la primera condición es falsa) se probará la segunda condición, si la hay, y así sucesivamente. A continuación se muestran ejemplos de los diferentes operadores de comparación y lógicos que puedes usar en la línea de condición de tu declaración `if`.

### Operadores de comparación

|Operador | Descripción|
|---------|------------|
| >       | Mayor que  |
| <       | Menor que  |
| >=      | Mayor o igual |
| <=      | Menor o iguak |
| ==      | Igual      |
| !=      | No igual   |

### Operadores Lógicos

|Operador | Descripción|
|---------|------------|
|and      | Ambas condiciones deben cumplirse|
|or       | Una de las condiciones debe cumplirse|

**Ejemplos**

En los ejemplos de abajo, `num` es una variable ingresada por el usuario que ha sido almacenada como un entero.

```python
if num > 10:
  print("Esto está por encima de 10")
else:
  print("Esto está por debajo de 10")
```
Si `num` es mayor que 10, mostrará el mensaje "Esto está por encima de 10"; de lo contrario, mostrará el mensaje "Esto está por debajo de 10".

```python
if num > 10: 
  print(“Esto está por encima de 10”) 
elif num == 10: 
 print(“Esto es igual a 10”) 
else: 
 print(“Esto está por debajo de 10”)
```
Si `num` es mayor que 10, mostrará el mensaje "Esto está por encima de 10"; de lo contrario, verificará la siguiente condición. Si `num` es igual a 10, mostrará el mensaje "Esto es igual a 10". De lo contrario, si ninguna de las dos primeras condiciones se cumple, mostrará el mensaje "Esto está por debajo de 10".

```python
if num >= 10: 
  if num <= 20:
    print(“Esto está entre 10 and 20”) 
  else:
    print(“Esto esta por encima de 20”) 
else:
  print(“Esro está por debajo de 10”)
```

Si `num` es 10 o más, entonces probará otra declaración if para ver si `num` es menor o igual a 20. Si lo es, mostrará el mensaje "Esto está entre 10 y 20". Si `num` no es menor o igual a 20, entonces mostrará el mensaje "Esto está por encima de 20". Si num1 no es mayor a 10, mostrará el mensaje "Esto está por debajo de 10".

```python
texto = str.lower(texto)
```

Convierte el texto a minúsculas. Como Python distingue entre mayúsculas y minúsculas, esto convierte los datos ingresados por el usuario a minúsculas para que sea más fácil de verificar.

```python 
num = int(input(“Ingresa un número entre 10 y 20: ”)) 
if num >= 10 and num <= 20: 
 print(“Gracias”) 
else: 
 print(“Fuera de rango”)
```

Esto utiliza `and` para probar múltiples condiciones en la declaración `if`. Ambas condiciones deben cumplirse para producir la salida "Gracias".

```python
num = int(input(“Ingresa cualquier número entre 1 y 5: ”)) 
if num == 2 or num == 4: 
 print(“Gracias”) 
else: 
 print(“Incorrecto”)
```
Esto utiliza `or` para probar las condiciones en la declaración `if`. Solo una condición debe cumplirse para mostrar la salida "Gracias".

## Strings

*String* es el nombre técnico para las cadenas de texto. Para definir un bloque de código como una cadena, necesitas incluirlo entre comillas dobles (") o comillas simples ('). No importa cuál uses mientras seas consistente.

Hay algunos caracteres con los que necesitas tener cuidado al introducirlos en cadenas. Estos son:

" ' \

Esto se debe a que estos símbolos tienen significados especiales en Python y puede ser confuso si los usas en una cadena.

Si deseas usar uno de estos símbolos, necesitas precederlo con un símbolo de barra invertida y luego Python sabrá ignorar el símbolo y lo tratará como texto normal que se debe mostrar.

|Símbolo | En Python|
|--------|----------|
|"       |    \"    |
|'       |     \'   |
|\       |     \\\   |

### Cadenas y Números como Variables

Si defines una variable como una cadena, incluso si solo contiene números, no puedes luego usar esa cadena como parte de un cálculo. Si deseas usar una variable que ha sido definida como una cadena en un cálculo, tendrás que convertir la cadena a un número antes de que pueda ser usada.

```python
num = input("Ingresa un número: ")
total = num + 10
print(total)
```

En este ejemplo, se pide un número, pero no se ha definido como un valor numérico y cuando se ejecuta el programa, se obtendrá el siguiente error:

<!-- Aquí viene una imagen -->

Aunque este mensaje de error parece intimidante, simplemente está diciendo que la línea `total = num + 10` no está funcionando porque la variable num está definida como una cadena.

Este problema se puede resolver de una de dos maneras. Puedes definirlo como un número cuando la variable se está creando originalmente, usando esta línea:

```python
num = int(input("Ingresa un número: "))
```

o puedes convertirlo a un número después de que ha sido creado usando esta línea:

```python
num = int(num)
```

Lo mismo puede suceder con las cadenas.

```python
nombre = input("Ingresa un nombre: ")
num = int(input("Ingresa un número: "))
ID = nombre + num
print(ID)
```

En este programa, se le pide al usuario que ingrese su nombre y un número. Quieren que se unan y con las cadenas se utiliza el símbolo de adición como concatenación. Cuando se ejecuta este código, obtendrás un mensaje de error similar al anterior:

<!-- mensje de error -->

Para evitar esto, o bien no definas la variable como un número en primer lugar o conviértela a una cadena después usando la línea:

```python
num = str(num)
```

### Cadenas de Varias Líneas

Si deseas introducir una cadena en varias líneas, puedes usar el salto de línea **\n** o bien encerrar todo en comillas triples. Esto preservará el formato del texto.

```python
direccion = """123 Long Line
Oldtown
AB1 23CD"""
print(direccion)
```

**Códigos de ejemplo**

En los siguientes ejemplos, los términos "palabra", "frase", "nombre", "apodo" y "apellido" son todos nombres de variables.

```python
len(palabra)
```

Encuentra la longitud de la variable llamada word.

```python
palabra.upper()
```

Convierte la cadena en mayúsculas.

```python
palabra.lower()
```

Convierte la cadena en minúsculas.

```python
print(palabra.capitalize())
```

Muestra la variable de modo que solo la primera palabra tenga una letra mayúscula al principio y todo lo demás esté en minúsculas.

```python
nombre_completo= nombre + apellido
```

Une el nombre y el apellido sin un espacio entre ellos, conocido como concatenación.

```python
palabra.title()
```

Cambia una frase para que cada palabra tenga una letra mayúscula al principio y el resto de las letras en minúsculas (es decir, Mayúscula Inicial).

```python
texto = " Este es un texto. "  
print(texto.strip(" "))
```

Elimina caracteres adicionales (en este caso, espacios) del principio y del final de una cadena.

```python
print ("Hola Mundo"[7:10])
```
Cada letra se asigna un número de índice para identificar su posición en la frase, incluyendo el espacio. Python comienza a contar desde 0, no desde 1.

Por lo tanto, en este ejemplo, mostraría el valor de las posiciones 7, 8 y 9, que es "orl".

## Matemáticas

Python puede realizar varias funciones matemáticas, pero estas solo están disponibles cuando los datos se tratan como un número entero (integer) o un número con punto decimal (float). Si los datos se almacenan como una cadena, incluso si solo contiene caracteres numéricos, Python no puede realizar cálculos con ella.

**Código de ejemplo**

**Nota**: Ten en cuenta que, para usar algunas de las funciones matemáticas (`math.sqrt(num)` y `math.pi`) necesitarás importar la **biblioteca math** al principio de tu programa. Puedes hacer esto escribiendo `import math` en la primera línea del programa.

```python
print(round(num,2))
```

Muestra un número redondeado a dos lugares decimales.

```python
**
```

(por ejemplo, 10² es 10**2).

```python
math.sqrt(num)
```

La raíz cuadrada de un número, pero debes tener la línea `import math` en la parte superior de tu programa para que esto funcione.

```python
num=float(input("Ingrese número: "))
```

Permite números con un punto decimal que divide la parte entera y la fraccionaria.

```python
math.pi
```

Te da pi (π) hasta 15 lugares decimales, pero debes tener la línea `import math` en la parte superior de tu programa para que esto funcione.

```python
x // y
```

División de números enteros (por ejemplo, 15//2 da como respuesta 7).

```python
x % y
```

Encuentra el resto (por ejemplo, 15%2 da como respuesta 1).

## Bucle-For

**Explicación**

Un bucle for permite a Python repetir código un número establecido de veces. Es conocido como un bucle de conteo porque se sabe el número de veces que se ejecutará el bucle antes de que comience.

<!-- Aqui va una imagen -->

En este caso, el bucle comienza en 1 y seguirá repitiéndose (mostrando i) hasta que alcance 10 y luego se detendrá. Así es como se vería este bucle en Python.

<!-- Aquí va una imagen -->

En este ejemplo, las salidas serían **1, 2, 3, 4, 5, 6, 7, 8 y 9**.

Cuando llega a 10, el bucle se detendrá, por lo que no se mostrará 10 en la salida.

*Recuerda indentar las líneas de código dentro del bucle for.*

**Código de ejemplo**

La función `range()` se usa frecuentemente para listar el número inicial, el número final, pero también puede incluir los pasos (por ejemplo, contando en 1, 5 o cualquier otro valor que desees).

```python
for i in range(1, 10):
    print(i)
```  
Este ejemplo, se usa una variable llamada "i" para llevar un registro del número de veces que se ha repetido el bucle. Comenzará i en 1 (ya que es el valor inicial en la función range) y repetirá el bucle, sumando 1 a i cada vez y mostrando el valor de i hasta que alcance 10 (como lo dicta la función range), donde se detendrá. Por lo tanto, no repetirá el bucle una décima vez y tendrá la siguiente salida:

**1, 2, 3, 4, 5, 6, 7, 8, 9**

```python
for i in range(1, 10, 2):
    print(i)
```
En este otro ejemplo, la función `range()` incluye un tercer valor que muestra cuánto se agrega a i en cada bucle (en este caso 2). La salida será: **1, 3, 5, 7, 9**

```python
for i in range(10, 1, -3):
    print(i)
```

Este rango restará 3 de i en cada ocasión. La salida será: **10, 7, 4**

```python
for i in word:
    print(i)
```
Esto mostraría cada carácter en una cadena llamada "word" como una salida separada (es decir, en una línea separada).