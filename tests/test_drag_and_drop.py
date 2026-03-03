from tests.pages.drag_and_drop_page import DragAndDropPage

def test_drag_and_drop(driver):
    page = DragAndDropPage(driver)
    page.load()

    before = page.get_column_headers()
    assert before == ("A", "B")

    page.drag_and_drop()

    after = page.get_column_headers()
    assert after == ("B", "A")