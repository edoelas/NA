from .helpers import *
import pandas as pd

# 🛖🏢🃏🚗
# 🥖🪨🧱🪵🧶

goal_strings = {
    "build_town": "🛖 (1🥖1🧱1🪵1🧶)",
    "build_city": "🏢 (2🥖3🪨)",
    "build_road": "🛣️ (1🧱1🪵)",
    "buy_card": "🃏 (1🥖1🧶1🪨)"
}

log_data = []

def material_to_string(materials):
    # 🪵🪨🧶🧱🥖
    if type(materials) == Materials:
        materials = material_to_list(materials)
    mls = [str(material).rjust(2) for material in materials]
    return f"{mls[0]}🥖 {mls[1]}🪨 {mls[2]}🧱 {mls[3]}🪵 {mls[4]}🧶"

def goals_to_string(goals, count = 5):
    substitutions = {"build_town": "TOWN", "build_city": "CITY", "build_road": "ROAD", "buy_card": "CARD"}
    goals = [substitutions[goal] for goal in goals]
    return ", ".join(goals[:count]) + (", ..." if len(goals) > count else "")
    
def log_turn(goals: List[str], materials: Materials, id: str):
    log_data.append({
        "id": id,
        "goals": goals.copy(),
        "materials": material_to_list(materials),
        "events": [],
        "offers": []
    })

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
                "materials": material_to_string(turn["materials"]),
                "goal_1": goal_strings[turn["goals"][0]] if turn["goals"][0] else "",
                "goal_2": goal_strings[turn["goals"][1]] if turn["goals"][1] else "",
                "goal_3": goal_strings[turn["goals"][2]] if turn["goals"][2] else "",
                "trade_1": material_to_string(turn["offers"][0][0]) + "=>" + material_to_string(turn["offers"][0][1]) if turn["offers"] else "",
                "trade_2": material_to_string(turn["offers"][1][0]) + "=>" + material_to_string(turn["offers"][1][1]) if len(turn["offers"]) > 1 else "",
                "trade_3": material_to_string(turn["offers"][2][0]) + "=>" + material_to_string(turn["offers"][2][1]) if len(turn["offers"]) > 2 else "",
                "events": turn["events"],
            }
        )
    return pd.DataFrame(df_data)