import os
from tests.pages.file_download_page import FileDownloadPage
from tests.pages.base_page import wait_for_file


def test_download_all_files(tmp_path, driver, logger):
    download_dir = str(tmp_path)

    page = FileDownloadPage(driver, logger)
    page.load()

    filenames = page.download_all_files(limit=6)  # Limit to 6 files for testing

    logger.info(f"Waiting for downloaded files in {download_dir}")

    for filename in filenames:
        file_path = wait_for_file(download_dir, filename)
        assert os.path.exists(file_path)

    logger.info("All files downloaded successfully")

    assert len(os.listdir(download_dir)) == len(filenames)
