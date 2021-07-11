import io  # インメモリストリームを使え、ディスクにファイルを書かなくてもいい
import requests
import zipfile


url = ('https://files.pythonhosted.org/packages/7c/1b/9b68465658cda69f'
      '33c31c4dbd511ac5648835680ea8de87ce05c81f95bf/'
      'setuptools-50.3.0.zip')

f = io.BytesIO()
r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('setuptools-50.3.0/README.rst') as r:
        print(r.read().decode())

