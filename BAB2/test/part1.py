import requests
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)
# Cetak kode status dari response
print(response.status_code)
# Cetak isi file hello.txt menggunakan method response.iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for line in response.iter_lines():
    print(line.decode('utf-8'))
