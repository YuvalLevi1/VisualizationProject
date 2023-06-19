import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.set_page_config(page_title='NBA statistics',
                   page_icon='data:image/jpeg;base64,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',
                   initial_sidebar_state='expanded',
                   layout="wide")

# Data Loading
data = pd.read_csv('Data/all_seasons.csv')
country_codes = pd.read_csv('Data/country_code.csv')

# Data preprocessing
data['season'] = data['season'].str.split('-').str[0].astype(int)
data.loc[data['team_abbreviation'] == 'VAN', 'team_abbreviation'] = 'MEM'
data.loc[data['team_abbreviation'] == 'SEA', 'team_abbreviation'] = 'OKC'
data.loc[data['team_abbreviation'] == 'NOK', 'team_abbreviation'] = 'NOP'
data.loc[data['team_abbreviation'] == 'CHH', 'team_abbreviation'] = 'CHA'
data.loc[data['team_abbreviation'] == 'NJN', 'team_abbreviation'] = 'BKN'
data.loc[data['team_abbreviation'] == 'NOH', 'team_abbreviation'] = 'NOP'

country_codes = country_codes.drop(['code_2digit'], axis=1)
country_codes.rename(columns={'Country_name': 'country'}, inplace=True)
data = pd.merge(data, country_codes, on='country', how='left')
data.rename(columns={'code_3digit': 'code'}, inplace=True)
data['code'] = data['code'].fillna('USA')


def norm(old, new):
    mean_value = data[old].mean()
    std_value = data[old].std()
    data[new] = (data[old] - mean_value) / std_value


norm('player_height', 'height')
norm('player_weight', 'weight')
norm('reb', 'rebb')
norm('ast', 'astt')
norm('pts', 'ptss')

# Parameters
seasons = list(np.unique(data['season']))

teams = list(np.unique(data['team_abbreviation']))
teams_dict = {}
for t in teams:
    teams_dict[t] = f'NBA_LOGOS/{t}.png'


def create_slide_bar(key):
    _, c, _ = st.columns((0.1, 2, 0.5))
    with c:
        selected = st.select_slider("Drag the point on the slide bar to choose seasons range:", seasons, key=f's{key}')
    return selected


# First plot
# Slide bar
selected_season = create_slide_bar(1)

# Teams filter
_, col1, _, col2, _ = st.columns((0.1, 1.4, .1, 2.2, 0.1))
with col1:
    selected_team = st.multiselect('Select NBA teams:', teams)
with col2:
    sel_teams = []
    if selected_team:
        for team in selected_team:
            sel_teams.append(teams_dict[team])
    else:
        sel_teams.append('NBA_LOGOS/NBA_LOGO.jpg')
    st.image(sel_teams, width=80)

# Create the graph
if not selected_team:
    filtered_data = data.loc[data['season'] <= selected_season]
else:
    filtered_data = data.loc[(data['season'] <= selected_season) & (data['team_abbreviation'].isin(selected_team))]

_, col, _, col2, _ = st.columns((0.1, 3.3, 0.1, 0.7, 0.1))
with col2:
    for _ in range(10):
        st.write('')

    st.write('**Choose:**')

    show_line1 = st.checkbox('Points', value=False)
    show_line3 = st.checkbox('Rebounds', value=False)
    show_line4 = st.checkbox('Assists', value=False)
    show_line2 = st.checkbox('Height', value=False)
    show_line5 = st.checkbox('Weight', value=False)

with col:
    if len(filtered_data) == 0:
        fig, ax = plt.subplots()
        ax.axis('off')
        ax.set_xlim([1996, 2019])

    else:
        filtered_data = filtered_data.groupby('season')[['ptss', 'rebb', 'astt', 'height', 'weight', 'pts', 'reb', 'ast',
                                                         'player_height', 'player_weight']].mean().reset_index()

        trace1 = go.Scatter(x=seasons, y=list(filtered_data['ptss']), name='Points',
                            hovertemplate='Season: %{x}<br>Points: %{customdata[4]}')
        trace2 = go.Scatter(x=seasons, y=list(filtered_data['height']), name='Height',
                            hovertemplate='Season: %{x}<br>Height: %{customdata[0]}')
        trace3 = go.Scatter(x=seasons, y=list(filtered_data['rebb']), name='Rebounds',
                            hovertemplate='Season: %{x}<br>Rebounds: %{customdata[2]}')
        trace4 = go.Scatter(x=seasons, y=list(filtered_data['astt']), name='Assists',
                            hovertemplate='Season: %{x}<br>Assists: %{customdata[3]}')
        trace5 = go.Scatter(x=seasons, y=list(filtered_data['weight']), name='Weight',
                            hovertemplate='Season: %{x}<br>Weight: %{customdata[1]}')

        # Assign custom data to each trace
        h = [[round(i, 2)] for i in list(filtered_data['player_height'])]
        w = [[round(i, 2)] for i in list(filtered_data['player_weight'])]
        r = [[round(i, 2)] for i in list(filtered_data['reb'])]
        a = [[round(i, 2)] for i in list(filtered_data['ast'])]
        p = [[round(i, 2)] for i in list(filtered_data['pts'])]
        custom = [[h[i], w[i], r[i], a[i], p[i]] for i in range(len(h))]

        trace1.customdata = trace2.customdata = trace3.customdata = trace4.customdata = trace5.customdata = custom

        layout = go.Layout(width=1000, height=600, title={
            'text': 'Comparison between the physicality of the players and their performance',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis_title='Season', yaxis_title='Normalized Value',
            annotations=[
               dict(
                   x=0.5,
                   y=1.1,
                   xref='paper',
                   yref='paper',
                   text=f'Up to {selected_season} season for the selected teams',
                   showarrow=False,
                   font=dict(size=16)
               )
           ]
                           )
        fig = go.Figure(layout=layout)

        if show_line1:
            fig.add_trace(trace1)
        if show_line2:
            fig.add_trace(trace2)
        if show_line3:
            fig.add_trace(trace3)
        if show_line4:
            fig.add_trace(trace4)
        if show_line5:
            fig.add_trace(trace5)

        # Adding vertical lines
        if not selected_team:
            y1 = 0.13
        else:
            y1 = 0.5
        for year in range(1996, selected_season+1):
            fig.add_shape(
                type="line",
                x0=year,
                y0=-0.1,
                x1=year,
                y1=y1,
                line=dict(color="rgba(200, 200, 200, 0.5)", width=1),
            )

    st.plotly_chart(fig)

# Second plot - Map plot
st.markdown("#### **Map Visualization**")

# create slide bar
selected_season2 = create_slide_bar(2)

# create selector
select = st.radio('Select display:', (f'Until {selected_season2} season', f'Only {selected_season2} season'), horizontal=True)

if select == f'Until {selected_season2} season':
    filtered_data2 = data.loc[data['season'] <= selected_season2]

else:
    filtered_data2 = data.loc[data['season'] == selected_season2]


# # Create map plot
_, col, _, col2, _ = st.columns((0.1, 3.3, 0.1, 0.7, 0.1))
with col2:
    # for _ in range(10):
    #     st.write('')

    st.write('**Choose map display:**')
    usa = st.checkbox('USA', value=True)
    world = st.checkbox('Other World', value=True)

    if usa and world:
        filtered = filtered_data2.groupby('code').agg({
            'pts': 'mean',
            'reb': 'mean',
            'ast': 'mean',
            'player_height': 'mean',
            'player_weight': 'mean',
            'player_name': 'nunique'}).reset_index()
        filtered.rename(columns={'player_name': 'Players'}, inplace=True)

    elif usa:
        filtered = filtered_data2.loc[data['code'] == 'USA']
        filtered = filtered.groupby('code').agg({
            'pts': 'mean',
            'reb': 'mean',
            'ast': 'mean',
            'player_height': 'mean',
            'player_weight': 'mean',
            'player_name': 'nunique'}).reset_index()
        filtered.rename(columns={'player_name': 'Players'}, inplace=True)

    elif world:
        filtered = filtered_data2.loc[data['code'] != 'USA']
        filtered = filtered = filtered.groupby('code').agg({
            'pts': 'mean',
            'reb': 'mean',
            'ast': 'mean',
            'player_height': 'mean',
            'player_weight': 'mean',
            'player_name': 'nunique'}).reset_index()
        filtered.rename(columns={'player_name': 'Players'}, inplace=True)

with col:
    if (not usa and not world) or len(filtered) == 0:
        empty_geojson = {
            "type": "FeatureCollection",
            "features": []
        }
        # Create the figure with an empty choropleth trace
        fig = go.Figure(go.Choropleth(geojson=empty_geojson))

    else:
        filtered = pd.merge(filtered, data[['country', 'code']], on='code', how='left')
        fig = px.choropleth(filtered, locations='code', color='Players', hover_name='country',
                            hover_data=['pts', 'reb', 'ast', 'player_weight', 'player_height'],
                            color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

