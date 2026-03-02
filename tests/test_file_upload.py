import os
from tests.pages.file_upload_page import FileUploadPage

def test_file_upload(driver):
    page = FileUploadPage(driver)
    page.load()

    test_file_path = os.path.abspath("tests/resources/test_file.txt")
    uploaded_file_name = page.upload_file(test_file_path)

    assert uploaded_file_name == "test_file.txt"