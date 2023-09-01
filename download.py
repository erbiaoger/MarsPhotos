import requests
import os

# 构建 API 请求
api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "J4A9noeSQPalMWPdamZOkeTbg38xSOlEdVuqpitv"  # 替换为你自己的 NASA API 密钥

for sol in range(500, 510):
    params = {
        "sol": sol,  # 指定火星上的“太阳日”（sol）
        "camera": "FHAZ",  # 指定相机类型（可选）
        "api_key": api_key
    }

    # 发送 GET 请求
    response = requests.get(api_url, params=params)

    # 处理 API 响应
    if response.status_code == 200:
        data = response.json()
        photos = data["photos"]
        
        for photo in photos:
            img_src = photo["img_src"]
            #print(img_src)       
        
            # 下载图片 
            os.system("wget " + img_src)
        os.system("mkdir -p Mar_{:04d}".format(sol))
        os.system("mv *.JPG Mar_{:04d}".format(sol))
    else:
        print("请求失败:", response.status_code)



