import dash_core_components as dcc
import dash_html_components as html
import dash

# app settings
app = dash.Dash(__name__, update_title=None)
app.title = "Genshin Artifact Simulator"
server = app.server

# app layout
app.layout = html.Div(
    [
        html.Div([
            # Icon
            html.Div([
                html.Img(src=app.get_asset_url("resin_icon.png"),
                         id="resin-icon",
                         style={"height": "60px",
                                "width": "auto",
                                "margin-top": "25px"})
            ],
                className="one-third column"
            ),

            # Webpage Title
            html.Div([
                html.Div([
                    html.H3("GenAS v1.0", style={"margin-bottom": "0px"}),
                    html.H5("Genshin Artifact Simulator", style={"margin-top": "0px", "color": "dodgerblue"})])
            ],
                className="one-half column",
                id="title",
            ),

            # Learn More Button
            html.Div([
                html.A(
                    html.Button("Built by @trwstin", id="learn-more-button", className="button"),
                    href="https://www.github.com/trwstin")
            ],
                className="one-third column",
                id="button",
            )
        ],
            id="header",
            className="row flex-display"
        ),

        html.Div([
            html.Div([
                # Select Domain
                html.P("Select domain to farm:", className="control_label"),
                dcc.Dropdown(
                    id="domain_dropdown",
                    className="dcc_control",
                    options=[{"label": "Midsummer Courtyard",
                              "value": "Midsummer Courtyard"},
                             {"label": "Domain of Guyun", 
                              "value": "Domain of Guyun"},
                             {"label": "Valley of Remembrance",
                              "value": "Valley of Remembrance"},
                             {"label": "Hidden Palace of Zhou Formula",
                              "value": "Hidden Palace of Zhou Formula"},
                             {"label": "Clear Pool and Mountain Cavern",
                              "value": "Clear Pool and Mountain Cavern"},
                             {"label": "Peak of Vindagnyr",
                              "value": "Peak of Vindagnyr"},
                             {"label": "Ridge Watch",
                              "value": "Ridge Watch"},
                             {"label": "Slumbering Court",
                              "value": "Slumbering Court"},
                             {"label": "Momiji-Dyed Court",
                              "value": "Momiji-Dyed Court"},
                             {"label": "The Lost Valley",
                              "value": "The Lost Valley"},
                             {"label": "Spire of Solitary Enlightenment",
                              "value": "Spire of Solitary Enlightenment"},
                             {"label": "City of Gold",
                              "value": "City of Gold"}],
                    value='Midsummer Courtyard',
                    multi=False,
                    clearable=False),

                # Select Resin
                html.P("Select resin type:", className="control_label"),
                dcc.RadioItems(
                    id="resin_type",
                    options=[{'label': 'Original Resin', 'value': '20'},
                             {'label': 'Condensed Resin', 'value': '40'}],
                    value='20',
                    className="dcc_control"),

                # Farm Button
                html.Button("Farm", className="button", id="farm_button", n_clicks=0),
            ],
                id="cross-filter-options",
                className="pretty_container four columns",
            ),

            html.Div([
                html.Div([

                    # Domain Header
                    html.Div(
                        [html.H6(children=html.P("Domain:")),
                         html.P("domain", id="domain_header", style={"font-weight": "600"})],
                        id="domain",
                        className="mini_container"),

                    # Artifacts Header
                    html.Div(
                        [html.H6(children=html.P("Total Artifacts Farmed:")),
                         html.P(id="total_artifacts_header", style={"font-weight": "600"})],
                        id="total_artifacts",
                        className="mini_container"),

                    # Resin Header
                    html.Div(
                        [html.H6(children=html.P("Total Resin Used:")),
                         html.P(id="total_resin_header", style={"font-weight": "600"})],
                        id="total_resin",
                        className="mini_container")],
                    id="info-container",
                    className="row container-display"),

                # Artifact Box
                html.Div(id="artifact_container", className="pretty_container")
            ],
                id="right-column",
                className="eight columns"
            )
        ],
            className="row flex-display"
        ),

        # Inventory
        html.Details([
            html.Summary("Inventory", style={"margin-left": "10px", "margin-top": "10px"}),
            html.Div(id="inventory_box", className="pretty_container")
        ]),

        # Upgrade
        html.Details([
            html.Summary("Upgrade", style={"margin-left": "10px", "margin-top": "10px"}),
            html.Div([
                html.Div(
                    [html.P("Select which artifact to upgrade: "),
                     dcc.Dropdown(options=[], id="artifact_select"),
                     html.Button("Upgrade",
                                 style={"margin-top": "20px"},
                                 id="upgrade_button",
                                 className="button")]
                )],
                id="upgrade_box", className="pretty_container")
        ])
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"}
)
