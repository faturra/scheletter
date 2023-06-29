import requests



# URL endpoint API

url = 'http://10.10.162.62:5774/WebService/getGtk?npsn=20100766'



# Bearer token

token = '31rQ0440xSYB2vs'



# Header Authorization

headers = {

	'Authorization': f'Bearer {token}'

}



# Mengirim GET request ke API dengan header Authorization

response = requests.get(url, headers=headers)


# Memeriksa status code response

if response.status_code == 200:
    
	# Mendapatkan data JSON dari response
    
	data = response.json()
	
	dapodik_reference = data.get('rows', [])

	# Mencetak data
	print('Dapodik API Connected [OK].')
else:
	# Menampilkan pesan jika request gagal
    
	print('Gagal mengambil data dari API.')