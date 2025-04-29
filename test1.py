from __future__ import annotations
from typing import Any, Dict

class Test1:
    def __init__(self) -> None:
        self.__dict__["_name_pair"] = {}     

    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__["_name_pair"][name] = value  

    def __getattr__(self, name: str) -> Any:
        print("getattr triggered")
        return self.__dict__["_name_pair"].get(name, None)  # 安全访问字典

def main() -> None:
    # 5. 正确传递初始化参数
    test_1 = Test1()  
    test_1.peter = 'alice'
    test_1.pp = 'pp'

    print(test_1.peter)
    print(test_1.pp)


if __name__ == "__main__":  # 7. 修正拼写错误 "__name__" → "__main__"
    main()