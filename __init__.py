import datetime
import logging
import azure.functions as func
import json
import time
from . import crawling

def main(mytimer: func.TimerRequest, tablePath: func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    tags = crawling.naver();
    data = {
        "temp": tags[0],
        "weather": tags[1],
        "weather2": tags[2],
        "lowset": tags[3],
        "highset": tags[4],
        "PartitionKey": "Weather_check",
        "RowKey": int(time.time()-999999999999)
    }

    tablePath.set(json.dumps(data))