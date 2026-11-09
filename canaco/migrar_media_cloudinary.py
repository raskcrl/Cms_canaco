
from pathlib import Path

from django.conf import settings
from home.models import Archivo
import cloudinary
import cloudinary.api
import cloudinary.uploader


archivos = (
    Archivo.objects
    .exclude(ruta='')
    .values_list('ruta', flat=True)
    .distinct()
)

subidos = 0
ya_existentes = 0
omitidos = 0
errores = 0

print("INICIANDO MIGRACIÓN DE ARCHIVOS A CLOUDINARY\n")

for ruta in archivos:

    archivo_local = Path(settings.MEDIA_ROOT) / ruta

    if not archivo_local.is_file():
        print(f"NO EXISTE LOCALMENTE: {ruta}")
        omitidos += 1
        continue

    public_id = f"media/{Path(ruta).with_suffix('').as_posix()}"

    try:
        try:
            cloudinary.api.resource(
                public_id,
                resource_type="image"
            )

            print(f"YA EXISTE EN CLOUDINARY: {ruta}")
            ya_existentes += 1
            continue

        except cloudinary.exceptions.NotFound:
            pass

        resultado = cloudinary.uploader.upload(
            str(archivo_local),
            public_id=public_id,
            resource_type="image",
            overwrite=False,
        )

        print(f"SUBIDO: {ruta}")
        print(f"URL: {resultado['secure_url']}\n")

        subidos += 1

    except Exception as error:
        print(f"ERROR: {ruta}")
        print(error)
        errores += 1


print("\n========== RESUMEN ==========")
print(f"Subidos: {subidos}")
print(f"Ya existentes: {ya_existentes}")
print(f"Omitidos (sin archivo local): {omitidos}")
print(f"Errores: {errores}")
print("=============================")
