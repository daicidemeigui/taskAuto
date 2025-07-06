import base64

with open("picture/Snipaste_2025-07-06_15-28-32.png","rb") as f:
    str = base64.b64encode(f.read()).decode('utf-8')
    print(str)
