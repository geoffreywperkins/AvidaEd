import logging

from base.base_page import BasePage
from utilities.custom_logger import create_custom_logger


class OrganismPage(BasePage):
    """
    Specialization of the BasePage that is specialized for use on the Organism
    Page within the Avida-ED website.
    """

    def __init__(self, driver):
        """
        Sets up the page at initialization.

        :param driver: The driver that is interacting with the actual page.
        """
        super().__init__(driver)
        self.driver = driver
        self.go_to_organism()

    log = create_custom_logger(logging.DEBUG)

    def org_settings_displayed(self):
        """
        Checks if the Organism Settings popup is currently displayed.

        :return: True if the organism settings popup currently displayed, false
        otherwise.
        """
        org_sett_displayed = False
        if self.organism_displayed():
            org_sett_displayed = self.element_displayed("dijit_Dialog_4")
        return org_sett_displayed

    def open_org_settings(self):
        """
        Navigates to the "Organism Settings" popup from within the "Organism" 
        pane.

        :return: None.
        """
        self.go_to_organism()
        button = self.get_element("OrgSetting")
        button_text = self.get_text(element=button)
        if button_text == "Settings":
            self.click_element(element=button)

    def close_org_settings(self):
        """
        Closes the "Organism Settings" popup if it is open.

        :return: None.
        """
        if self.org_settings_displayed():
            self.click_element("indDone")

    def org_details_displayed(self):
        """
        Determines whether the details panel within the Organism window is
        currently displayed.
        
        :return: True if the details panel displayed, otherwise false. 
        """
        org_details_displayed = False
        if self.organism_displayed():
            org_details_displayed = self.element_displayed("rightDetail")
        return org_details_displayed

    def open_org_details(self):
        """
        Displays the Details panel within the Organism window if it is not
        already displayed.
        
        :return: None.
        """

        self.go_to_organism()
        if not self.org_details_displayed():
            self.click_element("OrgDetailsButton")

    def close_org_details(self):
        """
        Hides the Details panel within the Organism window if it is currently
        displayed.
        
        :return: None. 
        """
        self.go_to_organism()
        if self.org_details_displayed():
            self.click_element("OrgDetailsButton")