from Classifier import Classifier
from Database import Database
from data import initDataInDB, SplitSQLiteData
from fastapi import FastAPI
import uvicorn

db = Database()
classifier = Classifier()
app = FastAPI()
# train the model from the CSV
X, Y = initDataInDB(db)
classifier.train(X,Y)

try:
    @app.post("/predict")
    async def predict(msg):
        try:
            response, proba = classifier.predict(msg)
            return { "category": response, "proba": proba, "msg": msg, "error": "" }
        except Exception as err:
            print(err)
            return { "error": str(err) }

    uvicorn.run(app, host="127.0.0.1", port=1337)

except KeyboardInterrupt as e:
    db.connection.close()
    classifier.safe()
    print("Programm stoped")
except Exception as err:
    db.connection.close()
    print(err)