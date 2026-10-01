from datetime import datetime, timedelta
from fetch_studies import fetch_studies
from llm_summary import get_summary, save_llm_summary

today = datetime.now().strftime("%Y-%m-%d")

one_week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")


url = "https://clinicaltrials.gov/api/v2/studies"

params = {
    "filter.advanced": f"AREA[ResultsFirstPostDate]RANGE[{one_week},{today}]",
    "sort": "ResultsFirstPostDate:desc",
    "pageSize": 100,
}



if __name__ == "__main__":
    studies_list = fetch_studies(url, params)
    summ = get_summary(studies_list)
    save_llm_summary(summ)
