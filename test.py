from joblib import load
import pandas as pd

def predict(
    month: int = 3,
    nombre_lots: int = 1,
    code_type_local: int = 2,
    nombre_pieces_principales: int = 3,
    surface: float = 75
) -> float:
    
    model = load('pipe.joblib')

    df = pd.DataFrame(
            {
                "month": [month],
                "Nombre_de_lots": [nombre_lots],
                "Code_type_local": [code_type_local],
                "Nombre_pieces_principales": [nombre_pieces_principales],
                "surface": [surface]
            }
        )

    prediction = model.predict(df)
    print(prediction)

    return prediction
