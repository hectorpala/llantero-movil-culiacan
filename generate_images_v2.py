import os
import requests
from openai import OpenAI
from PIL import Image
from io import BytesIO
import time

BASE_DIR = "/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/llantero movil culiacan pro/assets/images"
client = OpenAI()
results = {"success": [], "failed": []}

STYLE = "Ultra realistic professional stock photography, shot with Canon EOS R5, 35mm lens, natural lighting, photojournalistic documentary style. Real Mexican person, authentic work environment, no AI artifacts, no text, no watermarks, no logos. Photo looks like it was taken by a professional photographer on a real job site."

def generate_and_resize(name, prompt, dall_e_size, resize_variants):
    """Generate one image and create all size variants"""
    print(f"  Generando {name}...", end=" ", flush=True)
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=dall_e_size,
            quality="hd",
            n=1,
        )
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        original = Image.open(BytesIO(image_data))

        for filename, width, height, folder in resize_variants:
            folder_path = os.path.join(BASE_DIR, folder) if folder else BASE_DIR
            os.makedirs(folder_path, exist_ok=True)
            filepath = os.path.join(folder_path, filename)
            resized = original.resize((width, height), Image.LANCZOS)
            resized.save(filepath, "WEBP", quality=85)

        print(f"OK ({len(resize_variants)} variantes)")
        results["success"].append(name)
    except Exception as e:
        print(f"ERROR: {e}")
        results["failed"].append({"file": name, "error": str(e)})
    time.sleep(1)

print(f"\n{'='*60}")
print(f"  GENERADOR v2 - Estilo Realista Stock Photo")
print(f"  Llantero Movil Culiacan Pro")
print(f"{'='*60}\n")

# ============================================
# 1. HERO (primero como pidio el usuario)
# ============================================
print("[1/10] HERO PRINCIPAL")
generate_and_resize("hero", 
    f"A Mexican mobile tire service technician age 35, with short dark hair and trimmed beard, wearing a clean dark navy blue work uniform with a reflective safety stripe, holding a tablet and explaining something to a female client at the front door of a modern middle-class Mexican home at night. Behind him a white branded service van is parked on the residential street with street lights. The scene is warmly lit by the porch light. {STYLE}",
    "1792x1024",
    [
        ("llantero-movil-hero-1200w.webp", 1200, 800, ""),
        ("llantero-movil-hero-800w.webp", 800, 533, ""),
        ("llantero-movil-hero-500w.webp", 500, 333, ""),
    ]
)

# ============================================
# 2. SERVICIOS - Cards cuadradas
# ============================================
print("\n[2/10] CAMBIO DE LLANTA")
generate_and_resize("cambio-llanta",
    f"A Mexican mechanic kneeling beside a car on a residential driveway, using a cross lug wrench to remove wheel bolts. He wears dark navy work overalls with a cap. A hydraulic floor jack supports the car. A professional toolbox is open nearby on the concrete. Bright daylight, clean suburban Mexican home background. {STYLE}",
    "1024x1024",
    [
        ("cambio-llanta-420w.webp", 420, 420, ""),
        ("cambio-llanta-800w.webp", 800, 800, ""),
    ]
)

print("\n[3/10] REPARACION DE PONCHADURA")
generate_and_resize("reparacion-ponchadura",
    f"Close-up of a Mexican tire technician wearing blue nitrile gloves and a gray t-shirt with dark overalls, using a metal rasp tool to prepare a punctured tire for an internal patch. The dismounted tire is on a portable tire machine. A well-organized toolbox with patches and rubber cement is visible. Indoor workshop lighting from windows. {STYLE}",
    "1024x1024",
    [
        ("reparacion-ponchadura-420w.webp", 420, 420, ""),
        ("reparacion-ponchadura-800w.webp", 800, 800, ""),
    ]
)

print("\n[4/10] VULCANIZADORA MOVIL")
generate_and_resize("vulcanizadora-movil",
    f"A Mexican tire technician in dark work uniform operating a portable tire vulcanizing machine mounted on the tailgate of a white service pickup truck. Air compressor hoses, tire tools, and stacked tires visible in the truck bed. Mexican residential neighborhood street with houses and trees in background. Afternoon natural light. {STYLE}",
    "1024x1024",
    [
        ("vulcanizadora-movil-420w.webp", 420, 420, ""),
        ("vulcanizadora-movil-800w.webp", 800, 800, ""),
    ]
)

print("\n[5/10] LLANTERO 24 HORAS")
generate_and_resize("llantero-24-horas",
    f"Nighttime scene of a Mexican tire technician wearing a dark navy uniform with reflective safety stripe and a cap, kneeling beside a sedan on a Mexican residential street changing a flat tire. LED work light illuminates the scene. His white service truck with red emergency lights is parked behind. Street lamps and houses in dark background. Dramatic cinematic night photography. {STYLE}",
    "1024x1024",
    [
        ("llantero-24-horas-420w.webp", 420, 420, ""),
        ("llantero-24-horas-800w.webp", 800, 800, ""),
    ]
)

print("\n[6/10] ALINEACION Y BALANCEO")
generate_and_resize("alineacion-balanceo",
    f"A young Mexican technician wearing a cap and safety glasses, standing at a computerized wheel balancing machine inspecting the digital readout. A tire is mounted on the machine spindle. Clean organized auto shop interior with tool pegboard on wall, fluorescent lighting. Professional workshop environment. {STYLE}",
    "1024x1024",
    [
        ("alineacion-balanceo-420w.webp", 420, 420, ""),
        ("alineacion-balanceo-800w.webp", 800, 800, ""),
    ]
)

print("\n[7/10] VENTA DE LLANTAS")
generate_and_resize("venta-llantas",
    f"Interior of a Mexican tire shop showing rows of new black tires stacked on metal racks, organized by size. A technician in work clothes examines the tread pattern of a tire he is holding. Price labels visible on the rack shelves. Clean commercial space, bright overhead lighting. {STYLE}",
    "1024x1024",
    [
        ("venta-llantas-420w.webp", 420, 420, ""),
        ("venta-llantas-800w.webp", 800, 800, ""),
    ]
)

# ============================================
# 3. PAGINAS INTERNAS - Wide
# ============================================
print("\n[8/10] EMERGENCIA (wide)")
generate_and_resize("emergencia-wide",
    f"A Mexican mobile tire technician seen from behind, wearing dark navy uniform with reflective safety stripe and holding a toolbox in one hand and a portable work light in the other, walking toward a female client waiting at the front door of a Mexican home at night. A white service van with red emergency lights is parked on the street. Dramatic nighttime photography with warm porch light and cool street light contrast. {STYLE}",
    "1792x1024",
    [
        ("llantero-emergencia-1200w.webp", 1200, 800, ""),
        ("llantero-emergencia-800w.webp", 800, 534, ""),
    ]
)

print("\n[9/10] DOMICILIO (wide)")
generate_and_resize("domicilio-wide",
    f"A friendly Mexican tire technician age 30-35 arriving at a middle-class Mexican home during morning hours. He carries a professional toolbox and stands near the front door where the homeowner greets him. A white service pickup truck is parked in the driveway behind him with organized tools visible. Warm morning sunlight, green plants in the yard, typical Culiacan residential neighborhood. {STYLE}",
    "1792x1024",
    [
        ("llantero-domicilio-1200w.webp", 1200, 800, ""),
        ("llantero-domicilio-800w.webp", 800, 534, ""),
    ]
)

# ============================================
# 4. LOGO
# ============================================
print("\n[10/10] LOGO")
generate_and_resize("logo",
    "A clean, modern, minimalist logo icon on a pure white background. The icon is a simple stylized car tire seen from the side, with an orange colored road or speed line going through it. The design uses only two colors: orange and dark navy blue. Flat vector style, no gradients, no 3D effects, no shadows, no text, no letters, no words. Extremely simple and clean like a modern app icon.",
    "1024x1024",
    [
        ("logo-llantero-512.webp", 512, 512, ""),
        ("logo-llantero-256.webp", 256, 256, ""),
        ("logo-llantero-128.webp", 128, 128, ""),
        ("logo-nav.webp", 200, 76, ""),
    ]
)

print(f"\n{'='*60}")
print(f"  RESULTADOS SERVICIOS + HERO + LOGO")
print(f"{'='*60}")
print(f"  Exitosas: {len(results['success'])}/10")
print(f"  Fallidas: {len(results['failed'])}/10")
if results["failed"]:
    print(f"\n  Fallidas:")
    for f in results["failed"]:
        print(f"    - {f['file']}: {f['error'][:80]}")
print(f"{'='*60}\n")
print("Listo! Ahora ejecuta generate_social_proof_v2.py para las de social proof.")
