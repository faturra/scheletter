import requests
from .config import headers
from .api_endpoint import getSekolah, getPengguna, getGtk, getPesertaDidik

# Data School
response = requests.get(getSekolah, headers=headers)

if response.status_code == 200:
	data = response.json()
	dapodik_school = data.get('rows', [])
	print('Dapodik API School Connection [OK].')
else:
	print('Dapodik API School Connection Failed [ERROR].')

# Data Users
response = requests.get(getPengguna, headers=headers)

if response.status_code == 200:
	data = response.json()
	dapodik_users = data.get('rows', [])
	print('Dapodik API Users Connection [OK].')
else:
	print('Dapodik API Users Connection Failed [ERROR].')

# Data Employees
response = requests.get(getGtk, headers=headers)

if response.status_code == 200:
	data = response.json()
	dapodik_employees = data.get('rows', [])
	print('Dapodik API Employees Connection [OK].')
else:
	print('Dapodik API Employees Connection Failed [ERROR].')

# Data Students
response = requests.get(getPesertaDidik, headers=headers)

if response.status_code == 200:
	data = response.json()
	dapodik_students = data.get('rows', [])
	print('Dapodik API Students Connection [OK].')
else:
	print('Dapodik API Students Connection Failed [ERROR].')