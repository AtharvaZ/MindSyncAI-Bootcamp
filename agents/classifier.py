# agents/classifier.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from core.models import Task
from core.config import MODEL
import os

_GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

_CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages([
    ])

_llm = ChatGoogleGenerativeAI(
    #put model specifications here
)

def classify_effort(task: Task) -> Task:
    # --- Step 1: Get the initial classification from the LLM (Provided) ---
    out = _llm.invoke(
        _CLASSIFIER_PROMPT.format_messages(
            title=task.title,
            notes=task.notes or ""
        )
    )
    text = (out.content or "").lower()

    # --- Step 2: Parse the LLM's output (Provided) ---
    effort, conf = "medium", 0.6
    if "high" in text:
        effort, conf = "high", 0.8
    elif "low" in text:
        effort, conf = "low", 0.7
    elif "medium" in text:
        effort, conf = "medium", 0.7

    # --- Step 3: Refine with rule-based keywords (Audience codes this) ---
    
    # TODO: Check if any high-effort keywords are in the task's title or notes.
    # If so, set the effort to "high".
    # HINT: Use the `any()` function with a list comprehension.
    hi_kw = ["report", "analysis", "prototype", "research", "design", "study"]
    pass # Add your high-effort keyword check here.


    # TODO: Check for low-effort keywords.
    # If found (and the task isn't already high-effort), set the effort to "low".
    lo_kw = ["email", "call", "text", "schedule", "calendar", "meeting"]
    pass # Add your low-effort keyword check here.


    task.effort, task.confidence = effort, conf
    return task