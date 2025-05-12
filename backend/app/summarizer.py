from typing import List, Dict
import os

# Try to import OpenAI for advanced summarization
try:
    import openai
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = openai_api_key
except ImportError:
    openai = None
    openai_api_key = None


def summarize_events(events: List[Dict]) -> str:
    """Summarize a list of scraped events/news items using OpenAI if available, otherwise rule-based."""
    if not events:
        return "No new developments found."

    if openai and openai_api_key:
        # Use OpenAI API for summarization
        prompt = "Summarize the following competitor developments in a concise paragraph:\n"
        for event in events:
            if 'headline' in event:
                prompt += f"- {event['headline']}\n"
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=120,
                temperature=0.5
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"[OpenAI error: {e}]"

    # Fallback: simple rule-based summary
    summary_lines = []
    for event in events:
        if 'headline' in event:
            summary_lines.append(f"- {event['headline']}")
        elif 'error' in event:
            summary_lines.append(f"Error: {event['error']}")
    return '\n'.join(summary_lines)

# Example usage
if __name__ == "__main__":
    test_events = [
        {"headline": "Competitor A launches new AI product."},
        {"headline": "Competitor A appoints new CTO."}
    ]
    print(summarize_events(test_events))
