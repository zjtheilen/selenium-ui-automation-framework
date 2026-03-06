import pytest
from tests.pages.file_upload_page import FileUploadPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize(
    "file_path, expected_result",
    [
        ("tests/resources/invalid_file.txt", "success"),  # site allows .txt
        ("tests/resources/large_file.pdf", "success"),  # site allows large files
        ("", "error"),  # empty upload triggers server error
    ],
)
def test_file_upload_behavior(driver, file_path, expected_result, logger):
    page = FileUploadPage(driver, logger)
    page.load()

    logger.info(f"Testing file upload with path: '{file_path}' expecting {expected_result}")

    page.upload_file(file_path)

    if expected_result == "success":
        uploaded_name = page.get_uploaded_file_name()
        assert uploaded_name is not None
    elif expected_result == "error":
        h1_text = (
            WebDriverWait(driver, 5)
            .until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            .text
        )

        assert h1_text == "Internal Server Error"
        logger.info("Received expected error message for invalid file upload")
    
    logger.info("File upload test completed with expected result: " + expected_result)
