class StrategyEngine:
    @staticmethod
    def evaluate(user_action: str, scenario: dict, strategy: str) -> dict:
        correct_action = scenario["solution"].get(strategy, scenario["solution"]["GTO"])
        
        if user_action == correct_action:
            return {
                "status": "GOOD",
                "score": 100,
                "feedback": "Excellent! Your action is optimal for this scenario.",
            }
        
        if user_action != "FOLD" and correct_action == "FOLD":
            return {
                "status": "NUTLRAL",
                "score": 50,
                "feedback": "Not bad, but folding would have been the best choice in this situation.",
            }
        
        return {
            "status": "BAD",
            "score": 0,
            "feedback": f"Your action is not optimal. The best action for this scenario is {strategy} {correct_action}.",
        }