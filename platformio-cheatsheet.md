# Comandos comunes de PlatformIO

Ejecutar desde la carpeta del proyecto (la que contiene `platformio.ini`), con el venv activado:

```powershell
.\venv\Scripts\Activate.ps1
cd hw-477-v0.2-IR
```

## Build y upload

| Comando | Descripción |
|---|---|
| `pio run` | Compila el proyecto |
| `pio run -t upload` | Compila y sube el firmware a la placa |
| `pio run -t clean` | Limpia los archivos compilados |

## Monitor serial

| Comando | Descripción |
|---|---|
| `pio device monitor` | Abre el monitor serial (usa `monitor_port`/`monitor_speed` del `platformio.ini`) |
| `pio device monitor -p COM3 -b 9600` | Abre el monitor especificando puerto y baud rate manualmente |
| `Ctrl+C` | Cierra el monitor |

Atajo: subir y abrir el monitor en un solo paso:
```powershell
pio run -t upload -t monitor
```

## Dispositivos

| Comando | Descripción |
|---|---|
| `pio device list` | Lista los puertos serie detectados |

## Librerías

| Comando | Descripción |
|---|---|
| `pio lib search <nombre>` | Busca una librería en el registro de PlatformIO |
| `pio lib install <nombre>` | Instala una librería (mejor usar `lib_deps` en `platformio.ini`) |

## Proyectos

| Comando | Descripción |
|---|---|
| `pio project init --board uno` | Inicializa un nuevo proyecto PlatformIO en la carpeta actual |
