import os
from tests.pages.file_upload_page import FileUploadPage


def test_file_upload(driver, logger):
    page = FileUploadPage(driver, logger)
    page.load()

    logger.info("Testing file upload with a valid file")

    test_file_path = os.path.abspath("tests/resources/test_file.txt")
    page.upload_file(test_file_path)
    uploaded_file_name = page.get_uploaded_file_name()

    assert uploaded_file_name == "test_file.txt"

    logger.info(
        "File upload test completed successfully with uploaded file: "
        + uploaded_file_name
    )
