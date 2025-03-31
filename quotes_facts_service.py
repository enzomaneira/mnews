import requests
from config import API_KEYS

def get_quote():
    """Obtém uma citação aleatória"""
    url = "https://api.api-ninjas.com/v1/quotes"
    headers = {"X-Api-Key": API_KEYS['ninjas']}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            'quote': data[0]['quote'],
            'author': data[0]['author']
        }
    except Exception as e:
        print(f"Erro ao obter citação: {e}")
        return {
            'quote': "A vida é o que acontece enquanto você está ocupado fazendo outros planos.",
            'author': "John Lennon"
        }

def get_fact():
    """Obtém um fato curioso"""
    url = "https://api.api-ninjas.com/v1/facts"
    headers = {"X-Api-Key": API_KEYS['ninjas']}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()[0]['fact']
    except Exception as e:
        print(f"Erro ao obter fato: {e}")
        return "O cére humano pode gerar cerca de 23 watts de energia, o suficiente para alimentar uma lâmpada."

def generate_quote_html(quote_data):
    """Gera HTML para a citação"""
    return f"""
    <div class="quote-card">
        <h3><i class="fas fa-quote-left"></i> Quote of The Day </h3>
        <blockquote>
            <p>"{quote_data['quote']}"</p>
            <footer>— {quote_data['author']}</footer>
        </blockquote>
    </div>
    """

def generate_fact_html(fact):
    """Gera HTML para o fato"""
    return f"""
    <div class="fact-card">
        <h3><i class="fas fa-lightbulb"></i> Did you knew ?</h3>
        <p>{fact}</p>
    </div>
    """