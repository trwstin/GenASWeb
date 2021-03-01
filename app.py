import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from functions import *


# Create app layout
app.layout = html.Div(
    [
        html.Div(
            [
                # Icon
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("resin_icon.png"),
                            id="resin-icon",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-top": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                # Webpage Title
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "GenAS v1.0",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Genshin Artifact Simulator", style={"margin-top": "0px",
                                                                         "color": "dodgerblue"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                # Learn More Button
                html.Div(
                    [
                        html.A(
                            html.Button("Built by @trwstin", id="learn-more-button",
                                        className="button"),
                            href="https://www.github.com/trwstin",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.P("Select domain to farm:", className="control_label"),
                        dcc.Dropdown(
                            id="domain_dropdown",
                            className="dcc_control",
                            options=[
                                {"label": "Midsummer Courtyard", "value": "Midsummer Courtyard"},
                                {"label": "Domain of Guyun", "value": "Domain of Guyun"},
                                {"label": "Valley of Remembrance", "value": "Valley of Remembrance"},
                                {"label": "Hidden Palace of Zhou Formula", "value": "Hidden Palace of Zhou Formula"},
                                {"label": "Clear Pool and Mountain Cavern", "value": "Clear Pool and Mountain Cavern"},
                                {"label": "Peak of Vindagnyr", "value": "Peak of Vindagnyr"},
                            ],
                            value='Midsummer Courtyard',
                            multi=False,
                            clearable=False,
                        ),

                        html.P("Select resin type:", className="control_label"),
                        dcc.RadioItems(
                            id="resin_type",
                            options=[
                                {'label': 'Original Resin', 'value': '20'},
                                {'label': 'Condensed Resin', 'value': '40'}
                            ],
                            value='20',
                            className="dcc_control",
                        ),

                        html.Button("Farm", className="button", id="farm_button", n_clicks=0),

                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(children=html.P("Domain:")),
                                     html.P("domain", id="domain_header",
                                            style={"font-weight": "600"})],
                                    id="domain",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(children=html.P("Total Artifacts Farmed:")),
                                     html.P(id="total_artifacts_header",
                                            style={"font-weight": "600"})],
                                    id="total_artifacts",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(children=html.P("Total Resin Used:")),
                                     html.P(id="total_resin_header",
                                            style={"font-weight": "600"})],
                                    id="total_resin",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            id="artifact_container",
                            className="pretty_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),

        # Inventory

        html.Details([
            html.Summary("Inventory",
                         style={"margin-left": "10px",
                                "margin-top": "10px"}),
            html.Div(id="inventory_box", className="pretty_container")
        ]),

        html.Details([
            html.Summary("Upgrade",
                         style={"margin-left": "10px",
                                "margin-top": "10px"}),
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Select which artifact to upgrade: "),
                            dcc.Dropdown(
                                options=[],
                                id="artifact_select"),
                            html.Button("Upgrade",
                                        style={"margin-top": "20px"},
                                        id="upgrade_button",
                                        className="button"),
                        ]
                    ),
                ],
                id="upgrade_box", className="pretty_container"),
        ])

    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)


# Callbacks

# Shows the selected domain
@app.callback(
    Output("domain_header", "children"),
    Input("domain_dropdown", "value")
)
def display_domain(selected_domain):
    return selected_domain


# Button to farm artifacts
@app.callback(
    Output("artifact_container", "children"),
    [Input("farm_button", "n_clicks"),
     Input("domain_dropdown", "value"),
     Input("resin_type", "value")]
)
def farm_artifact(n_clicks, domain, resin_amt):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if n_clicks > 0 and "farm_button" in changed_id:
        if resin_amt == str(20):
            artifact = [artifact_gen(domain)]
            return html.Ul([html.Li(x) for x in artifact])
        elif resin_amt == str(40):
            artifact1 = [artifact_gen(domain)]
            artifact2 = [artifact_gen(domain)]
            artifact_list = np.array([artifact1, artifact2])
            return html.Ul([html.Li(x) for x in artifact_list])
    return "Select a domain and click 'Farm' to begin!"


# Updates the total artifacts farmed
@app.callback(
    Output("total_artifacts_header", "children"),
    [Input("farm_button", "n_clicks"),
     Input("resin_type", "value"),
     Input("total_artifacts_header", "children")]
)
def resin_counter(n_clicks, resin_amt, current_amt):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if current_amt is None:
        current_amt = 0
    if n_clicks > 0 and "farm_button" in changed_id and resin_amt == str(20):
        current_amt = int(current_amt) + 1
    elif n_clicks > 0 and "farm_button" in changed_id and resin_amt == str(40):
        current_amt = int(current_amt) + 2
    return str(current_amt)


# Updates the total resin used
@app.callback(
    Output("total_resin_header", "children"),
    [Input("farm_button", "n_clicks"),
     Input("resin_type", "value"),
     Input("total_resin_header", "children")]
)
def resin_counter(n_clicks, resin_amt, current_amt):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if current_amt is None:
        current_amt = 0
    if n_clicks > 0 and "farm_button" in changed_id:
        current_amt = int(current_amt) + int(resin_amt)
    return str(current_amt)


# Updates the inventory box with farmed artifacts
@app.callback(
    [Output("inventory_box", "children"),
     Output("artifact_select", "options")],
    [Input("farm_button", "n_clicks"),
     Input("upgrade_button", "n_clicks"),
     Input("artifact_select", "value")]
)
def update_inventory(n_clicks_farm, n_clicks_upgrade, selected_artifact):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if n_clicks_farm == 0 or n_clicks_farm is None:
        return "Your inventory is empty!", []

    elif n_clicks_farm > 0 and "farm_button" in changed_id:
        inventory_list = np.array([str(x) for x in inventory.values()])
        return html.Ol([html.Li(x) for x in inventory_list]), \
               [{"label": item, "value": item} for item in inventory_list]

    elif n_clicks_upgrade > 0 and "upgrade_button" in changed_id:
        for key, value in inventory.items():
            if str(selected_artifact) == str(value):
                artifact = inventory.get(str(key))
                artifact.enhance()
                inventory[str(key)] = artifact
        inventory_list = np.array([str(x) for x in inventory.values()])
        return html.Ol([html.Li(x) for x in inventory_list]), \
               [{"label": item, "value": item} for item in inventory_list]


# Main
if __name__ == "__main__":
    app.run_server(debug=False)
