import pytz
from typing import Optional
import datetime

LOCAL_TZ = pytz.timezone('America/Bogota')

        # En orden de tamaño de mercado/prioridad
zones = [
["🇲🇽", "America/Mexico_City"],
["🇨🇴", "America/Bogota"],
["🇵🇪", "America/Lima"],
["🇨🇱", "America/Santiago"],
["🇦🇷", "America/Buenos_Aires"],
["🇪🇸", "Europe/Madrid"],
["🇺🇾", "America/Montevideo"],
["🇪🇨", "America/Guayaquil"],
["🇬🇹", "America/Guatemala"],
["🇸🇻", "America/El_Salvador"],
["🇧🇴", "America/La_Paz"],
["🇵🇾", "America/Asuncion"],
["🇩🇴", "America/Santo_Domingo"],
["🇵🇦", "America/Panama"],
["🇨🇷", "America/Costa_Rica"],
["🇭🇳", "America/Tegucigalpa"],
["🇻🇪", "America/Caracas"],
["🇳🇮", "America/Managua"],
["🇨🇺", "Cuba"],
["🇺🇸", "US/Pacific"]
]

class Schedule:
    """

    Instancia para generar el horario correspondiente
    segun el horario de cada país.

    """

    def date_to_convert(self, date_to_convert, lista: list = None):



        # Los timezones no están derivados de países, sino de ciudades.
        # Aunque la prioridad es por país

        print(date_to_convert)
        print("Generando bloque de banderas:")
        print("")

        # Inicializamos el diccionario

        date_to_convert = datetime.datetime.strptime(
        date_to_convert, "%Y-%m-%d %H:%M:%S")
        
        times = {"00pm": "X"}
        date_to_convert = LOCAL_TZ.localize(date_to_convert)

        if lista is None:
            for country in zones:            
                dtc = date_to_convert.astimezone(pytz.timezone(country[1]))
                if country[1] == "Europe/Madrid":
                    # Imprime la hora en formato de 24 horas y una "H" al final
                    dtc = dtc.strftime("%-HH")
                else:
                    # Imprime la hora en formato de 12 horas PM/AM
                    dtc = dtc.strftime("%-I%p")
                try:
                    times[dtc] = times[dtc] + country[0]
                except KeyError:
                    times[dtc] = country[0]
                # Si el país es USA en Pacific, agregar el "PT" frente a bandera de US
                if country[1] == "US/Pacific":
                    times[dtc] = times[dtc] + " PT"

                times[dtc] = times[dtc] + " "
            
            for time, flag in times.items():
                if flag != 'X':
                    print(time.lower(), flag.strip())

        elif lista != None:

            comparacion=[]   
            for pais in zones:
                if pais[0] in lista:
                    comparacion.append(pais)
            if len(comparacion) > 0:
                for pais in comparacion: 
                    #print(pais)
                    dtc2 = date_to_convert.astimezone(pytz.timezone(pais[1]))
                    if pais[1] == "Europe/Madrid":
                        # Imprime la hora en formato de 24 horas y una "H" al final
                        dtc2 = dtc2.strftime("%-HH")
                    else:
                        # Imprime la hora en formato de 12 horas PM/AM
                        dtc2 = dtc2.strftime("%-I%p")
                    try:
                        times[dtc2] = times[dtc2] + pais[0]
                    except KeyError:
                        times[dtc2] = pais[0]
                    # Si el país es USA en Pacific, agregar el "PT" frente a bandera de US
                    if pais[1] == "US/Pacific":
                        times[dtc2] = times[dtc2] + " PT"

                    times[dtc2] = times[dtc2] + " "
                
                for time, flag in times.items():
                    if flag != 'X':
                        print(time.lower(), flag.strip())
            else:
                print('No hay nada')


if __name__ == '__main__':

    # Fecha y hora de entrada
    schedule = Schedule()
    schedule.date_to_convert("2021-05-11 15:00:00",lista=['🇬🇹','🇨🇴','🇪🇸','🇲🇽','🇺🇸'])




