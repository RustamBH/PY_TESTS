import requests

TOKEN = ""


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code != 200:
            return "Error"
        return response.json()

    def get_info_dir(self, dir_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": dir_name}
        response = requests.get(upload_url, headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            return "Error"
        dirname = response.json()["name"]
        type_dir = response.json()["type"]
        return dirname, type_dir, response.status_code

    def create_folder(self, dir_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.get_headers()
        params = {"path": dir_name, "overwrite": "true"}
        response = requests.put(upload_url, headers=headers, params=params)
        if response.status_code != 201:
            return "Error"
        return response.status_code

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        disk_file_path = "netology/upload.txt"
        dir_name = disk_file_path.rstrip(file_path)
        resp = self.create_folder(dir_name=dir_name)
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code != 201:
            return "Error"
        return response.status_code


if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    new_dir_name = "netology"
    resp_create_folder = uploader.create_folder(new_dir_name)
    resp_get_info = uploader.get_info_dir(new_dir_name)
