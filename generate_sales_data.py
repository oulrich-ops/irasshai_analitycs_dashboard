import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Données des produits récupérés depuis le site iRASSHAi
products_data = [
    # Riz & Nouilles
    {"product": "Ramen instantanés au miso vegan", "category": "Riz & Nouilles", "unit_price": 3.20},
    {"product": "Ramen instantanés à la sauce soja vegan", "category": "Riz & Nouilles", "unit_price": 3.20},
    {"product": "Nouilles soba", "category": "Riz & Nouilles", "unit_price": 4.90},
    {"product": "Ramen instantanés au miso sans gluten", "category": "Riz & Nouilles", "unit_price": 4.10},
    {"product": "Nouilles Udon 7 portions", "category": "Riz & Nouilles", "unit_price": 5.50},
    {"product": "Nouilles soba 100% sarrasin", "category": "Riz & Nouilles", "unit_price": 5.50},
    {"product": "Ramen instantanés sauce soja sans gluten", "category": "Riz & Nouilles", "unit_price": 4.10},
    {"product": "Ramen instantanés tonkotsu sans gluten", "category": "Riz & Nouilles", "unit_price": 4.10},
    {"product": "Nouilles Udon de Kagawa 3 portions", "category": "Riz & Nouilles", "unit_price": 3.90},
    {"product": "Ramen instantanés au potage vegan", "category": "Riz & Nouilles", "unit_price": 3.20},
    {"product": "Ramen à la sauce soja vegan 3 portions", "category": "Riz & Nouilles", "unit_price": 4.50},
    {"product": "Nouilles yakisoba précuites avec sauce 3 portions", "category": "Riz & Nouilles", "unit_price": 5.60},
    {"product": "Nouilles udon au curry 2 portions", "category": "Riz & Nouilles", "unit_price": 4.90},
    {"product": "Nouilles udon précuites avec sauce 3 portions", "category": "Riz & Nouilles", "unit_price": 5.60},
    {"product": "Ramen au miso vegan 3 portions", "category": "Riz & Nouilles", "unit_price": 4.50},
    {"product": "Ramen au yuzu et à la sauce soja 2 portions", "category": "Riz & Nouilles", "unit_price": 5.65},
    {"product": "Nouilles udon précuites avec bouillon 3 portions", "category": "Riz & Nouilles", "unit_price": 5.60},
    {"product": "Ramen instantanés au curry vegan 2 portions", "category": "Riz & Nouilles", "unit_price": 4.90},
    {"product": "Nouilles yakisoba précuites 5 portions", "category": "Riz & Nouilles", "unit_price": 6.50},
    {"product": "Nouilles udon iRASSHAi", "category": "Riz & Nouilles", "unit_price": 4.50},
    {"product": "Nouilles soba d'Okuizumo", "category": "Riz & Nouilles", "unit_price": 6.90},
    {"product": "Nouilles soba 100% sarrasin premium", "category": "Riz & Nouilles", "unit_price": 9.40},
    {"product": "Ramen tantan men piquant vegan 2 portions", "category": "Riz & Nouilles", "unit_price": 4.90},
    {"product": "Nouilles udon précuites 3 portions", "category": "Riz & Nouilles", "unit_price": 5.40},
    {"product": "Nouilles soba à l'igname", "category": "Riz & Nouilles", "unit_price": 4.10},
    {"product": "Nouilles udon au matcha", "category": "Riz & Nouilles", "unit_price": 3.50},
    {"product": "Nouilles yakisoba avec sauce 2 portions", "category": "Riz & Nouilles", "unit_price": 4.50},
    {"product": "Ramen au yuzu vegan 2 portions", "category": "Riz & Nouilles", "unit_price": 5.65},
    
    # Essentiels iRASSHAi (produits de la marque)
    {"product": "Sauce soja iRASSHAi", "category": "Essentiels", "unit_price": 6.90},
    {"product": "Riz japonais iRASSHAi", "category": "Essentiels", "unit_price": 8.50},
    {"product": "Dashi iRASSHAi", "category": "Essentiels", "unit_price": 7.90},
    {"product": "Miso iRASSHAi", "category": "Essentiels", "unit_price": 7.50},
    {"product": "Matcha iRASSHAi", "category": "Essentiels", "unit_price": 12.90},
    {"product": "Vinaigre de riz iRASSHAi", "category": "Essentiels", "unit_price": 5.90},
    {"product": "Mirin iRASSHAi", "category": "Essentiels", "unit_price": 6.50},
    {"product": "Sauce teriyaki iRASSHAi", "category": "Essentiels", "unit_price": 6.90},
    
    # Condiments & Sauces
    {"product": "Wasabi", "category": "Condiments", "unit_price": 8.90},
    {"product": "Yuzu kosho", "category": "Condiments", "unit_price": 9.50},
    {"product": "Vinaigrette au sésame", "category": "Condiments", "unit_price": 7.90},
    {"product": "Sauce ponzu", "category": "Condiments", "unit_price": 6.90},
    
    # Boissons
    {"product": "Thé vert japonais", "category": "Boissons", "unit_price": 8.90},
    {"product": "Saké", "category": "Boissons", "unit_price": 15.90},
    {"product": "Amazake", "category": "Boissons", "unit_price": 6.90},
    
    # Coffrets
    {"product": "Coffret découverte thés", "category": "Coffrets", "unit_price": 29.90},
    {"product": "Coffret art de cuisiner japonais", "category": "Coffrets", "unit_price": 59.90},
    {"product": "Coffret matcha", "category": "Coffrets", "unit_price": 39.90},
]

# Régions françaises pour la distribution géographique
regions = [
    "Île-de-France", "Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur",
    "Nouvelle-Aquitaine", "Occitanie", "Hauts-de-France", "Bretagne",
    "Grand Est", "Pays de la Loire", "Normandie", "Bourgogne-Franche-Comté",
    "Centre-Val de Loire", "Corse"
]

# Pondération pour rendre certaines régions plus actives (Paris, Lyon, etc.)
region_weights = [0.35, 0.15, 0.12, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.01, 0.01]

# Fonction pour générer les données de ventes
def generate_sales_data(num_records=1000, start_date='2024-01-01', end_date='2024-12-31'):
    """
    Génère des données de ventes réalistes pour iRASSHAi
    
    Args:
        num_records: Nombre de commandes à générer
        start_date: Date de début
        end_date: Date de fin
    
    Returns:
        DataFrame pandas avec les données de ventes
    """
    np.random.seed(42)
    random.seed(42)
    
    sales_records = []
    
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    for i in range(num_records):
        # Générer une date aléatoire
        days_between = (end - start).days
        random_days = random.randint(0, days_between)
        order_date = start + timedelta(days=random_days)
        
        # Tendance saisonnière : plus de ventes en automne/hiver
        month = order_date.month
        seasonal_factor = 1.0
        if month in [10, 11, 12, 1, 2]:  # Automne/Hiver
            seasonal_factor = 1.3
        elif month in [6, 7, 8]:  # Été
            seasonal_factor = 0.8
        
        # Choisir un produit aléatoire
        product_info = random.choice(products_data)
        
        # Quantité vendue (avec distribution réaliste)
        # Les produits moins chers sont vendus en plus grande quantité
        if product_info["unit_price"] < 5:
            units_sold = np.random.choice([1, 2, 3, 4, 5, 6], p=[0.3, 0.25, 0.2, 0.15, 0.07, 0.03])
        elif product_info["unit_price"] < 10:
            units_sold = np.random.choice([1, 2, 3, 4], p=[0.4, 0.35, 0.2, 0.05])
        else:  # Produits premium
            units_sold = np.random.choice([1, 2, 3], p=[0.6, 0.3, 0.1])
        
        # Appliquer le facteur saisonnier
        if random.random() < seasonal_factor - 1:
            units_sold += 1
        
        # Région (avec pondération)
        region = np.random.choice(regions, p=region_weights)
        
        # Calculer les ventes
        sales = round(units_sold * product_info["unit_price"], 2)
        
        # Créer l'enregistrement
        record = {
            "Order ID": f"ORD-{1000 + i}",
            "Date": order_date.strftime('%Y-%m-%d'),
            "Product": product_info["product"],
            "Category": product_info["category"],
            "Region": region,
            "Units Sold": units_sold,
            "Unit Price": product_info["unit_price"],
            "Sales": sales
        }
        
        sales_records.append(record)
    
    # Créer le DataFrame
    df = pd.DataFrame(sales_records)
    
    # Trier par date
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df


sales_df = generate_sales_data(num_records=2500, start_date='2022-01-01', end_date='2024-12-31')


output_file = './data/irasshai_sales_data.csv'
sales_df.to_csv(output_file, index=False, encoding='utf-8-sig')


