from crewai.tools import BaseTool
from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeTranscriptTool(BaseTool):
    name: str = "YouTube Transcript Tool"
    description: str = "Search YouTube and fetch transcript."

    def _run(self, topic: str):
        search = VideosSearch(topic, limit=5)
        result = search.result()

        if len(result["result"]) == 0:
            return "No video found."

        video_id = result["result"][0]["id"]

        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)

        text = ""

        for line in transcript:
            text += line.text + " "

        return text


yt_tool = YouTubeTranscriptTool()