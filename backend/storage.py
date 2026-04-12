from typing import Dict, List
import httpx
import json
import os

class GistStorage:
    def __init__(self):
        # RenderのEnvironment Variablesから読み込み
        self.token = os.getenv("GITHUB_TOKEN")
        self.gist_id = os.getenv("GIST_ID")
        self.file_name = os.getenv("FILE_NAME", "scenarios.json")
        self._cache: List[Dict] = []

    async def reload_scenarios(self):
        """API経由でセキュアにデータを取得"""
        if not self.token or not self.gist_id:
            # ここで None の場合に早期リターンせず例外を出すことでデバッグしやすくします
            raise ValueError(f"Missing Env Vars: TOKEN={'Set' if self.token else 'None'}, ID={'Set' if self.gist_id else 'None'}")

        api_url = f"https://api.github.com/gists/{self.gist_id}"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(api_url, headers=headers)
            
            if response.status_code == 200:
                gist_data = response.json()
                files = gist_data.get("files", {})
                
                if self.file_name in files:
                    content_str = files[self.file_name].get("content")
                    self._cache = json.loads(content_str)
                    print(f"Success: Loaded {len(self._cache)} hands.")
                else:
                    raise Exception(f"File {self.file_name} not found in Gist.")
            else:
                raise Exception(f"GitHub API Error: {response.status_code}")

    def get_all(self) -> List[Dict]:
        return self._cache

    def get_by_id(self, scenario_id: int) -> Dict:
        return next((s for s in self._cache if s["id"] == scenario_id), self._cache[0] if self._cache else {})

# インスタンス化の際に引数は不要になります
storage = GistStorage()