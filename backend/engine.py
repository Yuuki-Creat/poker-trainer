class StrategyEngine:
    @staticmethod
    def evaluate(user_action: str, scenario: dict, strategy: str) -> dict:
        print(f"DEBUG: scenario keys: {list(scenario.keys())}")
        all_solutions = scenario.get("solutions")
        
        if not all_solutions:
            return {
                "status": "ERROR",
                "score": 0,
                "feedback": "Scenario data error: 'solutions' key not found.",
            }
        
        # 指定された戦略（TAG/GTO等）の正解を取得。なければGTO、それもなければFOLD
        correct_action = all_solutions.get(strategy, all_solutions.get("GTO", "FOLD"))
        
        # 判定ロジック
        if user_action == correct_action:
            return {
                "status": "GOOD",
                "score": 100,
                "feedback": "Excellent! Your action is optimal for this scenario.",
            }
        
        if user_action != "FOLD" and correct_action == "FOLD":
            return {
                "status": "NEUTRAL",
                "score": 50,
                "feedback": "Not bad, but folding would have been the best choice here.",
            }
        
        return {
            "status": "BAD",
            "score": 0,
            "feedback": f"Not optimal. The best action for {strategy} is {correct_action}.",
        }