import os

SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY')
JWT_SECRET = os.getenv('JWT_SECRET_KEY')

APP_NAME="Opencity Reporter"
APP_ICON = "/static/assets/images/logo.png"
ENABLE_CORS = True 
CORS_OPTIONS = { 
        "supports_credentials": True, 
        "allow_headers": "*", 
        "expose_headers": "*", 
        "resources": "*", 
        "origins": ["http://localhost:4200","http://localhost:3000"] 
}
        

# Dashboard embedding 
GUEST_ROLE_NAME = "Gamma" 
GUEST_TOKEN_JWT_SECRET = JWT_SECRET
GUEST_TOKEN_JWT_ALGO = "HS256" 
GUEST_TOKEN_HEADER_NAME = "X-GuestToken" 
GUEST_TOKEN_JWT_EXP_SECONDS = 300 # 5 minutes

# Setting it to '/' would take the user to '/superset/welcome/'
LOGO_TARGET_PATH = '/'

# Specify tooltip that should appear when hovering over the App Icon/Logo
LOGO_TOOLTIP = "Opencity"

# Specify any text that should appear to the right of the logo
LOGO_RIGHT_TEXT = "Opencity"

FAVICONS = [{"href": "/static/assets/images/favicon.png"}]

THEME_OVERRIDES = {
    "colors": {
        "text": {
            "label": '#414141',
            "help": '#FFD21A'
        },
        "primary": {
            "base": '#036D6D',
        },
        "secondary": {
            "base": '#0ACCDB',
        },
        "grayscale": {
            "base": 'orange',
        },
        "error": {
            "base": 'Pink'
        }
    },
}

EXTRA_CATEGORICAL_COLOR_SCHEMES = [
     {
         "id": 'opencity_report_color',
         "description": '',
         "label": 'Opencity Color',
         "colors":
          ['#036D6D', '#036D6D', '#75E00E', '#FFD21A', '#414141', '#AA5ECB', '#CE42A1',
          '#EC487D', '#FA6E67', '#FFA064', '#EEDD55', '#9977BB', '#BBAA44', '#DDCCDD']
     }]
FEATURE_FLAGS = {"EMBEDDED_SUPERSET": True,"ENABLE_TEMPLATE_PROCESSING": True}
