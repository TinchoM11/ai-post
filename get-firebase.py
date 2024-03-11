from fire import db


def get_transaction():
    print("HOLA1")
    collection_ref = db.collection("transactions")

 # Get Document with id 0nJMeLgRh9xCHnxXJISh
    doc_ref = collection_ref.document("0nJMeLgRh9xCHnxXJISh")

    try:
        doc = doc_ref.get()
        print("Document data: ", doc.to_dict())

        if doc.exists:
            return doc.to_dict()
        else:
            return "Transaction not found"
    except Exception as e:
        print("Error:", e)
        return "Error occurred while retrieving transaction data"


# Mostrar la transaccion
print(get_transaction())
