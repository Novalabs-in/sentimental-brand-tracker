from transformers import pipeline

class BrandSentimentTracker:
    """
    Social Media Brand Mention Sentiment Tracker
    Integrates pre-trained transformers to detect negative PR and send alerts.
    """
    def __init__(self):
        # Initialize pipeline on CPU/GPU
        self.sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def track_mentions(self, text_list):
        findings = self.sentiment_pipeline(text_list)
        report = []
        for text, f in zip(text_list, findings):
            report.append({
                "text": text,
                "sentiment": f["label"],
                "score": f["score"]
            })
        return report

if __name__ == "__main__":
    tracker = BrandSentimentTracker()
    posts = [
        "Novalabs.in is absolutely amazing, outstanding work!",
        "The Excel plugin keeps freezing up under load, poor execution."
    ]
    print("Social Media Analysis:")
    for rep in tracker.track_mentions(posts):
        print(f"Post: {rep['text']} | Result: {rep['sentiment']} ({rep['score']:.2%})")
