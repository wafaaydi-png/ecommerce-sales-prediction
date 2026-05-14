from flask import Flask, render_template, request
import pandas as pd
import joblib
import xgboost as xgb

print("Pandas version :", pd.__version__)
print("XGBoost OK")

app = Flask(__name__)

# Charger modèle
model = joblib.load("models/sales_xgboost.pkl")
model_columns = joblib.load("models/model_columns.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        # Récupération des données formulaire
        quantity = float(request.form["quantity"])
        weight = float(request.form["weight"])
        unit_price = float(request.form["unit_price"])   # ajouté
        category = request.form["category"]
        region = request.form["region"]

        # Créer DataFrame
        new_data = pd.DataFrame({
            "Quantity": [quantity],
            "Weight": [weight],
            "Unit Price": [unit_price],   # ajouté
            "Category": [category],
            "Region": [region]
        })

        # Encoder variables catégorielles
        new_data_encoded = pd.get_dummies(new_data)

        # Aligner avec les colonnes du modèle
        new_data_encoded = new_data_encoded.reindex(
            columns=model_columns,
            fill_value=0
        )

        # Prédiction
        prediction = round(model.predict(new_data_encoded)[0], 2)

    return render_template(
        "indexSales.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)