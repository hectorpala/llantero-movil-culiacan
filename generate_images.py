import os
import requests
from openai import OpenAI
from PIL import Image
from io import BytesIO
import time

BASE_DIR = "/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/llantero movil culiacan pro/assets/images"

client = OpenAI()

images = [
    {"filename": "cambio-llanta-420w.webp", "folder": "", "size": "1024x1024", "prompt": "Close-up of a professional mechanic changing a car tire using a hydraulic jack on a residential driveway. Clean work area, professional tools visible. The mechanic wears work gloves and orange uniform. Realistic photography, well-lit, professional composition. Square format. No text or words anywhere in the image."},
    {"filename": "reparacion-ponchadura-420w.webp", "folder": "", "size": "1024x1024", "prompt": "Close-up of a tire technician applying a professional rubber patch inside a dismounted tire. His gloved hands press firmly on the patch. A portable tire machine and tools are visible in the background. Warm workshop lighting. Realistic photography. Square format. No text or words anywhere in the image."},
    {"filename": "vulcanizadora-movil-420w.webp", "folder": "", "size": "1024x1024", "prompt": "Mobile tire vulcanizing setup on the back of a service truck. Portable vulcanizing machine, air compressor, and tire tools neatly organized. A technician in orange uniform working on a tire. Urban Mexican neighborhood background. Realistic photography. Square format. No text or words anywhere in the image."},
    {"filename": "llantero-24-horas-420w.webp", "folder": "", "size": "1024x1024", "prompt": "Nighttime scene of a mobile tire service technician fixing a flat tire on a car parked on a well-lit Mexican city street. The service truck has emergency lights on. Dramatic night lighting. Realistic photography. Square format. No text or words anywhere in the image."},
    {"filename": "alineacion-balanceo-420w.webp", "folder": "", "size": "1024x1024", "prompt": "A tire mounted on a modern computerized wheel balancing machine spinning smoothly. Digital display showing alignment readings. Clean auto shop environment. Realistic photography. Square format. No text or words anywhere in the image."},
    {"filename": "venta-llantas-420w.webp", "folder": "", "size": "1024x1024", "prompt": "Display of new tires stacked neatly showing various sizes and brands. Professional tire shop display. Clean, well-organized. Bright commercial lighting. Realistic photography. Square format. No text or words anywhere in the image."},
    {"filename": "llantero-movil-hero-1200w.webp", "folder": "", "size": "1792x1024", "prompt": "Professional mobile tire technician in orange uniform changing a flat tire beside a silver SUV on a clean residential street in Culiacan Mexico. White service van with tools parked behind. Golden hour sunlight. Wide angle. Realistic photography. No text or words anywhere in the image."},
    {"filename": "llantero-emergencia-800w.webp", "folder": "", "size": "1792x1024", "prompt": "Emergency roadside tire service on a highway shoulder at dusk. White service truck with orange emergency lights, technician changing a blown tire on an SUV. Dramatic sky with orange and purple tones. Wide angle. Realistic photography. No text or words anywhere in the image."},
    {"filename": "llantero-domicilio-800w.webp", "folder": "", "size": "1792x1024", "prompt": "Friendly tire technician in orange polo shirt arriving at a middle-class Mexican home with toolbox. Service van parked in driveway. Car with flat front tire visible. Warm morning light. Wide angle. Realistic photography. No text or words anywhere in the image."},
    {"filename": "logo-llantero-512.webp", "folder": "", "size": "1024x1024", "prompt": "Clean modern minimalist logo on pure white background. Stylized tire icon with a road going through it. Colors are orange and dark navy blue. Flat design, no 3D effects, no shadows. Vector style graphic. No text or words anywhere in the image."},
    {"filename": "google-review-emergency-service-1200w.webp", "folder": "social-proof/reviews", "size": "1792x1024", "prompt": "Clean screenshot mockup of Google My Business review interface, 5 gold stars prominently displayed, Spanish language, review text reads: Se me poncho la llanta a las 2 de la manana en la Mexico 15. Llegaron en 25 minutos. Me cambiaron la llanta rapido y a buen precio. 100 por ciento recomendado. Profile shows circular avatar icon, reviewer name Carlos R., date hace 2 semanas. White background, modern Google UI design, sharp text, professional typography, 16:9 aspect ratio."},
    {"filename": "google-review-ponchadura-1200w.webp", "folder": "social-proof/reviews", "size": "1792x1024", "prompt": "Professional Google My Business review screenshot mockup, 5 yellow stars rating, Spanish text review reads: Me ponche afuera de la oficina y en media hora ya estaba el llantero. Reparo la ponchadura con parche profesional. Muy amable y precios justos. Circular generic user avatar, reviewer name Ana L., timestamp hace 1 mes. Authentic Google review interface design, white clean background, crisp typography, 16:9 horizontal format."},
    {"filename": "google-review-domicilio-1200w.webp", "folder": "social-proof/reviews", "size": "1792x1024", "prompt": "Google review interface screenshot, 5 golden stars prominently shown, Spanish language review text: Pedi el servicio a domicilio para cambiar las 4 llantas de mi camioneta. Llegaron puntuales y las instalaron en menos de una hora. Excelente servicio. Circular profile picture placeholder, reviewer name Miguel H., date hace 5 dias. Clean white background, modern Google My Business design, 16:9 aspect ratio."},
    {"filename": "team-llanteros-culiacan-1200w.webp", "folder": "social-proof", "size": "1792x1024", "prompt": "Three professional Mexican mobile tire technicians standing together in front of white service truck with tire tools visible inside. Culiacan neighborhood with palm trees in background. Clean orange work uniforms with reflective stripes. One holds a cross wrench, another a hydraulic jack, the third a tire pressure gauge. Friendly confident smiles, warm natural Mexican sunlight. Photorealistic professional team portrait. 16:9. No text."},
    {"filename": "llantero-principal-van-1200w.webp", "folder": "social-proof", "size": "1792x1024", "prompt": "Confident Mexican tire technician age 35-40 standing beside white service truck with open side door showing organized tires, jacks, wrenches, and air compressor. Clean orange polo shirt, holding professional lug wrench. Culiacan street with tropical trees, golden hour afternoon lighting. Friendly trustworthy expression. Photorealistic portrait. 16:9. No text."},
    {"filename": "taller-movil-herramientas-1200w.webp", "folder": "social-proof", "size": "1792x1024", "prompt": "Interior of a mobile tire service truck meticulously organized. Stacked new tires of various sizes secured with straps, portable tire changer machine, air compressor, hydraulic jacks, cross wrenches, tire pressure gauges. LED work lights illuminate the space. A technician reaches for a tool. Clean organized professional workspace. Photorealistic, warm industrial lighting. 16:9. No text."},
    {"filename": "before-after-ponchadura-repair-1200w.webp", "folder": "social-proof/before-after", "size": "1792x1024", "prompt": "Split screen before and after comparison. LEFT SIDE: a completely flat tire on a car in a parking lot, the rim almost touching the ground, visible nail stuck in the tread. RIGHT SIDE: same tire fully inflated and repaired, showing perfect condition, tire mounted back on the car. Mexican urban parking lot context. Natural daylight. Photorealistic. 16:9. No text."},
    {"filename": "before-after-tire-change-1200w.webp", "folder": "social-proof/before-after", "size": "1792x1024", "prompt": "Before and after split comparison image. LEFT: severely worn bald tire with exposed steel belts, cracked rubber, dangerous tread depth, mounted on a sedan. RIGHT: brand new tire with deep fresh tread pattern, clean black rubber, perfectly mounted and balanced on the same wheel, shiny rim cleaned. Same car, same angle. Natural outdoor lighting in a Mexican residential driveway. Photorealistic. 16:9. No text."},
    {"filename": "before-after-blowout-repair-1200w.webp", "folder": "social-proof/before-after", "size": "1792x1024", "prompt": "Dramatic before after comparison split screen. LEFT SIDE: blown out shredded tire on highway shoulder, rubber fragments scattered, rim exposed, car tilted on damaged tire. RIGHT SIDE: same vehicle with brand new spare tire professionally installed, car level and ready to drive, clean work area, tools packed away. Highway shoulder in Sinaloa Mexico. Golden hour dramatic lighting. Photorealistic. 16:9. No text."},
    {"filename": "before-after-alignment-1200w.webp", "folder": "social-proof/before-after", "size": "1792x1024", "prompt": "Before and after side by side comparison. LEFT: close-up of a tire showing severe uneven wear pattern on the inner edge, visible feathering, poor alignment damage, tire surface worn smooth on one side. RIGHT: new properly aligned tire with even tread wear, perfect contact patch, computerized alignment printout visible in corner showing green within spec readings. Auto shop lighting, clean professional environment. Photorealistic. 16:9. No text."},
]

results = {"success": [], "failed": []}

print(f"\n{'='*60}")
print(f"  GENERADOR DE IMAGENES - Llantero Movil Culiacan Pro")
print(f"  Total: {len(images)} imagenes")
print(f"{'='*60}\n")

for i, img in enumerate(images, 1):
    folder_path = os.path.join(BASE_DIR, img["folder"]) if img["folder"] else BASE_DIR
    os.makedirs(folder_path, exist_ok=True)
    filepath = os.path.join(folder_path, img["filename"])

    if os.path.exists(filepath):
        print(f"[{i}/{len(images)}] SKIP {img['filename']} (ya existe)")
        results["success"].append(img["filename"])
        continue

    print(f"[{i}/{len(images)}] Generando {img['filename']}...", end=" ", flush=True)

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=img["prompt"],
            size=img["size"],
            quality="hd",
            n=1,
        )

        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        pil_image = Image.open(BytesIO(image_data))
        pil_image.save(filepath, "WEBP", quality=85)

        print(f"OK")
        results["success"].append(img["filename"])

    except Exception as e:
        print(f"ERROR: {e}")
        results["failed"].append({"file": img["filename"], "error": str(e)})

    time.sleep(1)

print(f"\n{'='*60}")
print(f"  RESULTADOS")
print(f"{'='*60}")
print(f"  Exitosas: {len(results['success'])}/{len(images)}")
print(f"  Fallidas: {len(results['failed'])}/{len(images)}")
if results["failed"]:
    print(f"\n  Fallidas:")
    for f in results["failed"]:
        print(f"    - {f['file']}: {f['error'][:80]}")
print(f"{'='*60}\n")
