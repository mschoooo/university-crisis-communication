# -*- coding: utf-8 -*-
import sys
import urllib.request
import re
from PIL import Image
import io

sys.stdout.reconfigure(encoding="utf-8")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = 'https://www.kado.net/news/articleView.html?idxno=1295293'
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
        for img in imgs:
            if '/news/' in img or '/photo/' in img:
                print('Found img URL:', img)
                full_url = img if img.startswith('http') else 'https://www.kado.net' + img
                try:
                    img_req = urllib.request.Request(full_url, headers=headers)
                    with urllib.request.urlopen(img_req) as img_resp:
                        data = img_resp.read()
                        im = Image.open(io.BytesIO(data))
                        print(f"Downloaded: {full_url}, size={im.size}, format={im.format}")
                        if im.size[0] > 400:
                            im.convert('RGB').save('versions/deck_v7/assets/protest_kangwon.jpg', quality=92)
                            print("Saved to versions/deck_v7/assets/protest_kangwon.jpg!")
                            break
                except Exception as err:
                    print('Img download error:', err)
except Exception as e:
    print('Page error:', e)
