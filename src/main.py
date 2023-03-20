import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import openpyxl


def merge_and_create_plots(left_df, right_df, lcolumn_name, rcolumn_name):
    merged = left_df.merge(right_df, how='inner', on='Entity')

    plot = px.scatter(merged, x=lcolumn_name, y=rcolumn_name, color='Entity')
    plot.show()

    plot2 = px.scatter(merged, x=rcolumn_name, y=lcolumn_name, color='Entity')
    plot2.show()


def descending_bar_plot(df, rcolumn_name, lcolumn_name='Entity'):
    fig = px.bar(df, x=lcolumn_name, y=rcolumn_name)
    fig.update_layout(xaxis={'categoryorder': 'total descending'})
    fig.show()


def extract_type_from_column(df, column_name, type_name):
    return df[df[column_name].isin([type_name])]


if __name__ == "__main__":
    """
    water = pd.read_csv('../data/WaterUse.csv')
    land = pd.read_csv('../data/LandUse.csv')
    scarcity = pd.read_csv('../data/Scarcity-WeightedWater.csv')
    carbon = pd.read_csv('../data/CarbonEmissions.csv')
    eutrophication = pd.read_csv('../data/Eutrophication.csv')

    
    print(water.columns)
    print(land.columns)
    print(scarcity.columns)
    print(carbon.columns)
    print(eutrophication.columns)
    """

    # scatter plots to detect correlation between any two factors
    """
    merge_and_create_plots(water, land, 'Freshwater withdrawals per kilogram (Poore & Nemecek, 2018)', 'Land use per kilogram (Poore & Nemecek, 2018)')

    # most interesting --> correlation between scarcity and consumption
    merge_and_create_plots(water, scarcity, 'Freshwater withdrawals per kilogram (Poore & Nemecek, 2018)', 'Scarcity-weighted water use per kilogram (Poore & Nemecek, 2018)')
    merge_and_create_plots(water, carbon, 'Freshwater withdrawals per kilogram (Poore & Nemecek, 2018)', 'GHG emissions per kilogram (Poore & Nemecek, 2018)')
    merge_and_create_plots(carbon, land, 'GHG emissions per kilogram (Poore & Nemecek, 2018)', 'Land use per kilogram (Poore & Nemecek, 2018)')
    merge_and_create_plots(scarcity, eutrophication, 'Scarcity-weighted water use per kilogram (Poore & Nemecek, 2018)', 'Eutrophying emissions per kilogram (Poore & Nemecek, 2018)')
    """

    # emissions by stage, grouped
    """
    carbon_by_stage = pd.read_csv('../data/CarbonEmissionsByStage.csv')
    # print(carbon_by_stage.columns)

    # bar chart with all carbon emissions per stage of production
    stage = go.Figure(
        data=[
            go.Bar(name='Land Use', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_land_use']),
            go.Bar(name='Farm', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_farm']),
            go.Bar(name='Animal Feed', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_animal_feed']),
            go.Bar(name='Processing', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_processing']),
            go.Bar(name='Transport', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_transport']),
            go.Bar(name='Retail', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_retail']),
            go.Bar(name='Packaging', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_packaging']),
            go.Bar(name='Losses', x=carbon_by_stage['Entity'], y=carbon_by_stage['food_emissions_losses']),
        ]
    )

    # stage.show()
    """

    # bar charts with each stage independent and in descending order of emitting entity
    """
    descending_bar_plot(carbon_by_stage, 'food_emissions_land_use')
    descending_bar_plot(carbon_by_stage, 'food_emissions_farm')
    descending_bar_plot(carbon_by_stage, 'food_emissions_animal_feed')
    descending_bar_plot(carbon_by_stage, 'food_emissions_processing')
    descending_bar_plot(carbon_by_stage, 'food_emissions_transport')
    descending_bar_plot(carbon_by_stage, 'food_emissions_retail')
    descending_bar_plot(carbon_by_stage, 'food_emissions_packaging')
    descending_bar_plot(carbon_by_stage, 'food_emissions_losses')
    """
    # --> the most important emission stage is what they call Farm emissions, 2nd is food losses, 3rd is animal feed

    nutrients = pd.read_excel('../data/Swiss_food_composition_database(4).xlsx')
    print(nutrients.columns)

    """
    cereal = extract_type_from_column(nutrients, 'Category', 'Cereal products, pulses and potatoes/Other cereal products')
    descending_bar_plot(cereal, 'Protein (g)', 'Name')
    descending_bar_plot(cereal, 'Selenium (Se) (µg)', 'Name')
    descending_bar_plot(cereal, 'Energy, kilojoules (kJ)', 'Name')
    """

    """
    # Folate
    fig = px.scatter(nutrients, y='Folate (µg)', x='Protein (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Folate (µg)', x='Starch (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Folate (µg)', x='Dietary fibres (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Folate (µg)', x='Fat, total (g)', color='Category')
    fig.show()

    # Vitamine A
    fig = px.scatter(nutrients, y='Vitamin A activity, RE (µg-RE)', x='Starch (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Vitamin A activity, RE (µg-RE)', x='Protein (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Vitamin A activity, RE (µg-RE)',  x='Sugars (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Vitamin A activity, RE (µg-RE)', x='Dietary fibres (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Vitamin A activity, RE (µg-RE)', x='Fat, total (g)', color='Category')
    fig.show()

    # Zinc
    # interesting one
    fig = px.scatter(nutrients, y='Zinc (Zn) (mg)', x='Protein (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Zinc (Zn) (mg)', x='Starch (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Zinc (Zn) (mg)', x='Dietary fibres (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Zinc (Zn) (mg)', x='Fat, total (g)', color='Category')
    fig.show()

    # Iodide
    fig = px.scatter(nutrients, y='Iodide (I) (µg)', x='Protein (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Iodide (I) (µg)', x='Starch (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Iodide (I) (µg)', x='Dietary fibres (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Iodide (I) (µg)', x='Fat, total (g)', color='Category')
    fig.show()

    # Salt
    fig = px.scatter(nutrients, y='Salt (NaCl) (g)', x='Protein (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Salt (NaCl) (g)', x='Starch (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Salt (NaCl) (g)', x='Dietary fibres (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Salt (NaCl) (g)', x='Fat, total (g)', color='Category')
    fig.show()
    """





