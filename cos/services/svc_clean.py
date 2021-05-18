import mimetypes
import os
import shutil
from pathlib import Path
from typing import Dict
from typing import List
from typing import Literal


class Clean:

    def __init__(self, directory: str, type: Literal["ext", "type"]) -> None:

        self.directory = directory
        self.type = type

    def clean(self) -> None:
        filenames = self.list_filenames()
        self.group_files(filenames)

    def list_filenames(self) -> List[str]:
        for root, _, filenames in os.walk(self.directory):
            if root == self.directory:
                return filenames

    def group_files(self, filenames: List[str]) -> List[Dict[str, List[str]]]:
        files = filenames.copy()

        if self.type == "ext":
            # extension types
            ext_types = list(set(list(map(self._get_file_ext, files))))
            # groups
            for t in ext_types:
                _dir = os.path.join(self.directory, t.replace(".", ""))
                self.create_directory(_dir)
                for _file in files:
                    if t in _file:
                        self.move_file(os.path.join(
                            self.directory, _file), os.path.join(_dir, _file))
                        files.remove(_file)

            if files:
                for _file in files:
                    self.move_file(os.path.join(
                        self.directory, _file), os.path.join(_dir, _file))
                    files.remove(_file)

        elif self.type == "type":
            f_types = ext_types = list(
                set(list(map(self._get_file_type, files))))
            for t in f_types:
                _dir = os.path.join(self.directory, t)
                self.create_directory(_dir)
                for _file in files:
                    if self._get_file_type(_file) == t:
                        self.move_file(os.path.join(
                            self.directory, _file), os.path.join(_dir, _file))

    def create_directory(self, directory_name: str) -> None:
        Path(directory_name).mkdir(exist_ok=True, parents=True)

    def move_file(self, initial: str, final: str) -> None:
        shutil.move(initial, final)

    @staticmethod
    def _get_file_ext(filename: str) -> str:
        _, f_type = os.path.splitext(filename)
        if f_type:
            return f_type

        else:
            return "msc"

    @staticmethod
    def _get_file_type(filename: str) -> str:  # return the mime type of the file
        _type = mimetypes.guess_type(filename)[0]
        return _type if _type else "msc"
