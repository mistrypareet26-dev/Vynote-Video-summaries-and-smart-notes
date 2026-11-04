import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def chunk_text(text: str, max_chars: int = 6000) -> list[str]:
    """Splits text into chunks of roughly max_chars characters."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_length += len(word) + 1
        if current_length > max_chars:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            current_chunk.append(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_chunk(chunk: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": f"Summarize this part of a video transcript into concise bullet points:\n\n{chunk}"
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

def summarize_text(transcript: str) -> str:
    """Handles long transcripts by chunking, summarizing each piece, then combining."""
    chunks = chunk_text(transcript)

    if len(chunks) == 1:
        return summarize_chunk(chunks[0])

    # Summarize each chunk
    chunk_summaries = [summarize_chunk(chunk) for chunk in chunks]

    # Combine chunk summaries into one final summary
    combined = "\n\n".join(chunk_summaries)
    final_response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": (
                    "Combine these partial summaries of a video into one clear, "
                    "well-organized summary with bullet points:\n\n"
                    f"{combined}"
                )
            }
        ],
        max_tokens=1000,
    )
    return final_response.choices[0].message.content

if __name__ == "__main__":
    sample_text = "This is a test transcript about how loops work in programming."
    print(summarize_text(sample_text))