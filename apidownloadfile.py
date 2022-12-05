import requests

python_file_url = "http://tdc-www.harvard.edu/Python.pdf"
response = requests.get(python_file_url, stream=True)
print(response)

with open("python_python.pdf", "wb") as pdf:
    for buddy in response.iter_content(chunk_size=1024):
        if buddy:
            pdf.write(buddy)
