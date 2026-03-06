import pytest
from tests.pages.hovers_page import HoversPage


@pytest.mark.parametrize(
    "index, expected_name",
    [
        (0, "user1"),
        (1, "user2"),
        (2, "user3"),
    ],
)
def test_hover_reveals_caption(driver, index, expected_name, logger):
    page = HoversPage(driver, logger)
    page.load()

    logger.info(f"Hovering over figure at index: {index} expecting name: {expected_name}")

    page.hover_over_figure(index)

    caption_text = page.get_caption_text(index)

    name_line = caption_text.split("\n")[0]
    assert name_line.lower() == f"name: {expected_name}"

    assert page.is_profile_link_visible(index)

    logger.info(f"Hover test completed successfully for index: {index} with expected name: {expected_name}")    
