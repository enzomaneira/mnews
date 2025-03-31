import os

# Configurações de Email
SMTP_CONFIG = {
    'username': os.environ['SMTP_USERNAME'],        
    'password': os.environ['SMTP_PASSWORD'],       
    'server': os.environ.get('SMTP_SERVER', "email-smtp.us-east-1.amazonaws.com"),
    'port': int(os.environ.get('SMTP_PORT', "587")),
    'from_email': os.environ['FROM_EMAIL'],       
    'to_email': os.environ['TO_EMAIL']              
}

# Chaves de API
API_KEYS = {
    'serpapi': os.environ['SERPAPI_KEY'],          
    'tomorrowio': os.environ['WEATHER_API_KEY'],    
    'ninjas': os.environ['NINJAS_API_KEY']       
}

# Palavras-chave para busca
KEYWORDS = {
    'pt': "shampoo OR cabelo OR hidratação capilar OR tratamento capilar OR transição capilar OR cuidados com cabelo OR cabelos cacheados",
    'en': "hair cosmetics OR shampoo OR haircare OR hair hydration OR hair treatment",
    'salon_line': "salon line"
}

# Consultas pré-configuradas
QUERIES = {
    "Brasil": {"query": KEYWORDS['pt'], "location": "Brazil", "lang": "pt"},
    "EUA": {"query": KEYWORDS['en'], "location": "United States", "lang": "en"},
    "Salon Line": {"query": KEYWORDS['salon_line'], "location": "Brazil", "lang": "pt"}
}

# Cidades para previsão do tempo
CITIES = ["São Paulo", "Jandira", "Barueri"]