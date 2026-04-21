#!/usr/bin/env python3
# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    stream_processor.py                               :+:      :+:    :+:   #
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

    @abstractmethod
    def process(self, data:  Any) -> str:
        pass

    @abstractmethod
    def validate(self, data:  Any) -> bool:
        pass

    def format_output(self, result:  str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):

    def process(self, data:  Any) -> str:
        data: List[Any] = list(data)
        somme: int = 0
        for x in data:
            somme += float(x)
        average: float = somme / len(data) if data else 0
        return (f"{len(data)} numeric values, sum={somme}, avg={average:.1f}")

    def validate(self, data:  Any) -> bool:
        try:
            for x in list(data):
                if type(x) not in Union[int, float]:
                    return 0
            return 1
        except (ValueError, TypeError):
            return 0

    def format_output(self, result:  str) -> str:
        return f"Processed {result}"


class TextProcessor(DataProcessor):

    def process(self, data:  Any) -> str:
        data: str = str(data)
        word: int = len(data.split())
        return (f"{len(data)} characters, {word} words")

    def validate(self, data:  Any) -> bool:
        if type(data) == str:
            return 1
        return 0

    def format_output(self, result:  str) -> str:
        return f"Processing text: {result}"


class LogProcessor(DataProcessor):

    def process(self, data:  Any) -> str:
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

    def validate(self, data:  Any) -> bool:
        lvl_lst: List[str] = ['INFO', 'ERROR', 'DEBUG', 'ALERT']
        if type(data) == str and any(lvl in data for lvl in lvl_lst):
            return 1
        return 0

    def format_output(self, result:  str) -> str:
        return f"{result}"


def main():

    def example() -> None:
        print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
        list_data: list = [
            (NumericProcessor(), "Numeric", [1, 2, 3, 4, 5], "data"),
            (TextProcessor(), "Text", "Hello Nexus World", "data"),
            (LogProcessor(), "Log", "ERROR: Connection timeout", "entry")
        ]
        for objects, label, data, form in list_data:
            print(f"\nInitializing {label} Processor...")
            if objects.validate(data) is True:
                print(f"Processing data: {data}")
                result = objects.process(data)
                print(f"Validation: {label} {form} verified")
                print(f"Output: {objects.format_output(result)}")
            else:
                print(f"Erreur de validation de {data}")

        print("\n=== Polymorphic Processing Demo ===")

    def code_nexus() -> None:
        print("Processing multiple data types through same interface...")
        print(f"Result 1: Processed {NumericProcessor().process([2, 2, 2])}")
        print(f"Result 2: Processed text: \
{TextProcessor().process('Hello worlds')}")
        print(f"Result 3: {LogProcessor().process('INFO: System ready')}")
        print("\nFoundation systems online. Nexus ready for advanced streams")

    example()
    code_nexus()


if __name__ == "__main__":
    main()
