from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi

# Search video
search = VideosSearch("OpenAI DevDay Keynote", limit=1)
result = search.result()

video = result["result"][0]

print("Title:", video["title"])
print("Video ID:", video["id"])
print("URL:", video["link"])

video_id = video["id"]

try:
    # Create API object
    ytt_api = YouTubeTranscriptApi()

    # Fetch transcript
    transcript = ytt_api.fetch(video_id)

    print("\nFirst 10 transcript lines:\n")
    for line in transcript[:10]:
        print(line)

except Exception as e:
    print("\nError:", e)