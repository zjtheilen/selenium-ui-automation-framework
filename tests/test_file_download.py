import os
from tests.pages.file_download_page import FileDownloadPage
from tests.pages.base_page import wait_for_file

def test_download_all_files(tmp_path, driver):
    download_dir = str(tmp_path)

    page = FileDownloadPage(driver)
    page.load()

    filenames = page.download_all_files()

    print("Files Selenium attempted to download:")
    print(filenames)
    print("Count:", len(filenames))

    for filename in filenames:
        file_path = wait_for_file(download_dir, filename)
        assert os.path.exists(file_path)
    
    assert len(os.listdir(download_dir)) == len(filenames)