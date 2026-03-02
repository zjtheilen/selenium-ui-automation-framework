from tests.pages.nested_frames_page import NestedFramesPage

def test_nested_frames(driver):
    page = NestedFramesPage(driver)
    page.load()

    assert page.get_frame_text(["frame-top", "frame-left"]) == "LEFT"
    assert page.get_frame_text(["frame-top", "frame-middle"]) == "MIDDLE"
    assert page.get_frame_text(["frame-top", "frame-right"]) == "RIGHT"
    assert page.get_frame_text(["frame-bottom"]) == "BOTTOM"