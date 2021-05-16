# Clisya

Versión 0.1.2

---

Una pequeña librería de zonas horarias para generar banderas compatibles en email, redes, paginas web, etc. 

Actualmente se encuentra disponible para generar las zonas horarias de los siguientes países:

México : 🇲🇽  | Colombia : 🇨🇴  | Perú : 🇵🇪  | Chile : 🇨🇱  | Argentina : 🇦🇷 | España : 🇪🇸 | Uruguay : 🇺🇾 |     

Ecuador : 🇪🇨 | Guatemala : 🇬🇹 | El Salvador : 🇸🇻 | Bolivia : 🇧🇴 | Paraguay : 🇵🇾 | República 

Dominicana : 🇩🇴 | Panamá : 🇵🇦 | Costa Rica : 🇨🇷 | Honduras : 🇭🇳 | Venezuela : 🇻🇪 | Nicaragua : 🇳🇮 | Cuba : 🇨🇺 | US_Pacific : 🇺🇸 |

## Instalación

```python
pip install clisya
```

## Uso de Clisya.

```python
from clisya import Schedule
import clisya 
```

### Agregar fecha y hora.

Es tan sencillo como solo agregar la fecha y hora al método **date_to_convert,** se generara en base a la fecha y hora de su ordenador.

Se asume la hora y fecha registrada en horario **GMT-5.**

```python
#Declarar instancia del objecto
clisya = Schedule()

# Pasar argumento (datetime) Se asume la hora y fecha registrada en horario **GMT-5**
clisya.date_to_convert("2021-05-12 18:00:00")
```

### Pasar elementos a la lista **country.**

Puede agregar el nombre de los países que desea, filtramos el resultado por su preferencia.

Si desea conocer la hora en algún país en particular, ingrese su nombre en la lista **country.**

**NO** ingresar tildes en los nombres, de lo contrario presentara un error.

```python
clisya = Schedule()
clisya.date_to_convert("2021-05-12 18:00:00", country=['colombia','peru','España','Mexico'])
```

## **Contribuir.**

---

Te invitamos en caso de que encuentres algún bug o tengas feedback de alguna parte de `clisya`.

*Está librería se construyo basada en el repositorio [Horarios](https://github.com/freddier/Horarios) de Freddy Vega.*