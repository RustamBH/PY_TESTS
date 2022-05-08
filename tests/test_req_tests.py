import unittest
from Netology.HTTP_req import YaUploader

TOKEN = ""


class TestYaUploader(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp --> work")

    def tearDown(self) -> None:
        print("tearDown -->work")

    def test_create_folder(self):
        new_dir_name = 'netology'
        uploader = YaUploader(token=TOKEN)
        self.assertEqual(uploader.create_folder(new_dir_name), 201)

    @unittest.expectedFailure
    def test_fail_create_folder(self):
        new_dir_name = 'netology'
        uploader = YaUploader(token=TOKEN)
        self.assertNotEqual(uploader.create_folder(new_dir_name), "Error")

    # @unittest.expectedFailure
    # def test2_fail_create_folder(self):
    #     new_dir_name = 'netology'
    #     uploader = YaUploader(token=TOKEN)
    #     self.assertEqual(uploader.create_folder(new_dir_name), 201)

    def test_get_info_dir(self):
        new_dir_name = 'netology'
        uploader = YaUploader(token=TOKEN)
        self.assertEqual(uploader.get_info_dir(new_dir_name), ('netology', 'dir', 200))

    @unittest.expectedFailure
    def test_fail_get_info_dir(self):
        new_dir_name = 'netology_new'
        uploader = YaUploader(token=TOKEN)
        self.assertEqual(uploader.get_info_dir(new_dir_name), ('netology', 'dir', 200))
