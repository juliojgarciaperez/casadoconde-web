from PIL import Image
import base64, io

src = Image.open("/Users/cx01828/Downloads/CC.png").convert("RGBA")

# favicon.ico — multi-size
src.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32)])

# apple-touch-icon.png — 180x180
src.resize((180, 180), Image.LANCZOS).save("apple-touch-icon.png")

# favicon.svg — embeds 32x32 PNG as base64 (keeps existing <link> working)
img32 = src.resize((32, 32), Image.LANCZOS)
buf = io.BytesIO()
img32.save(buf, format="PNG")
b64 = base64.b64encode(buf.getvalue()).decode()
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><image href="data:image/png;base64,{b64}" width="32" height="32"/></svg>'
open("favicon.svg", "w").write(svg)

print("Done: favicon.ico, apple-touch-icon.png, favicon.svg")
