from .helpers import *
import pandas as pd
from typing import List, Tuple

# 🛖🏢🃏🚗
# 🥖🪨🧱🪵🧶

log_data = []

def material_to_string(materials, show_all = True):
    # 🪵🪨🧶🧱🥖
    material_icons = ["🥖", "🪨", "🧱", "🪵", "🧶"]
    if materials == None: return ""

    if type(materials) == Materials:
        materials = material_to_list(materials)

    material_tuples = list(zip(materials, material_icons))
    mls = [str(t[0]).rjust(2)+t[1] for t in material_tuples if show_all or t[0] > 0]
    return " ".join(mls)

def trade_to_string(trade: Tuple[List[int],List[int]]):
    if trade == None or not trade[0] or not trade[1]: return ""
    offer = material_to_string(trade[0], False)
    request = material_to_string(trade[1], False)
    return f"[{offer}]\n[{request}]"

def goal_to_string(goal):
    if goal == None: return ""
    goal_strings = {
        "build_town": "🛖 (1🥖1🧱1🪵1🧶)",
        "build_city": "🏢 (2🥖3🪨)",
        "build_road": "🛣️ (1🧱1🪵)",
        "buy_card": "🃏 (1🥖1🧶1🪨)"
    }
    return goal_strings[goal]

def goals_to_string(goals, count = 5):
    if goals == None: return ""
    substitutions = {"build_town": "TOWN", "build_city": "CITY", "build_road": "ROAD", "buy_card": "CARD"}
    goals = [substitutions[goal] for goal in goals]
    return ", ".join(goals[:count]) + (", ..." if len(goals) > count else "")
    
def start_log(id: str):
    log_data.append({
        "id": id,
        "goals": None,
        "materials": None,
        "events": [],
        "offers": []
    })

def log_goal(goals: List[str]):
    log_data[-1]["goals"] = goals.copy()

def log_materials(materials: Materials):
    log_data[-1]["materials"] = material_to_list(materials)

def log_event(msg: str):
    log_data[-1]["events"].append(msg)

def log_offer(gives: Materials, receives: Materials):
    log_data[-1]["offers"].append((material_to_list(gives), material_to_list(receives)))


def clear_log_data():
    global log_data
    log_data = []

def get_log_data():
    return log_data

def get_log_df():
    df_data = []
    for turn in log_data:
        df_data.append(
            {
                "id": turn["id"],
                "materials": material_to_string(turn["materials"], False),
                "goal_1": goal_to_string(getl(turn["goals"],0)),
                "goal_2": goal_to_string(getl(turn["goals"],1)),
                "goal_3": goal_to_string(getl(turn["goals"],2)),
                "trade_1": trade_to_string(getl(turn["offers"],0)),
                "trade_2": trade_to_string(getl(turn["offers"],1)),
                "trade_3": trade_to_string(getl(turn["offers"],2)),
                "events": turn["events"],
            }
        )
    df = pd.DataFrame(df_data)
    return df

