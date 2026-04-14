class StrategyEngine:
    @staticmethod
    def evaluate(user_action: str, scenario: dict, strategy: str) -> dict:
        # JSON側にある個別の解説を取得（なければ空文字）
        json_feedback = scenario.get("feedback", "") 
        all_solutions = scenario.get("solutions") or scenario.get("solution")
        
        if not all_solutions:
            return {
                "status": "ERROR",
                "score": 0,
                "feedback": "Data error: 'Solution missing.",
            }

        # 選択された戦略（TAG/GTO/LAG）に応じた正解を取得
        # JSONに該当戦略がない場合はGTOをフォールバックに
        correct_action = all_solutions.get(strategy, all_solutions.get("GTO", "FOLD"))
        
        # 期待値(EV)ベースのスコアリング
        if user_action == correct_action:
            return {
                "status": "GOOD",
                "score": 100,
                # JSONの解説がある場合は、基本メッセージの後ろに連結する
                "feedback": f"Optimal! {json_feedback}".strip(),
            }

        # Foldすべきところでアクションした場合
        if user_action != "FOLD" and correct_action == "FOLD":
            return {
                "status": "NEUTRAL",
                "score": 50,
                "feedback": f"Fold was better. {json_feedback}".strip(),
            }
        
        return {
            "status": "BAD",
            "score": 0,
            "feedback": f"Incorrect. {strategy} choice is {correct_action}. {json_feedback}".strip(),
        }