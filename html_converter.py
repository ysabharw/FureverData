import sqlite3
import pandas as pd
import plotly.express as px

# Connect to SQLite database
conn = sqlite3.connect('furever_data.db')

# Load data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM pets", conn)

# Example 1: Bar chart for Pet Type vs Adoption Likelihood
def bar_chart_pet_type_vs_adoption():
    grouped = df.groupby('PetType')['AdoptionLikelihood'].mean().reset_index()
    fig = px.bar(grouped, x='PetType', y='AdoptionLikelihood', title='Adoption Likelihood by Pet Type')
    fig.write_html("bar_chart_pet_type_vs_adoption.html")

# Example 2: Pie chart for Vaccination Status
def pie_chart_vaccination_status():
    vaccinated = df.groupby('Vaccinated')['AdoptionLikelihood'].mean().reset_index()
    vaccinated['Status'] = vaccinated['Vaccinated'].apply(lambda x: 'Vaccinated' if x == 1 else 'Not Vaccinated')
    fig = px.pie(vaccinated, values='AdoptionLikelihood', names='Status', title='Adoption Likelihood by Vaccination Status')
    fig.write_html("pie_chart_vaccination_status.html")

# Example 3: Scatter plot for Weight vs Adoption Likelihood
def scatter_plot_weight_vs_adoption():
    fig = px.scatter(df, x='WeightKg', y='AdoptionLikelihood', color='PetType',
                     title='Weight vs Adoption Likelihood')
    fig.write_html("scatter_plot_weight_vs_adoption.html")

# Example 4: Box plot for Age Distribution by Pet Type
def box_plot_age_by_pet_type():
    fig = px.box(df, x='PetType', y='AgeMonths', color='PetType',
                 title='Age Distribution by Pet Type')
    fig.write_html("box_plot_age_by_pet_type.html")

# Example 5: Histogram for Time in Shelter vs Adoption Likelihood
def histogram_time_in_shelter():
    fig = px.histogram(df, x='TimeInShelterDays', color='AdoptionLikelihood', nbins=30,
                       title='Time in Shelter vs Adoption Likelihood')
    fig.write_html("histogram_time_in_shelter.html")

# Run all visualizations
bar_chart_pet_type_vs_adoption()
pie_chart_vaccination_status()
scatter_plot_weight_vs_adoption()
box_plot_age_by_pet_type()
histogram_time_in_shelter()

# Close the database connection
conn.close()
