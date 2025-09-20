# graph/plan_graph.py
from __future__ import annotations
from typing import TypedDict
from datetime import date

from langgraph.graph import StateGraph, END

from core.models import Task, DayPlan, DailySummary
from agents.parser import parse_task
from agents.classifier import classify_effort
from agents.scheduler import greedy_schedule
from agents.summarizer import summarize


class State(TypedDict, total=False):
    raw_text: str
    task: Task
    plan: DayPlan
    summary: DailySummary

def node_parse(state: State) -> State:
    """Raw text → Task"""
    # TODO: Get "raw_text" from the state, call the parse_task agent,
    # and update the state with the new "task".
    pass


def node_classify(state: State) -> State:
    """Task → (effort, confidence)"""
    # TODO: Get the "task" from the state, call the classify_effort agent,
    # and update the "task" in the state with the result.
    pass


def node_schedule(state: State) -> State:
    """Task(+effort) → DayPlan (today by default)"""
    # TODO: Get the "task" from the state, call the greedy_schedule agent,
    # and update the state with the new "plan".
    # HINT: You'll need to determine the target_day from the task's deadline.
    pass


def node_summary(state: State) -> State:
    """DayPlan → DailySummary (rule-based tips by default)"""
    # TODO: Get the "plan" from the state, call the summarize agent,
    # and update the state with the new "summary".
    pass


def build_graph():
    """
    Returns a compiled LangGraph app that runs:
        parse → classify → schedule → summary
    """
    # TODO: Create a StateGraph instance.
    g = None

    # TODO: Add the four nodes you just defined to the graph.
    pass

    # TODO: Set the entry point and add the edges to connect the nodes in sequence.
    pass

    # TODO: Compile and return the graph.
    pass


def run_once(raw_text: str) -> State:
    """
    Convenience wrapper used by app.py:
    input raw text → returns final state with task, plan, summary.
    """
    # TODO: Build the graph, invoke it with the initial state, and return the final state.
    # HINT: The initial state is {"raw_text": raw_text}
    pass

