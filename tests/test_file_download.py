import os
import time
from tests.pages.file_download_page import FileDownloadPage

def test_file_download(tmp_path, driver):
    download_dir = str(tmp_path)
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command"
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {
            "behavior": "allow",
            "downloadPath": download_dir
        }
    }
    driver.execute("send_command", params)

    page = FileDownloadPage(driver)
    page.load()

    filename = page.download_first_file(download_dir)

    file_path = os.path.join(download_dir, filename)

    for _ in range(10):
        if os.path.exists(file_path):
            break
        time.sleep(0.5)
    
    assert os.path.exists(file_path)
