import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import openpyxl
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


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

    """
    # emissions by stage, grouped
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

    stage.show()
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

    """
    nutrients = pd.read_excel('../data/Swiss_food_composition_database(4).xlsx')
    print(nutrients.columns)

    fig = px.scatter(nutrients, y='Zinc (Zn) (mg)', x='Protein (g)', color='Category')
    fig.show()

    fig = px.scatter(nutrients, y='Vitamin A activity, RE (µg-RE)', x='Starch (g)', color='Category')
    fig.show()
    """

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

    all = ['Name', 'Category', 'Energy, kilojoules (kJ)', 'Fat, total (g)', 'Fatty acids, saturated (g)', 'Fatty acids, monounsaturated (g)', 'Fatty acids, polyunsaturated (g)', 'Cholesterol (mg)', 'Carbohydrates, available (g)', 'Sugars (g)', 'Starch (g)', 'Dietary fibres (g)', 'Protein (g)', 'Salt (NaCl) (g)', 'Alcohol (g)', 'Water (g)', 'Vitamin A activity, RE (µg-RE)', 'Vitamin A activity, RAE (µg-RE)', 'Retinol (µg)', 'Beta- carotene activity (µg-BCE)', 'Beta-carotene (µg)', 'Vitamin B1 (thiamine) (mg)']
    table = pd.read_excel('../data/Swiss_food_composition_database(4).xlsx', usecols=all)
    # , 'Vitamin B2 (riboflavin) (mg)', 'Vitamin B6 (pyridoxine) (mg)', 'Vitamin B12 (cobalamin) (µg)', 'Niacin (mg)', 'Folate (µg)', 'Panthotenic acid (mg)', 'Vitamin C (ascorbic acid) (mg)', 'Vitamin D (calciferol) (µg)', 'Vitamin E activity (mg-ATE)', 'Potassium (K) (mg)', 'Sodium (Na) (mg)', 'Chloride (Cl) (mg)', 'Calcium (Ca) (mg)', 'Magnesium (Mg) (mg)', 'Phosphorus (P) (mg)', 'Iron (Fe) (mg)', 'Iodide (I) (µg)', 'Zinc (Zn) (mg)'

    # standardize data
    selected_columns = ['Energy, kilojoules (kJ)', 'Fat, total (g)', 'Fatty acids, saturated (g)', 'Fatty acids, monounsaturated (g)', 'Fatty acids, polyunsaturated (g)', 'Cholesterol (mg)', 'Carbohydrates, available (g)', 'Sugars (g)', 'Starch (g)', 'Dietary fibres (g)', 'Protein (g)', 'Salt (NaCl) (g)', 'Alcohol (g)', 'Water (g)', 'Vitamin A activity, RE (µg-RE)', 'Vitamin A activity, RAE (µg-RE)', 'Retinol (µg)', 'Beta- carotene activity (µg-BCE)', 'Beta-carotene (µg)', 'Vitamin B1 (thiamine) (mg)']
    x = table.loc[:, selected_columns].values
    y = table.loc[:, ['Name', 'Category']].values

    x_standard = StandardScaler().fit_transform(x)

    # 2D PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(x_standard)

    principal_table = pd.DataFrame(data=principal_components, columns=['x', 'y'])

    # combine with name and category
    final_table = pd.concat([principal_table, table[['Name', 'Category']]], axis=1)
    print(final_table.columns)


    # TNSE
    tnse = TSNE(n_components=3, random_state=0)
    projections = tnse.fit_transform(x_standard)

    principal_table = pd.DataFrame(data=projections, columns=['x', 'y', 'z'])

    final_table = pd.concat([principal_table, table[['Name', 'Category']]], axis=1)
    print(final_table['Category'])


    # plot non-linear
    fig = px.scatter_3d(final_table, x=final_table['x'], y=final_table['y'], z=final_table['z'],
                        color=final_table['Category'], color_discrete_map=['palegoldenrod', 'darkorange', 'cornsilk', 'indigo', 'violet', 'mintcream',
                                                                           'mediumspringgreen', 'indigo', 'mediumspringgreen', 'mediumspringgreen',
                                                                           'mediumspringgreen', 'mediumseagreen', 'mediumseagreen', 'mediumseagreen',
                                                                           'indianred', 'goldenrod', 'violet', 'blueviolet', 'goldenrod', 'mediumseagreen',
                                                                           'mediumseagreen', 'violet', 'maroon', 'indianred', 'lightsalmon',
                                                                           'indigo, indianred', 'blueviolet', 'indigo', 'mintcream', 'blueviolet',
                                                                           'blueviolet', 'cornsilk', 'mintcream', 'gold', 'mintcream', 'cornsilk',
                                                                           'lavender', 'indigo', 'indigo', 'blueviolet', 'mintcream', 'blueviolet',
                                                                           'lavender', 'indigo', 'blueviolet', 'floralwhite', 'maroon', 'cornsilk',
                                                                           'indigo', 'indigo', 'indigo', 'lightsalmon', 'gold', 'gold', 'lavender',
                                                                           'lavender', 'lavender', 'mintcream', 'maroon', 'maroon', 'gold', 'cornsilk',
                                                                           'goldenrod', 'darkorange', 'goldenrod', 'blueviolet', 'maroon', 'lavender',
                                                                           'indigo', 'lightsalmon', 'maroon', 'maroon', 'maroon', 'lightblue', 'blueviolet',
                                                                           'mintcream', 'lightblue', 'blueviolet', 'cornsilk', 'blueviolet', 'lavender',
                                                                           'indigo', 'maroon', 'darkorange', 'indigo', 'lavender', 'maroon',
                                                                           'cornsilk', 'lavender', 'lavender', 'gold', 'maroon', 'maroon', 'lightblue',
                                                                           'mintcream', 'darkorange', 'lavender', 'gold', 'cornsilk', 'darkorange',
                                                                           'mediumspringgreen', 'indigo', 'mintcream', 'darkorange', 'mintcream',
                                                                           'cornsilk', 'indianred', 'lightblue', 'gold', 'indigo', 'mediumseagreen',
                                                                           'lightsalmon', 'lavender', 'lavender', 'lavender', 'green', 'maroon', 'goldenrod',
                                                                           'violet', 'violet', 'mintcream'])
    fig.update_traces(marker=dict(size=3))
    fig.show()

    # plot
    """
    schema = final_table.loc[:, ['x', 'y', 'z', 'Name', 'Category']]
    scatter_3d = go.Scatter3d(
        x=schema['x'],
        y=schema['y'],
        z=schema['z'],
        mode='markers',
        marker=dict(
            size=3,
            color=all
            #colorscale='Viridis'
        )
    )

    fig = go.Figure(data=[scatter_3d])
    fig.show()
    """


    #fig = px.scatter(final_table, x='x', y='y', color='Category')
    #fig.show()




    # data for sankey diagram
    #   Product                                 Use
    #   -------                                 Biofuel & Cie       Incineration        Soil fertilizer     Openland waste
    #   Juice (including molasses) 53.6%
    #   Bagasse                                 0.10                0.08                0                   0.10
    #   Straws (leaves and tops) (0.28)                             0.25                0.03
    #   Stems
    #   Press mud                               0                   0                   0.03


#                           Use                     By-product          Use
    #   Juice     50      Sugar production        Molasses (0.041)    Commercial sale
    #                       (M, WS, W)              (C, B, A, F)      Biofuel & Cie
    #             50      Ethanol production      Sugar (0.140)       Animal feed supplement
    #                       (W, V, E)             Wasterwater         Fertilizer
    #                                             Vinasse
    #                                               (B)
    #                                             Ethanol
    #                                             Syrup

    """
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=["Juice", "Bagasse", "Straws", "Press mud", "Wastewater",
                   "Sugar Production", "Ethanol Production", "Incineration",
                   "Bagasse Ash", "Raw Energy (Mechanical)", "Raw Energy (Thermal)", "Syrup", "Molasses", "Sugar", "Vinasse",
                   "Ethanol",
                   "Biofuel & Cie", "Commercial Sale & Food Production", "Openland disposal", "Fertilizer", "Raw Energy (Electrical)", "Other"],
            color=["rgb(245, 222, 179)", "rgb(255,160,122)", "rgb(240,128,128)", "rgb(233,150,122)", "rgb(143,188,143)",
                   "rgb(245, 222, 179)", "rgb(135,206,235)", "rgb(139,69,19)",
                   "rgb(169,169,169)", "rgb(189,183,107)", "rgb(189,183,107)", "rgb(255,140,0)", "rgb(128,0,0)",
                   "rgb(245, 222, 179)", "rgb(216,191,216)",
                   "rgb(135,206,235)",
                   "rgb(32,178,170)", "rgb(70,130,180)", "rgb(178,34,34)", "rgb(46,139,87)", "rgb(189,183,107)",
                   "rgb(128,128,128)"]
        ),
        link=dict(
            source=[0, 0,       1, 1, 1, 1, 1,      2, 2,   3,  4,      5, 5, 5, 5,         6, 6,           7, 7, 7, 7,         8, 8,        11,     12, 12, 12, 12,     13, 14, 14,     15],
            target=[5, 6,       7, 16, 18, 19, 15,  18, 19, 19, 19,     4, 11, 12, 13,      14, 15,         8, 20, 9, 10,       18, 21,      17,     17, 19, 21, 15,     17, 16, 19,     17],
            value=[26.8, 26.8,  3, 5, 5, 3, 1,      4, 1,   5,  21.924, 21.924, 0.5, 2, 1,  24.74, 2.061,   1, 0.25, 0.25, 1.5, 2.5, 0.5,    0.5,    0.5, 1, 0.25, 0.25, 1,  9, 15.7,    2.25],
            color=[  "rgba(245, 222, 179, 0.6)", "rgba(245, 222, 179, 0.6)", "rgba(255,160,122, 0.6)", "rgba(255,160,122, 0.6)", "rgba(255,160,122, 0.6)", "rgba(255,160,122, 0.6)", "rgba(255,160,122, 0.6)", "rgba(240,128,128,0.6)", "rgba(240,128,128,0.6)",
                     "rgba(233,150,122, 0.6)", "rgba(143,188,143, 0.6)",
                     "rgba(245, 222, 179, 0.6)", "rgba(245, 222, 179, 0.6)", "rgba(245, 222, 179, 0.6)", "rgba(245, 222, 179, 0.6)", "rgba(135,206,235, 0.6)", "rgba(135,206,235, 0.6)", "rgba(139,69,19, 0.6)", "rgba(139,69,19, 0.6)", "rgba(139,69,19, 0.6)", "rgba(139,69,19, 0.6)",
                     "rgba(169,169,169, 0.6)", "rgba(169,169,169, 0.6)", "rgba(255,140,0, 0.6)",
                     "rgba(128,0,0, 0.6)", "rgba(128,0,0, 0.6)", "rgba(128,0,0, 0.6)", "rgba(128,0,0, 0.6)", "rgba(245, 222, 179, 0.6)", "rgba(216,191,216, 0.6)", "rgba(216,191,216, 0.6)",
                     "rgba(135,206,235, 0.6)"]

    ))])

    fig.update_layout(title_text="Waste and by-products, processing of 1 ton of sugarcane", font_size=10)
    fig.show()
    """


