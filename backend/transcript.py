from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(youtube_url: str) -> str:
    """Extracts the video ID from a YouTube URL."""
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", youtube_url)
    if not match:
        raise ValueError("Could not extract video ID from URL")
    return match.group(1)



def get_transcript(youtube_url: str, languages=None) -> str:
    video_id = get_video_id(youtube_url)
    if languages is None:
        languages = ["en", "hi"]
    
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id, languages=languages)
    
    full_text = " ".join(snippet.text for snippet in fetched_transcript)
    return full_text

