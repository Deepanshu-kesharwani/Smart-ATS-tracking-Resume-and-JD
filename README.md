# Smart ATS - Resume & Job Description Tracker

An intelligent **Applicant Tracking System (ATS)** powered by AI that analyzes your resume against job descriptions and provides actionable insights to improve your chances of getting hired.

## Overview

Smart ATS is a Streamlit-based web application that uses advanced AI (powered by OpenRouter and GPT-4o-mini) to evaluate resumes against job descriptions. It provides:

- **JD Match Percentage**: See how well your resume aligns with the job description
- **Missing Keywords**: Identify critical skills and keywords you're missing
- **Profile Summary**: Get insights about your professional profile

This tool is perfect for job seekers wanting to tailor their resumes for specific positions and improve their ATS score.

## Features

✨ **Key Features**:
- 📄 PDF Resume Upload & Parsing
- 🔍 Job Description Analysis
- 🎯 ATS Match Score Calculation
- 🏷️ Missing Keywords Identification
- 📊 JSON-formatted Results
- 🚀 Fast AI-powered Evaluation
- 💡 Expert Recommendations for Resume Improvement

## Tech Stack

- **Python 3.x**
- **Streamlit** - Web UI Framework
- **OpenAI/OpenRouter API** - AI Model Integration
- **PyPDF2** - PDF Processing
- **python-dotenv** - Environment Variable Management

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.8+** installed
2. **OpenRouter API Key** (Get it from [openrouter.ai](https://openrouter.ai))
3. **pip** (Python package manager)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Deepanshu-kesharwani/Smart-ATS-tracking-Resume-and-JD.git
cd Smart-ATS-tracking-Resume-and-JD
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
SITE_URL=http://localhost
SITE_NAME=Smart ATS
```

**How to get your OpenRouter API Key:**
1. Visit [openrouter.ai](https://openrouter.ai)
2. Sign up or log in
3. Navigate to your API keys section
4. Create a new API key and copy it
5. Add it to your `.env` file

## Usage

### Run the Application

```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

### Using Smart ATS

1. **Paste Job Description**: Copy the job description and paste it into the text area
2. **Upload Resume**: Select and upload your resume in PDF format
3. **Click Submit**: Hit the "Submit" button to analyze
4. **View Results**: Get your ATS match percentage, missing keywords, and profile summary

### Example Output

```json
{
  "JD Match": "85%",
  "MissingKeywords": ["Machine Learning", "Docker", "Kubernetes"],
  "Profile Summary": "Strong software engineer with 5+ years of experience..."
}
```

## Project Structure

```
Smart-ATS-tracking-Resume-and-JD/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore file
└── README.md              
```

## How It Works

1. **Resume Parsing**: Extracts text from uploaded PDF files
2. **AI Analysis**: Sends resume and job description to OpenRouter API
3. **ATS Evaluation**: GPT-4o-mini evaluates the match and identifies gaps
4. **Results Formatting**: Returns structured JSON with:
   - Match percentage
   - Missing keywords
   - Profile assessment

## Configuration

### Changing the AI Model

To use a different OpenRouter model, edit `main.py` line 23:

```python
model="openai/gpt-4o-mini"   # Change to any OpenRouter model slug
```

Available models on OpenRouter: [openrouter.ai/docs](https://openrouter.ai/docs)

### Adjusting Temperature

Modify the `temperature` parameter in `main.py` to control response creativity:
- `0.2` (current): More focused, deterministic results
- `0.5-0.7`: Balanced
- `1.0+`: More creative/varied responses

## Troubleshooting

### API Key Issues
- ❌ `Invalid API Key`: Check your `.env` file has the correct `OPENROUTER_API_KEY`
- ❌ `Rate Limited`: Wait a moment and try again (free tier has limits)

### PDF Upload Issues
- ❌ `No file uploaded`: Make sure you select a PDF file before submitting
- ❌ `PDF parsing error`: Ensure the PDF is readable and not corrupted

### Running Issues
- ❌ `Streamlit not found`: Run `pip install -r requirements.txt` again
- ❌ `Port already in use`: Change port with `streamlit run main.py --server.port 8502`

## Tips for Best Results

1. **Format Your Resume Clearly**: Use standard fonts and proper formatting
2. **Use Keywords from JD**: Include relevant skills mentioned in the job description
3. **Keep It Updated**: Update your resume regularly with recent projects and skills
4. **Customize per Application**: Tailor your resume for each job application
5. **Review Missing Keywords**: Add relevant missing keywords if applicable to your experience

## Limitations

- Analyzes based on text content only (formatting not considered)
- AI evaluation is based on keyword matching and relevance
- Results are not a guarantee of hiring success
- Requires internet connection for API calls
- Subject to OpenRouter API rate limits

## Future Enhancements

- 🚀 Support for DOCX file format
- 📊 Historical comparison and analytics
- 🔄 Batch resume analysis
- 💾 Save and track applications
- 📱 Mobile app version
- 🌍 Multi-language support

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



## Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/Deepanshu-kesharwani/Smart-ATS-tracking-Resume-and-JD/issues)
- Contact the developer

## Author

**Deepanshu Kesharwani**  
GitHub: [@Deepanshu-kesharwani](https://github.com/Deepanshu-kesharwani)

---

⭐ If this project helped you, please consider giving it a star!

**Happy Applying! 🎯**
