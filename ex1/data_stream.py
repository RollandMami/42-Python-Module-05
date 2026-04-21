#!/usr/bin/env python3
# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    data_stream.py                                    :+:      :+:    :+:   #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/20 08:31:19 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/20 08:31:19 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: int):
        self.stream_id: int = stream_id
        self.current_data: List[Any] = []
        self.last_criteria: Optional[str] = None

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch:  List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        self.current_data = data_batch
        self.last_criteria = criteria
        if not criteria:
            return data_batch
        return [
            elm for elm in data_batch 
            if type(elm) is str and criteria in elm
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        data: List[Any] = self.current_data
        criteria: Optional[str] = self.last_criteria
        filtered = self.filter_data(data, criteria)
        total: int = len(data)
        count: int = len(filtered)
        return {
            "stream_id": self.stream_id,
            "last_criteria": criteria if criteria else "None",
            "count": count,
            "total": total,
            "avg": count / total if total > 0 else 0.0
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: int):
        super().__init__(stream_id)

    def process_batch(self, data_batch:  List[Any]) -> str:
        pass

    def filter_data(self, data_batch:  List[Any],
                    criteria:  Optional[str]= None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass
    
    def __str__(self) -> str:
        return f"SENSOR_{self.stream_id}"

class TransactionStream(DataStream):
    def __init__(self, stream_id: int):
        super().__init__(stream_id)

    def process_batch(self, data_batch:  List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch:  List[Any],
                    criteria:  Optional[str]= None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass

    def __str__(self) -> str:
        return f"TRANS_{self.stream_id}"


class EventStream(DataStream):
    def __init__(self, stream_id: int):
        super().__init__(stream_id)

    def process_batch(self, data_batch:  List[Any]) -> str:
        pass

    def filter_data(self, data_batch:  List[Any],
                    criteria:  Optional[str]= None) -> List[Any]:
        if (criteria):
            pass
        else:
            pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass

    def __str__(self) -> str:
        return f"EVENT_{self.stream_id}"


class StreamProcessor():
    def __init__(self):
        pass