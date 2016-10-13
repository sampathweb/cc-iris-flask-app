import logging
import requests

from .config import IRIS_API_SERICE_URL

logger = logging.getLogger('app')


def query_iris_api(sepal_length, sepal_width, petal_length, petal_width):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    resp = requests.post(IRIS_API_SERICE_URL, json=payload)
    if resp.status_code == 200:
        results = resp.json()
        # Results come as Array of predictions.  Return the first item in the array
        data = results.get("data")
        if data:
            return data[0]  # First Predicted Result
    else:
        logger.error("Call to Prediction API Failed with error {}".format(resp.text))
