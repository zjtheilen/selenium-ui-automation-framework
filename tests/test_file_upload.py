import os
from tests.pages.file_upload_page import FileUploadPage

def test_file_upload(driver):
    page = FileUploadPage(driver)
    page.load()

    test_file_path = os.path.abspath("tests/resources/test_file.txt")
    page.upload_file(test_file_path)
    uploaded_file_name = page.get_uploaded_file_name()

    assert uploaded_file_name == "test_file.txt"