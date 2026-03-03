import os
from tests.pages.file_download_page import FileDownloadPage
from tests.pages.base_page import wait_for_file

def test_download_all_files(tmp_path, driver):
    download_dir = str(tmp_path)

    # Enable Chrome downloads
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command"
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_dir}
    }
    driver.execute("send_command", params)

    page = FileDownloadPage(driver)
    page.load()

    filenames = page.download_all_files()

    for filename in filenames:
        file_path = wait_for_file(download_dir, filename)
        assert os.path.exists(file_path)