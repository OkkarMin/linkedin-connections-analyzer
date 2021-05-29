# LinkedIn Connections Analyzer

🔗 [https://linkedin-analzyer.herokuapp.com](https://okkarm.in/linkedin-connections-analyzer)

![GIF of end product](/assets/end_product.gif)

Hey hey 👋 , welcome to my LinkedIn connections analyzer. I recently found out that 
LinkedIn allow you to export your connections data in CSV format. I got curious and downloaded 
a copy for myself found out it contains informations that is publicly available to LinkedIn users. 
Data you are seeing now is my (Okkar Min's) connections data. If you would like to see your own 
data, just upload your Connections.csv obtained from LinkedIn using the uploader box

Do let me know how I could improve this!

# 🥞 Technology Stack

- 🎞 Framework : Streamlit
- 💄 UI Components : Plotly
- 🎬 Animations : Lottie

# Folder structure

```
linkedin-connections-analyzer/
┣━━ 📂 .streamlit           # Streamlit configurations
┃ ┗━━ config.toml           # Custom theme
┣━━ 📂 assets               # Public assets
┃ ┣━━ end_product.gif
┃ ┣━━ hand_shake_mask.png
┃ ┗━━ linkedin_logo.png
┣━━ 📂 utils                # Helper functions
┃ ┗━━ __init__.py
┣━━ .gitignore
┣━━ Procfile                # For Heroku
┣━━ README.md
┣━━ app.py                  # THE MVP
┣━━ okkar_connections.csv
┣━━ requirements.txt    
┗━━ setup.sh                # For Heroku
```

# How to run
1. Clone this repository
2. Install dependencies
3. `streamlit run app.py`

```bash
git clone https://github.com/OkkarMin/linkedin-connections-analyzer.git
cd linkedin-connections-analzyer
pip install -r requirements.txt
streamlit run app.py
``` 
