# 🎥 YouTube AI Blog Generator

An AI-powered application that transforms YouTube video transcripts into structured, detailed blog posts using CrewAI and OpenAI.

## ✨ Features

* 🔍 **YouTube Search:** Find videos relevant to a given topic.
* 📝 **Transcript Extraction:** Retrieve video transcripts when available.
* 🤖 **AI-Powered Research:** Use a research agent to summarize important concepts.
* ✍️ **Automated Blog Writing:** Generate detailed Markdown blogs with headings, examples, conclusions, and key takeaways.
* 🌐 **Interactive Interface:** Generate blogs through a simple Streamlit application.
* 📥 **Download Blogs:** Download generated content as Markdown files.

## 🛠️ Tech Stack

| Technology             | Purpose                         |
| ---------------------- | ------------------------------- |
| Python                 | Core programming language       |
| CrewAI                 | Multi-agent orchestration       |
| OpenAI GPT-4o mini     | AI-powered research and writing |
| Streamlit              | Web interface                   |
| youtube-search-python  | YouTube video search            |
| youtube-transcript-api | Transcript retrieval            |
| python-dotenv          | Environment variable management |

## ⚙️ How It Works

1. Enter a topic in the Streamlit application.
2. The researcher agent searches YouTube for a relevant video.
3. The application retrieves the selected video's transcript.
4. The researcher agent prepares notes from the transcript.
5. The writer agent converts the research into a structured blog.
6. The generated blog appears in the application and can be downloaded.

### Workflow Architecture

```text
           User Input
               |
               v
         Streamlit App
             app.py
               |
               v
        CrewAI Workflow
            crew.py
               |
        +------+------+
        |             |
        v             v
   Researcher       Writer
     Agent           Agent
        |             |
        v             v
  YouTube Search   Blog Generation
  & Transcript          |
        |                |
        +-------+--------+
                |
                v
        Generated Markdown
                |
                v
        View and Download
```

## 📁 Project Structure

```text
youtube-ai-blog-generator/
│
├── app.py              # Streamlit application
├── agents.py           # Researcher and writer agents
├── crew.py             # CrewAI workflow configuration
├── tasks.py            # Research and writing tasks
├── tools.py            # YouTube search and transcript tool
├── test.py             # YouTube transcript testing
├── requirements.txt    # Project dependencies
├── new-blog.md         # Blog output file
└── README.md           # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/7471ashish/youtube-ai-blog-generator.git
cd youtube-ai-blog-generator
```

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the OpenAI API Key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your actual API key.

**Security:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📖 Usage

1. Launch the application.
2. Enter a topic, such as `LangChain tutorial` or `OpenAI DevDay keynote`.
3. Click **Generate Blog**.
4. Wait for the research and writing agents to finish.
5. Read the generated blog in the application.
6. Click **Download Blog** to save the Markdown file.

The current implementation selects the first video returned by YouTube search. Results depend on transcript availability and accessibility.

## 🔑 Environment Variables

| Variable         | Description                                 |
| ---------------- | ------------------------------------------- |
| `OPENAI_API_KEY` | API key used by the configured OpenAI model |

## ⚠️ Troubleshooting

**1. OpenAI API errors**

* Verify that your API key is valid.
* Ensure `.env` is in the project root.
* Check your API account's usage limits and billing status.

**2. Transcript retrieval errors**

* The selected video may not have an accessible transcript.
* Try a different topic or video.

**3. Dependency errors**

* Activate your virtual environment.
* Reinstall the dependencies from `requirements.txt`.
* If compatibility issues persist, check the installed package versions.

**4. Unexpected AI-generated content**

* Review the generated blog before publishing.
* Verify technical details and important claims against the original video.

**Note:** OpenAI API usage may incur charges.

## 🔮 Future Improvements

* Allow users to select from multiple YouTube search results.
* Support direct YouTube video URLs.
* Display video titles, links, and channel information.
* Add blog length, tone, and audience controls.
* Improve transcript error handling.
* Support multiple transcript languages.
* Add automated tests for the complete workflow.

## 🤝 Contributing

Contributions and suggestions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Submit a pull request.

## 👨‍💻 Author

**Ashish Bansal**

* GitHub: [@7471ashish](https://github.com/7471ashish)
* Project: [YouTube AI Blog Generator](https://github.com/7471ashish/youtube-ai-blog-generator)

---

⭐ If you find this project useful, consider starring the repository!
