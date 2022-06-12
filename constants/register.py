class RegisterConstants:
    FULLNAME_FIELD_XPATH = '//input[@placeholder="Full Name"]'
    EMAIL_FIELD_XPATH = '//input[@placeholder="Email"]'
    PASSWORD_FIELD_XPATH = "//input[@placeholder='Password']"
    PHONE_FIELD_XPATH = '//input[@placeholder="Phone"]'
    TERMS_CHECKBOX_XPATH = "//input[@type='checkbox']"
    CREATE_ACC_BUTTON_XPATH = "//button[@type='submit']"
    ERROR_MESSAGE_AGREE_TERMS_XPATH = '//*[@class="form-block"]/form/p'
    ERROR_MESSAGE_AGREE_TERMS_TEXT = 'You must agree with terms and conditions'
    ERROR_MESSAGE_FULLNAME_XPATH = "//div[@class='form-inputs']/div[1]/span/div/p"
    ERROR_MESSAGE_EMAIL_XPATH = "//div[@class='form-inputs']/div[2]/span/div/p"
    ERROR_MESSAGE_REQUIRED_TEXT = 'This field is required!'
