from .poker_logic import PokerLogic
class StrategyEngine:
    @staticmethod
    # def evaluate(user_action: str, scenario: dict, strategy: str) -> dict:
    #     all_solutions = scenario.get("solutions") or scenario.get("solution")
        
    #     if not all_solutions:
    #         return {
    #             "status": "ERROR",
    #             "score": 0,
    #             "feedback": "Data error: 'Solution missing.",
    #         }

    #     # フロントから届いた strategy (TAG/GTO等) をキーにして正解を取得
    #     # もし指定された戦略がデータになければ GTO を、それもなければ FOLD をデフォルトに
    #     correct_action = all_solutions.get(strategy)

    #     if not correct_action:
    #         correct_action = all_solutions.get("GTO", "FOLD")

    #     is_correct = user_action.upper() == correct_action.upper()

    #     if is_correct:
    #         return {
    #             "status": "GOOD",
    #             "score": 100,
    #             "feedback": f"正解です！{strategy}戦略では {correct_action} が推奨されます。"
    #         }
    #     else:
    #         return {
    #             "status": "BAD",
    #             "score": 0,
    #             "feedback": f"ミスです。{strategy}戦略での正解は {correct_action} でした。"
    #         }
    def evaluate(user_action: str, scenario: dict, strategy: str, current_hand: list) -> dict:
        if strategy == 'TAG' and scenario.get('phase') == 'Pre-flop':
            correct_action = PokerLogic.is_in_range(current_hand, scenario['position'], 'TAG')
        else:
            solutions = scenario.get("solutions, {}")
            correct_action = solutions.get(strategy, solutions.get("GTO", "FOLD"))
        
        json_feedback = scenario.get("feedback", "")
        
        if user_action == correct_action:
            return {
                "status": "GOOD",
                "score": 100,
                "feedback": f"Optimal! {json_feedback}"
            }
        
        return {
            "status": "BAD",
            "score": 0,
            "feedback": f"Not optimal. The best action was {correct_action}. {json_feedback}"
        }
