import numpy as np
from dash import Input, Output, callback
from functions import *
from layout import *


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
    if n_clicks > 0 and "farm_button" in changed_id:
        if resin_amt == str(20):
            current_amt = int(current_amt) + 1
        elif resin_amt == str(40):
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
