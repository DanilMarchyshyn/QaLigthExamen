class LoginConstants:
    EMAIL_FIELD_NAME = 'email'
    PASSWORD_FIELD_XPATH = "//input[@placeholder='Password']"
    LOGIN_BUTTON_XPATH = "//button[@type='submit']"
    ERROR_MESSAGE_EMAIL_XPATH = "//div[@class='form-inputs']/div[1]/span/div/p"
    ERROR_MESSAGE_PASSWORD_XPATH = "//div[@class='form-inputs']/div[2]/span/div/p"
    ERROR_MESSAGE_REQUIRED_TEXT = 'This field is required!'
    ERROR_MESSAGE_INVALID_XPATH = "//div[@class='form-block']/form/p"
    ERROR_MESSAGE_INVALID_TEXT = 'Invalid email or password'
    CREATE_ACC_LINK_XPATH = '//*[@class="auth-switch"]/p/a'
    LOGOUT_LINK_XPATH = '//*[@class="signOutFooter"]/a'
    LOGOUT_LINK_TEXT = "Logout"
