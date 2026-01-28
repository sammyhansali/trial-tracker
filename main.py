import json

import requests


def main():
    API_SERVER = "https://clinicaltrials.gov/api/v2"
    ENDPOINT = f"{API_SERVER}/studies"
    PARAMS = {
        "query.cond": "hair loss",
        "pageSize": 10,
        "sort": "StudyFirstSubmitDate:desc",  # "LastUpdatePostDate:desc",
    }

    resp = requests.get(ENDPOINT, params=PARAMS)
    resp.raise_for_status
    # print(resp.json())
    with open("./test_data.json", "w") as f:
        json.dump(resp.json(), f)


if __name__ == "__main__":
    main()
