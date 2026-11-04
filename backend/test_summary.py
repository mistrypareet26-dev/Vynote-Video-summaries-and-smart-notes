from transcript import get_transcript
from summarizer import summarize_text

video_id = "K-RsltkN63w"
transcript = get_transcript(video_id)
summary = summarize_text(transcript)

print(summary)