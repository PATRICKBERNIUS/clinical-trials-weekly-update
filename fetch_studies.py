import requests
from datetime import datetime, timedelta



today = datetime.now().strftime("%Y-%m-%d")

one_week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")


url = "https://clinicaltrials.gov/api/v2/studies"

params = {
    "filter.advanced": f"AREA[ResultsFirstPostDate]RANGE[{one_week},{today}]",
    "sort": "ResultsFirstPostDate:desc",
    "pageSize": 100,
}

def fetch_studies(url, params):

    studies = []


    response = requests.get(url, params=params)

    if response.status_code != 200:
            raise RuntimeError(f"ClincialTrials.gov returned {r.status_code}: {r.text}")

    
    data = response.json()


    if "errors" in data:
        raise RuntimeError(data["errors"])



    for study in data['studies']:
        nct_id = study['protocolSection']['identificationModule']['nctId']
        title = study['protocolSection']['identificationModule']['briefTitle']
        summary = study['protocolSection']['descriptionModule']['briefSummary']
        results_date = study['protocolSection']['statusModule'].get('resultsFirstPostDateStruct', {}).get('date', 'N/A')
        #print(f"{results_date} \n{nct_id}: {title} \n{summary}\n")
        study_content = f"{results_date} \n{nct_id}: {title} \n{summary}\n"

        studies.append(study_content)



    

    return studies

