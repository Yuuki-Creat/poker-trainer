from typing import Dict, List
import httpx
import json
import os

class GistStorage:
    def __init__(self, gist_url: str):
        self.gist_url = gist_url
        self._cache: List[Dict] = []

    async def reload_scenarios(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.gist_url)
            if response.status_code == 200:
                self._cache = response.json()
                print(f"Successfully loaded {len(self._cache)} scenarios from Gist.")
            else:
                raise Exception("Failed to fetch scenarios from Gist")

    def get_all(self) -> List[Dict]:
        return self._cache

    def get_by_id(self, scenario_id: int) -> Dict:
        return next((s for s in self._cache if s["id"] == scenario_id), self._cache[0])

RAW_GIST_URL = os.getenv("RAW_GIST_URL")
storage = GistStorage(RAW_GIST_URL)