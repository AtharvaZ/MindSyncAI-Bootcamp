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
    task = parse_task(state['raw_text'])
    state['task'] = task
    return state


def node_classify(state: State) -> State:
    """Task → (effort, confidence)"""
    # TODO: Get the "task" from the state, call the classify_effort agent,
    # and update the "task" in the state with the result.
    state['task'] = classify_effort(state['task'])
    return state


def node_schedule(state: State) -> State:
    """Task(+effort) → DayPlan (today by default)"""
    # TODO: Get the "task" from the state, call the greedy_schedule agent,
    # and update the state with the new "plan".
    # HINT: You'll need to determine the target_day from the task's deadline.
    task  = state['task']
    target_day = task.deadline.date() if task.deadline else date.today()
    state['plan'] = greedy_schedule([task], target_day)
    return state


def node_summary(state: State) -> State:
    """DayPlan → DailySummary (rule-based tips by default)"""
    # TODO: Get the "plan" from the state, call the summarize agent,
    # and update the state with the new "summary".
    state['summary'] = summarize(state['plan'], completed_titles=[])
    return state


def build_graph():
    """
    Returns a compiled LangGraph app that runs:
        parse → classify → schedule → summary
    """
    # TODO: Create a StateGraph instance.
    g = StateGraph(State)


    # TODO: Add the four nodes you just defined to the graph.
    g.add_node("parse",node_parse)
    g.add_node("classify", node_classify)
    g.add_node("schedule", node_schedule)
    g.add_node("summary", node_summary) 

    # TODO: Set the entry point and add the edges to connect the nodes in sequence.
    g.set_entry_point("parse")
    g.add_edge("parse","classify")
    g.add_edge("classify","schedule")
    g.add_edge("schedule","summary")
    g.add_edge("summary",END)


    # TODO: Compile and return the graph.
    return g.compile()


def run_once(raw_text: str) -> State:
    """
    Convenience wrapper used by app.py:
    input raw text → returns final state with task, plan, summary.
    """
    # TODO: Build the graph, invoke it with the initial state, and return the final state.
    # HINT: The initial state is {"raw_text": raw_text}
    app = build_graph()
    state: State = app.invoke({"raw_text": raw_text})
    return state
    pass

