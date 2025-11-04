import requests


token = 'Ваш токен'
def create_folder(folder, token):
    try:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': f'{folder}'}
        response = requests.put(url, headers=headers, params=params)
        if response.status_code == 401:
            return "Неверный токен"
        if response.status_code == 201:
            return "Папка создана"
        if response.status_code == 409:
            return "Папка с таким именем существует"
    except Exception as e:
        return f'ОШИБКА при создании папки! {e}'