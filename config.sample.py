from paypal import PayPalConfig
from paypal import PayPalInterface

config = PayPalConfig(API_USERNAME = "XXXXXX_XXXXXXXXXX_XXX_api1.XXXXX.XX",
                      API_PASSWORD = "xxxxxxxxxx",
                      API_SIGNATURE = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                      DEBUG_LEVEL=0)

interface = PayPalInterface(config=config)
