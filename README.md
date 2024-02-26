### Bucle For

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

---