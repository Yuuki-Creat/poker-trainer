from poker_logic import PokerLogic
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
    @staticmethod
    def evaluate(user_action: str, scenario: dict, strategy: str, current_hand: list) -> dict:
        # JSON内の solutions キーを取得
        all_solutions = scenario.get("solutions")
        
        if not all_solutions:
            return {"status": "ERROR", "score": 0, "feedback": "判定データが見つかりません。"}

        # TAG戦略かつプリフロップの場合は、poker_logicのレンジ判定を優先させることも可能
        # 今回はシンプルに、戦略に応じた正解を取得
        correct_action = all_solutions.get(strategy)
        
        if not correct_action:
            correct_action = all_solutions.get("GTO", "FOLD")

        # ユーザーのアクションと比較
        is_correct = user_action.upper() == correct_action.upper()
        
        # ボードがある場合はフィードバックにボード情報を加えるなどの処理も可能
        phase = scenario.get("phase", "Unknown")
        
        if is_correct:
            return {
                "status": "GOOD",
                "score": 100,
                "feedback": f"正解です！{phase}での{strategy}戦略は {correct_action} です。"
            }
        else:
            return {
                "status": "BAD",
                "score": 0,
                "feedback": f"ミスです。{phase}の{strategy}正解は {correct_action} でした。"
            }
