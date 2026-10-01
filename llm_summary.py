from anthropic import Anthropic
import os


anthropic_api = os.getenv("CLAUDE_API")
client = Anthropic(api_key=anthropic_api)



def get_summary(trials_list):


    prompt = f"""You are writing a weekly science briefing for one reader who wants to stay current on interesting developments across medicine and clinical research, without reading every study themselves.

    Below is a list of clinical trials with results or updates posted in the last week. Not all of them are noteworthy — many are routine safety/dosing studies, early-phase trials, or narrow procedural comparisons. Your job is to select only the findings that are genuinely interesting, significant, or novel, and ignore the rest.

    Organize your briefing into a few natural categories based on what you actually find interesting this week (for example: oncology, metabolic/diabetes, neurological, infectious disease, mental health, medical devices — but only include categories that have something worth mentioning). For each category, write a short paragraph (2-4 sentences) covering the most noteworthy trial(s) in that space, explaining what was studied and why it matters in plain language.

    Use a natural, spoken tone, as if reading this aloud to someone curious about science but without a medical background. Do not use markdown formatting, bullet points, or headers with # symbols — use plain paragraph text with a category name in a short title line before each paragraph. If nothing this week is genuinely interesting, it's fine to say so briefly rather than forcing significance onto routine studies.

    This week's clinical trials:
    {trials_list}

    Briefing:"""


    try:

        message = client.messages.create(
                    model = "claude-sonnet-5",
                    max_tokens=10000,
                    messages = [
                        {"role": "user", "content": prompt}
                    ]
                )


        full_summary = next(i.text for i in message.content if i.type == "text")
        return full_summary
    except Exception as e:
        print(f"Warning: LLM summary failed: {e}")
        return "No summmary today"






def save_llm_summary(summary, output_dir ="site"):

    file_name = "summary.txt"


    os.makedirs(output_dir, exist_ok=True)

    p = os.path.join(output_dir, file_name)


    with open(p, "w", encoding="utf-8") as f:
        f.write(summary)

    return p



def load_summary(path="site/summary.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()