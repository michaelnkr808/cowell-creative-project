# 🤖 AI Agent Implementation Guide

## What We Just Built

You now have a fully functional AI agent that can answer California tenant rights questions using Google's Gemini AI!

## 📁 New Files Created

### 1. `utils/langchain_setup.py`
This is the brain of your AI agent. It contains:

- **`get_llm()`** - Initializes the Gemini AI model
- **`create_tenant_rights_chain()`** - Creates a specialized AI chain for tenant rights
- **`ask_tenant_question()`** - The simple function that answers questions

### 2. `utils/__init__.py`
Makes the `utils` folder a Python package so we can import from it.

### 3. Updated `app.py`
Now uses the AI agent instead of echoing back messages.

## 🚀 How to Get This Running

### Step 1: Get Your Gemini API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key (looks like: `AIzaSy...`)

### Step 2: Create Your .env File

```bash
cd backend
echo "GOOGLE_API_KEY=paste_your_actual_key_here" > .env
```

**Replace** `paste_your_actual_key_here` with your real API key!

### Step 3: Install Dependencies

```bash
# Make sure you're in the backend directory
cd backend

# Install all Python packages
pip install -r requirements.txt
```

This will install:
- FastAPI (web server)
- Langchain (AI framework)
- Google Generative AI SDK (Gemini)
- And all other dependencies

### Step 4: Run the Backend

```bash
python app.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 5: Run the Frontend

In a NEW terminal:
```bash
# Go back to the main project directory
cd ..

# Start the React app
npm run dev
```

### Step 6: Test It!

1. Open browser: http://localhost:5173
2. Ask a question like: "What are my rights if my unit is unsafe?"
3. Watch the AI respond with real tenant rights information!

## 🧠 Understanding the Code Flow

### What Happens When You Ask a Question:

```
1. User types in React app
   ↓
2. Frontend sends POST to /chat
   ↓
3. app.py receives request
   ↓
4. Calls ask_tenant_question(message)
   ↓
5. Langchain formats prompt with system instructions
   ↓
6. Sends to Gemini AI
   ↓
7. Gemini generates response
   ↓
8. Returns to app.py
   ↓
9. app.py sends JSON response to frontend
   ↓
10. User sees the answer!
```

## 🎯 Key Concepts Explained

### What is a "Chain" in Langchain?

Think of it like an assembly line:

```python
chain = (
    prompt          # 1. Format the question with instructions
    | llm           # 2. Send to AI
    | parser        # 3. Format the response
)
```

Each step processes the data and passes it to the next step.

### What is `temperature`?

```python
temperature=0.3  # Lower = more focused and consistent
```

- **0.0** - Very deterministic, same answer every time
- **0.3** - Balanced (good for factual questions)
- **1.0** - Very creative, different answers each time

For legal information, we want **low temperature** (0.3) to be consistent and accurate.

### What is the System Prompt?

```python
("system", """You are a knowledgeable assistant...""")
```

This is the **instructions** we give the AI about how to behave. It's like hiring someone and telling them:
- What their role is
- How to respond
- What to prioritize

## 🔍 Troubleshooting

### Error: "GOOGLE_API_KEY not found"
- Make sure you created the `.env` file in the `backend/` directory
- Check that the API key is on a line like: `GOOGLE_API_KEY=your_key_here`
- No spaces around the `=` sign

### Error: "Module not found: utils"
- Make sure you created `utils/__init__.py`
- Make sure you're running from the `backend/` directory

### Error: "Invalid API key"
- Check that you copied the full API key
- Make sure there are no extra spaces
- Try generating a new key

### Server won't start
- Make sure port 8000 isn't already in use
- Check if you have Python 3.9+ installed: `python --version`

## 📊 Testing Different Questions

Try these questions to see how the AI responds:

1. **"What are my rights if my unit is unsafe?"**
   - Should explain habitability standards

2. **"How much notice does a landlord need to give before eviction?"**
   - Should discuss different notice periods

3. **"Can my landlord enter my apartment without permission?"**
   - Should explain entry rights and notice requirements

4. **"What can I do about a security deposit dispute?"**
   - Should explain deposit laws and dispute resolution

## 🎓 Next Steps

Right now, the AI uses its general knowledge about California tenant law. To make it even better, we can:

1. **Add RAG (Retrieval Augmented Generation)**
   - Load actual legal documents
   - Search documents for relevant sections
   - Give AI specific legal text to reference

2. **Add conversation history**
   - Remember previous messages in the chat
   - Allow follow-up questions

3. **Add citations**
   - Show which law or statute the answer comes from
   - Link to official resources

Want to implement any of these next?

## 💡 What You've Learned

- How to integrate AI APIs into a web application
- How Langchain creates "chains" of AI operations
- How to write effective prompts for AI
- How to handle API keys securely with environment variables
- The full stack flow from frontend → backend → AI → response

---

**You've now built a working AI chatbot! 🎉**

