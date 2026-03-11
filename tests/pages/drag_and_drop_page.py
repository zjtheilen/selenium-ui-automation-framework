from selenium.webdriver.common.by import By

# from selenium.webdriver.common.action_chains import ActionChains
from config.config import BASE_URL
from tests.pages.base_page import BasePage


class DragAndDropPage(BasePage):
    URL = BASE_URL + "/drag_and_drop"

    COLUMN_A = (By.ID, "column-a")
    COLUMN_B = (By.ID, "column-b")

    HEADER = (By.TAG_NAME, "header")

    def load(self):
        self.logger.info("Loading Drag and Drop page")
        self.driver.get(self.URL)

    def get_column_headers(self):
        self.logger.info("Getting column headers")
        header_a = (
            self.wait_for_element(self.COLUMN_A)
            .find_element(By.TAG_NAME, "header")
            .text
        )
        header_b = (
            self.wait_for_element(self.COLUMN_B)
            .find_element(By.TAG_NAME, "header")
            .text
        )
        return header_a, header_b

    def drag(self, source_locator, target_locator):
        self.logger.info("Dragging element")

        source_elem = self.driver.find_element(*source_locator)
        target_elem = self.driver.find_element(*target_locator)
        self.js_drag_and_drop(self.driver, source_elem, target_elem)
        # source = self.wait_for_element(source_locator)
        # target = self.wait_for_element(target_locator)

        # action = ActionChains(self.driver)
        # action.click_and_hold(source).move_to_element(target).release().perform()

        # ActionChains(self.driver).drag_and_drop(source, target).perform()
    
    def js_drag_and_drop(self, driver, source, target):
        driver.execute_script("""
        function simulateDragDrop(sourceNode, destinationNode) {
            var EVENT_TYPES = {
                DRAG_END: 'dragend',
                DRAG_START: 'dragstart',
                DROP: 'drop'
            }

            function createCustomEvent(type) {
                var event = new CustomEvent("CustomEvent")
                event.initCustomEvent(type, true, true, null)
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) {
                        this.data[key] = value;
                    },
                    getData: function(key) {
                        return this.data[key];
                    }
                }
                return event
            }

            function dispatchEvent(node, type, event) {
                if (node.dispatchEvent) return node.dispatchEvent(event);
                if (node.fireEvent) return node.fireEvent("on" + type, event);
            }

            var dragStartEvent = createCustomEvent(EVENT_TYPES.DRAG_START)
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragStartEvent)

            var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
            dropEvent.dataTransfer = dragStartEvent.dataTransfer
            dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)

            var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
            dragEndEvent.dataTransfer = dragStartEvent.dataTransfer
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
        }

        simulateDragDrop(arguments[0], arguments[1])
        """, source, target)
