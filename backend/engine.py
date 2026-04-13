class StrategyEngine:
    @staticmethod
    def evaluate(user_action: str, scenario: dict, strategy: str) -> dict:
        # JSON側にある個別の解説を取得（なければ空文字）
        json_feedback = scenario.get("feedback", "")
        
        all_solutions = scenario.get("solutions")
        
        if not all_solutions:
            return {
                "status": "ERROR",
                "score": 0,
                "feedback": "Scenario data error: 'solutions' key not found.",
            }
        
        correct_action = all_solutions.get(strategy, all_solutions.get("GTO", "FOLD"))
        
        # 判定結果に応じた基本メッセージと、JSONの個別解説を組み合わせる
        if user_action == correct_action:
            return {
                "status": "GOOD",
                "score": 100,
                # JSONの解説がある場合は、基本メッセージの後ろに連結する
                "feedback": f"Excellent! {json_feedback}".strip(),
            }
        
        if user_action != "FOLD" and correct_action == "FOLD":
            return {
                "status": "NEUTRAL",
                "score": 50,
                "feedback": f"Not bad, but folding was better. {json_feedback}".strip(),
            }
        
        return {
            "status": "BAD",
            "score": 0,
            "feedback": f"Not optimal. The best action is {correct_action}. {json_feedback}".strip(),
        }