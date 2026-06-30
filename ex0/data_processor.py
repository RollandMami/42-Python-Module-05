#!/usr/bin/env python3
# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    data_processor.py                                 :+:      :+:    :+:   #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/20 08:31:23 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/20 08:31:23 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

from typing import Any, List, Union, Dict
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self):
        self._data

    @abstractmethod
    def ingest(self, data:  Any) -> None:
        pass

    @abstractmethod
    def validate(self, data:  Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        return


class NumericProcessor(DataProcessor):

    def ingest(self, data:  Any) -> None:
        try:
            if not self.validate(data):
                raise ValueError("Got exception: Improper numeric data")
            data: List[Any] = list(data)
            somme: int = 0
            for x in data:
                somme += float(x)
            average: float = somme / len(data) if data else 0
            return (f"{len(data)} numeric values,\
                    sum={somme},\
                    avg={average:.1f}")
        except ValueError as e:
            print(e)

    def validate(self, data:  Any) -> bool:
        try:
            for x in list(data):
                if type(x) not in Union[int, float]:
                    return 0
            return 1
        except (ValueError, TypeError):
            return 0


class TextProcessor(DataProcessor):

    def ingest(self, data:  Any) -> None:
        try:
            if not self.validate(data):
                raise ValueError("")
            data: str = str(data)
            word: int = len(data.split())
            return (f"{len(data)} characters, {word} words")
        except ValueError:
            pass

    def validate(self, data:  Any) -> bool:
        if type(data) == str:
            return 1
        return 0


class LogProcessor(DataProcessor):

    def ingest(self, data:  Any) -> None:
        try:
            if not self.validate(data):
                raise ValueError
            lbl: Dict[str, str] = {
                "ERROR": "[ALERT]",
                "INFO": "[INFO]",
                "ALERT": "[ALERT]",
                "DEBUG": "[DEBUG]"
                }
            lst: List[Any] = str(data).split(": ")
            lvl: str = lst[0]
            msg: str = lst[1].strip()
            return (f"{lbl[lvl]} {lvl} level detected: {msg}")
        except ValueError:
            pass

    def validate(self, data:  Any) -> bool:
        lvl_lst: List[str] = ['INFO', 'ERROR', 'DEBUG', 'ALERT']
        if type(data) == str and any(lvl in data for lvl in lvl_lst):
            return 1
        return 0


def main():

    def example() -> None:
        print("=== Code Nexus - Data Processor ===")
        list_data: list = [
            (NumericProcessor(), "Numeric", [1, 2, 3, 4, 5], "data"),
            (TextProcessor(), "Text", "Hello Nexus World", "data"),
            (LogProcessor(), "Log", "ERROR: Connection timeout", "entry")
        ]
        for objects, label, data, form in list_data:
            print(f"\nInitializing {label} Processor...")
            if objects.validate(data) is True:
                print(f"Processing data: {data}")
                result = objects.ingest(data)
                print(f"Validation: {label} {form} verified")
                print(f"Output: {objects.output(result)}")
            else:
                print(f"Erreur de validation de {data}")

        print("\n=== Polymorphic Processing Demo ===")

    def code_nexus() -> None:
        print("Processing multiple data types through same interface...")
        print(f"Result 1: Processed {NumericProcessor().ingest([2, 2, 2])}")
        print(f"Result 2: Processed text: \
{TextProcessor().ingest('Hello worlds')}")
        print(f"Result 3: {LogProcessor().ingest('INFO: System ready')}")
        print("\nFoundation systems online. Nexus ready for advanced streams")

    example()
    code_nexus()


if __name__ == "__main__":
    main()
