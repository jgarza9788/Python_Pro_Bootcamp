exitbuttons = browser.find_elements_by_css_selector('button[aria-label="Dismiss"]')
                for eb in exitbuttons:
                    try:
                        eb.click()
                