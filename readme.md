# 🍜 iRASSHAi Analytics Dashboard


> Analyse des ventes d’un restaurant et épicerie japonaise à Paris
> **Pipeline** : CSV → BigQuery → Looker Studio
> *Données basées sur les vrais produits et prix du site [irasshai.co](https://irasshai.co/)*

![Status](https://img.shields.io/badge/status-production-success)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![BigQuery](https://img.shields.io/badge/BigQuery-ready-blue)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-ready-orange)


---

##  Aperçu

![Dashboard iRASSHAi](/images/demo_dashboard_irasshai.gif)

---

##  Dashboard Live -- Cliquez dessous !

**[Voir le dashboard interactif](https://lookerstudio.google.com/u/0/reporting/d8fe067e-6490-45ae-87a2-e61de75d6328/page/yR8eF)**


---

##  Architecture

![Architecture Data Pipeline](/images/architectureIrasshaiProject.png)

- **Source** : Données synthétiques (2500 commandes, 2022-2024)
- **Storage** : BigQuery (vues SQL optimisées)
- **Visualisation** : Looker Studio (dashboard interactif)

---

## Installation

```bash
git clone https://github.com/[ton-username]/irasshai-dashboard.git
cd irasshai-dashboard
pip install pandas numpy
python scripts/generate_irasshai_sales_data.py

```

---

##  License

Les données sont synthétiques et les produits sont utilisés à titre d'exemple 
depuis le catalogue public d'iRASSHAi.

---

**Fait avec ❤️ et 🍜 pour iRASSHAi**

*"いらっしゃい" - Bienvenue dans le monde de la data japonaise !*

---
