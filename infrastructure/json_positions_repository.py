import json
from pathlib import Path
from dataclasses import asdict

from domain.position_repository import IPositionRepository
from domain.position import Position

class JsonPositionRepository(IPositionRepository):
    # Реализация хранения данных о должностях в формате JSON
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def get_all(self) -> list[Position]:
        # Считать все данные из файла
        if not self.file_path.exists():
            return[]

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return [Position(**item) for item in data]
        except json.JSONDecodeError:
            print("Файл JSON повреждён или пуст")
            return []

    def save_all(self, positions: list[Position]) -> None:
        # Сохрнанение объектов в JSON-файл    

        data = [asdict(pos) for pos in positions]

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)