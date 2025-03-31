import requests
from config import API_KEYS, QUERIES

def fetch_news(pais, query, location, lang, limit=5):
    """Busca notícias e retorna dados formatados"""
    url = "https://serpapi.com/search.json"
    
    params = {
        "q": query,
        "tbm": "nws",
        "location": location,
        "hl": lang,
        "api_key": API_KEYS['serpapi'],
        "num": limit
    }
    
    # Configuração adicional para Brasil
    if pais == "Cosméticos Capilares - Brasil":
        params["tbs"] = "sbd:1,nsb:1"  # Ordenar por data e remover similares

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("news_results", [])
    except Exception as e:
        print(f"Erro ao buscar notícias para {pais}: {str(e)}")
        return []

def generate_news_html(pais, news_data):
    """Gera HTML para as notícias"""
    if not news_data:
        return f"""
        <div class="news-card">
            <h3>📰 Notícias sobre {pais}</h3>
            <p>Nenhuma notícia encontrada.</p>
        </div>
        """
    
    periodo = "" if pais == "Cosméticos Capilares - Brasil" else ""
    
    html = f"""
    <div class="news-card">
        <h3>📰 Notícias sobre {pais}{periodo}</h3>
        <div class="news-container">
    """
    
    for news in news_data[:5]:
        if not isinstance(news, dict):
            continue
            
        title = news.get('title', 'Sem título')
        snippet = news.get('snippet', 'Sem resumo')
        source = news.get('source', {})
        source_name = source.get('name', 'Fonte desconhecida') if isinstance(source, dict) else str(source)
        date = news.get('date', '')
        link = news.get('link', '#')
        
        html += f"""
            <div class="news-item">
                <h4>{title}</h4>
                <p class="news-snippet">{snippet}</p>
                <p class="news-source">{source_name} - {date}</p>
                <a href="{link}" target="_blank" class="news-link">Leia mais →</a>
            </div>
        """
    
    html += """
        </div>
    </div>
    """
    return html

def get_all_news_html():
    """Obtém HTML de notícias para todas as consultas"""
    results = []
    
    # Notícias do Brasil
    brasil_news = fetch_news("Cosméticos Capilares - Brasil", **QUERIES["Brasil"])
    results.append(generate_news_html("Cosméticos Capilares - Brasil", brasil_news))
    
    # Notícias dos EUA
    eua_news = fetch_news("Cosméticos Capilares - EUA", **QUERIES["EUA"])
    results.append(generate_news_html("Cosméticos Capilares - EUA", eua_news))
    
    # Notícias da Salon Line
    salon_news = fetch_news("Salon Line", **QUERIES["Salon Line"], limit=2)
    results.append(generate_news_html("Salon Line", salon_news))
    
    return results