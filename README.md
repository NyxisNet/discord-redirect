## discord-redirect
Github pages hosted site for a discord redirection site to use as custom link for our Discord.

- [English tutorial](#how-to-use)
- [Tutorial en Español](#cómo-usar)

---
<details>
  <summary>English Version</summary>

# English Version

## How to use

Here's a brief explanation of how this site works c:

### index.html

Do not edit this, it's useless to do any meaningful changes on this file because it is overwritten automatically every time the site is modified/updated.

If you want to change anything from this, change something from the [config](#configyml) or [template](#templatehtml).

### config.yml

This file defines key-value strings to be replaced in the [template](#templatehtml), whatever config key found in the template will be replaced with its corresponding value from the config.

All replacements are ordered from first to last, therefore you can use a key defined at the end as part of the string defined before that one.

##### Example of key reusability
```yaml
first-defined: "I can use {second-defined} in first-defined key."
second-defined: "the second key"
```
**Result after replacement:** `I can use the second key in first-defined key.`

If you need more complex handling of the site, modify the [template](#templatehtml)

### template.html

This is the template used for the website, it's literally just an HTML website but instead of using readable code for a real website it uses placeholders for the key-value configs found in [config.yml](#configyml), if you understand HTML and read the config.yml section, go ahead and modify it, if you don't know both of those, don't touch it.

### build.py

This script is executed to create the `index.html` from the `template.html`, there's not much to explain here, if you know python, you get it, if you don't, just don't touch it until you learn python.

*TODO: Make build.py part of a Github Pages workflow*

</details>

<details>
  <summary>Spanish Version</summary>

# Tutorial en Español:

<details>
  <summary>upsi</summary>
  (Traducido con IA porque me dio pereza reescribir todo)
</details>


## Cómo usar

Aquí tienes una breve explicación de cómo funciona este sitio c:

### index.html

No edites este archivo, es inútil hacer cambios significativos en él porque se sobrescribe automáticamente cada vez que el sitio se modifica/actualiza.

Si deseas cambiar algo de esto, modifica algo de la [configuración](#configyml) o [plantilla](#templatehtml).

### config.yml

Este archivo define cadenas de clave-valor que serán reemplazadas en la [plantilla](#templatehtml), cualquier clave de configuración encontrada en la plantilla será reemplazada por su valor correspondiente del archivo de configuración.

Todos los reemplazos se ordenan de primero a último, por lo tanto, puedes usar una clave definida al final como parte de una cadena definida antes de ella.

##### Ejemplo de reutilización de claves
```yaml
first-defined: "Puedo usar {second-defined} en la clave first-defined."
second-defined: "la segunda clave"
```
**Resultado después del reemplazo:** `Puedo usar la segunda clave en la clave first-defined.`

Si necesitas un manejo más complejo del sitio, modifica la [plantilla](#templatehtml).

### template.html

Esta es la plantilla utilizada para el sitio web, literalmente es solo un sitio HTML, pero en lugar de usar código legible para un sitio web real, usa marcadores de posición para las configuraciones clave-valor encontradas en [config.yml](#configyml). Si entiendes HTML y has leído la sección de config.yml, adelante, modifícalo. Si no sabes sobre ambos, no lo toques.

### build.py

Este script se ejecuta para crear el `index.html` a partir del `template.html`, no hay mucho que explicar aquí, si sabes Python, lo entenderás, si no lo sabes, simplemente no lo toques hasta que aprendas Python.

*TODO: Hacer que build.py sea parte de un flujo de trabajo de Github Pages*

</details>