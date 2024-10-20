from flask import Flask, render_template, request
import sqlite3
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Fetch data from database
def fetch_data(query):
    conn = sqlite3.connect('furever_data.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize', methods=['POST'])
def visualize():
    pet_type = request.form['pet_type']
    query = f"SELECT * FROM pets WHERE PetType = '{pet_type}'"
    df = fetch_data(query)
    
    # Create a plot based on user selection
    fig = px.bar(df, x='AgeMonths', y='AdoptionLikelihood', title=f'Adoption Likelihood for {pet_type}')
    plot_div = fig.to_html(full_html=False)
    
    return render_template('index.html', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True)
