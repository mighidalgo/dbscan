from fastapi import APIRouter, HTTPException
from sklearn.cluster import DBSCAN
import numpy as np
import os
from datetime import datetime, timedelta
from app.templates.fetch_dataset import get_bb_data_set

dbscan_router = APIRouter()

# Preprocesar los datos
def preprocess_meraki_data():
    t1 = str(datetime.now())
    t0 = str(datetime.now() - timedelta(days=21))
    data = get_bb_data_set(t0[0:10] + "T23:59:59Z", t1[0:10] + "T00:00:00Z")
    #print(data)
    features = []
    for item in data:
        sent = item['wan1']['sent']
        received = item['wan1']['received']
        features.append([sent, received])
    return np.array(features)

@dbscan_router.get("/")
async def dbscan():
    try:
        # Guardar los datos prepocesados
        features = preprocess_meraki_data()
        """
        DBSCAN configuration:
            eps: The maximum distance between two samples for one to be considered as in the neighborhood of the other.
            min_samples: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. 
        """
        eps = float(os.getenv('EPS', 305400000)) # if not defined, default value is 305400000
        min_samples = int(os.getenv('MIN_SAMPLES', 4)) # if not defined, default value is 4

        dbscan = DBSCAN(eps=eps, min_samples=min_samples)

        # Fitting dbscan to the data
        dbscan.fit(features)

        labels = dbscan.labels_  # Clusters labels (-1 means noise)
        unique_labels = set(labels)

        # Estructurar la respuesta
        results = {
            "clusters": [
                {
                    "label": int(label),
                    "points": [
                        {
                            "sent": int(features[i][0]),
                            "received": int(features[i][1]),
                        }
                        for i in range(len(features))
                        if labels[i] == label
                    ],
                }
                for label in unique_labels
            ]
        }

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running DBSCAN: {str(e)}")