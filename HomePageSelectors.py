from selenium.webdriver.common.by import By

class HomePageSelectors(object):

    top_nav_list = '//nav/div/ul[@data-level="1"]/li'

    accept_consent_btn = (By.ID, 'onetrust-accept-btn-handler')

    scores_btn = '//a[text()="SCORES"]'

    scores_header = '//h1[text()="Live Football Scores, Fixtures & Results"]'
