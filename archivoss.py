import pandas as pd

import re

datos =  """
16:57:55.479 Temp: 30.20°C | Hum: 42.00%
16:57:57.427 Temp: 30.10°C | Hum: 42.00%
16:57:59.475 Temp: 30.60°C | Hum: 43.00%
16:58:01.471 Temp: 30.10°C | Hum: 43.00%
16:58:03.520 Temp: 30.50°C | Hum: 43.00%
16:58:05.516 Temp: 30.70°C | Hum: 43.00%
16:58:07.564 Temp: 30.40°C | Hum: 43.00%
16:58:09.560 Temp: 30.20°C | Hum: 43.00%
16:58:11.662 Temp: 30.00°C | Hum: 43.00%
16:58:13.649 Temp: 30.20°C | Hum: 43.00%
16:58:15.664 Temp: 30.50°C | Hum: 43.00%
16:58:17.701 Temp: 30.70°C | Hum: 43.00%
16:58:19.697 Temp: 30.40°C | Hum: 43.00%
16:58:21.737 Temp: 30.10°C | Hum: 43.00%
16:58:23.745 Temp: 30.60°C | Hum: 43.00%
16:58:25.792 Temp: 30.00°C | Hum: 43.00%
16:58:27.788 Temp: 30.20°C | Hum: 43.00%
16:58:29.887 Temp: 30.80°C | Hum: 43.00%
16:58:31.887 Temp: 30.30°C | Hum: 43.00%
16:58:33.892 Temp: 30.10°C | Hum: 43.00%
16:58:36.025 Temp: 30.70°C | Hum: 44.00%
16:58:37.924 Temp: 30.60°C | Hum: 45.00%
16:58:39.974 Temp: 30.30°C | Hum: 46.00%
16:58:41.971 Temp: 30.40°C | Hum: 47.00%
16:58:44.062 Temp: 30.90°C | Hum: 47.00%
16:58:46.016 Temp: 30.80°C | Hum: 47.00%
16:58:48.064 Temp: 30.30°C | Hum: 46.00%
16:58:50.064 Temp: 30.70°C | Hum: 46.00%
16:58:52.157 Temp: 31.00°C | Hum: 45.00%
16:58:54.156 Temp: 31.50°C | Hum: 44.00%
16:58:56.153 Temp: 31.90°C | Hum: 44.00%
16:58:58.201 Temp: 31.60°C | Hum: 44.00%
16:59:00.200 Temp: 31.30°C | Hum: 43.00%
16:59:02.247 Temp: 31.10°C | Hum: 43.00%
16:59:04.294 Temp: 31.00°C | Hum: 43.00%
16:59:06.292 Temp: 31.60°C | Hum: 43.00%
16:59:08.286 Temp: 31.50°C | Hum: 43.00%
16:59:10.335 Temp: 31.90°C | Hum: 43.00%
16:59:12.384 Temp: 31.00°C | Hum: 43.00%
16:59:14.434 Temp: 31.90°C | Hum: 43.00%
16:59:16.429 Temp: 31.60°C | Hum: 42.00%
16:59:18.426 Temp: 31.30°C | Hum: 42.00%
16:59:20.472 Temp: 31.00°C | Hum: 42.00%
16:59:22.478 Temp: 31.80°C | Hum: 42.00%
16:59:24.518 Temp: 31.20°C | Hum: 42.00%
16:59:26.515 Temp: 31.40°C | Hum: 42.00%
16:59:28.562 Temp: 31.20°C | Hum: 42.00%
16:59:30.662 Temp: 31.10°C | Hum: 42.00%
16:59:32.609 Temp: 31.60°C | Hum: 42.00%
16:59:34.656 Temp: 31.20°C | Hum: 42.00%
16:59:36.706 Temp: 31.00°C | Hum: 42.00%
16:59:38.660 Temp: 32.10°C | Hum: 41.00%
16:59:40.698 Temp: 32.30°C | Hum: 41.00%
16:59:42.795 Temp: 32.80°C | Hum: 41.00%
16:59:44.742 Temp: 32.20°C | Hum: 41.00%
16:59:46.788 Temp: 32.30°C | Hum: 41.00%
"""

pattern = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d+)\s+Temp:\s([\d.]+)°C\s\|\sHum:\s([\d.]+)%")


guardar_datos = []

for line in datos.strip().splitlines():
    match = pattern.search(line)
    
    if match:
        tiempo = match.group(1)
        temperatura = float(match.group(2))
        humedad = float(match.group(3))
        guardar_datos.append({"Tiempo": tiempo, "Temperatura (°C)": temperatura, "Humedad (%)": humedad})
        
df = pd.DataFrame(guardar_datos)

df.to_csv("Temperatura_Humedad.csv", index=False)

print("Archivo csv creado con exito")