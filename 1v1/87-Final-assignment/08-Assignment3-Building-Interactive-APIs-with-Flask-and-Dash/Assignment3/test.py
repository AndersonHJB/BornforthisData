import requests

# Example of using the convert route
url = 'http://127.0.0.1:5000/convert'
files = {'image': open('static/079A2379.jpg', 'rb')}
data = {'output_type': 'png'}
response = requests.post(url, files=files, data=data)
# print(response.status_code)
if response.status_code == 200:
    save_img_out = open('static/output/output1.png', 'wb')
    save_img_out.write(response.content)
    save_img_out.close()
    print("Image saved successfully.")
else:
    print("Failed to convert image")
# print(response.content)
# print(response.json())


# Example of using the analyze route
url = 'http://127.0.0.1:5000/analyze'
data = {'text': 'I love programming with Python!'}
response = requests.post(url, data=data)
print(response.json())