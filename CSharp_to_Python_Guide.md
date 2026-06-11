# Cẩm nang chuyển từ C# sang Python cho Dev C#

## 1. Tư duy khác biệt cốt lõi

### C#
```csharp
public class User
{
    public string Name { get; set; }
}
```

### Python
```python
class User:
    def __init__(self, name):
        self.name = name
```

Lưu ý:

- Python không dùng `{}` để tạo block.
- Thụt lề (indentation) là cú pháp bắt buộc.
- Không cần khai báo kiểu dữ liệu ở biến.

---

## 2. Khai báo biến

### C#
```csharp
string name = "John";
int age = 20;
```

### Python
```python
name = "John"
age = 20
```

### Type Hint (khuyến nghị)

```python
name: str = "John"
age: int = 20
```

Python không ép buộc type hint nhưng nên dùng trong dự án lớn.

---

## 3. None ≈ null

### C#
```csharp
string? name = null;
```

### Python
```python
name = None
```

Kiểm tra:

```python
if name is None:
    print("null")
```

Không dùng:

```python
if name == None:
    pass
```

---

## 4. So sánh giá trị và tham chiếu

### C#
```csharp
obj1 == obj2
ReferenceEquals(obj1, obj2)
```

### Python

```python
a == b      # so sánh giá trị
a is b      # cùng object
```

Ví dụ:

```python
x = [1, 2]
y = [1, 2]

print(x == y)  # True
print(x is y)  # False
```

---

## 5. List ≈ List<T>

### C#
```csharp
var nums = new List<int> {1,2,3};
```

### Python

```python
nums = [1, 2, 3]
```

Thêm phần tử:

```python
nums.append(4)
```

Duyệt:

```python
for n in nums:
    print(n)
```

---

## 6. Dictionary

### C#
```csharp
var dict = new Dictionary<string, int>();
dict["a"] = 1;
```

### Python

```python
data = {
    "a": 1
}
```

Lấy an toàn:

```python
value = data.get("a")
```

Tránh:

```python
value = data["missing"]
```

sẽ phát sinh KeyError.

---

## 7. Tuple

```python
point = (10, 20)

x, y = point
```

Rất phổ biến trong Python.

---

## 8. ForEach vs Pythonic Loop

### C#
```csharp
foreach(var item in items)
{
    Console.WriteLine(item);
}
```

### Python

```python
for item in items:
    print(item)
```

---

## 9. LINQ → Comprehension

### C#
```csharp
var result = numbers
    .Where(x => x > 10)
    .Select(x => x * 2)
    .ToList();
```

### Python

```python
result = [x * 2 for x in numbers if x > 10]
```

Đây là kỹ năng quan trọng nhất khi chuyển sang Python.

---

## 10. Lambda

### C#
```csharp
x => x * 2
```

### Python

```python
lambda x: x * 2
```

Ví dụ:

```python
sorted(users, key=lambda u: u.age)
```

---

## 11. Exception

### C#
```csharp
try
{
}
catch(Exception ex)
{
}
finally
{
}
```

### Python

```python
try:
    pass
except Exception as ex:
    pass
finally:
    pass
```

---

## 12. Class và Dataclass

Thay vì viết constructor dài:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Sẽ tự sinh:

- __init__
- __repr__
- __eq__

Rất giống record của C#.

---

## 13. Property

### C#
```csharp
public string Name { get; set; }
```

### Python

```python
class User:

    @property
    def name(self):
        return self._name
```

Dùng khi cần logic đặc biệt.

---

## 14. Interface

Python không có interface truyền thống.

Thường dùng:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

---

## 15. Async Await

### C#
```csharp
await service.GetAsync();
```

### Python

```python
await service.get_async()
```

Định nghĩa:

```python
async def get_user():
    return "user"
```

Chạy:

```python
import asyncio

asyncio.run(get_user())
```

---

## 16. Package Management

### C#
- NuGet

### Python
- pip
- uv (rất khuyến nghị năm 2026)
- poetry

Ví dụ:

```bash
uv add requests
```

---

## 17. Virtual Environment

Không cài package global.

```bash
python -m venv .venv
```

hoặc

```bash
uv venv
```

Kích hoạt:

```bash
.venv\Scripts\activate
```

---

## 18. Project Structure Khuyến nghị

```text
project/
│
├── src/
│   └── app/
│       ├── services/
│       ├── repositories/
│       └── models/
│
├── tests/
├── pyproject.toml
└── README.md
```

---

## 19. Logging

Đừng spam print.

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Hello")
```

---

## 20. Type Hint rất quan trọng

```python
def add(a: int, b: int) -> int:
    return a + b
```

Dùng cùng:

- mypy
- pyright

để có trải nghiệm gần C# hơn.

---

## 21. Mutable Pitfall

Sai:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Đúng:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

Đây là bug kinh điển của dev mới học Python.

---

## 22. List Copy

Sai:

```python
b = a
```

Đúng:

```python
b = a.copy()
```

hoặc

```python
import copy

b = copy.deepcopy(a)
```

---

## 23. Context Manager

Tương tự using trong C#

### C#
```csharp
using(var file = new StreamReader(path))
{
}
```

### Python

```python
with open("file.txt") as f:
    data = f.read()
```

---

## 24. Enum

```python
from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2
```

---

## 25. Dependency Injection

Python ít dùng container nặng như .NET.

Thường:

```python
class UserService:
    def __init__(self, repo):
        self.repo = repo
```

Inject thủ công.

---

## 26. Framework Mapping

| C# | Python |
|-----|---------|
| ASP.NET Core | FastAPI |
| Entity Framework | SQLAlchemy |
| xUnit | pytest |
| Serilog | logging |
| AutoMapper | pydantic/dataclass |
| Hangfire | Celery |
| MediatR | Không quá phổ biến |

---

## 27. Testing

### pytest

```python
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
```

Chạy:

```bash
pytest
```

---

## 28. Pydantic (rất quan trọng với FastAPI)

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Validation tự động.

---

## 29. Pythonic Code

Dev C# mới sang thường viết:

```python
for i in range(len(items)):
    print(items[i])
```

Pythonic:

```python
for item in items:
    print(item)
```

Hoặc:

```python
for index, item in enumerate(items):
    print(index, item)
```

---

## 30. Checklist học nhanh

Tuần 1
- Syntax
- List
- Dict
- Function
- Exception

Tuần 2
- OOP
- Dataclass
- Type Hint
- Context Manager

Tuần 3
- Asyncio
- FastAPI
- SQLAlchemy

Tuần 4
- pytest
- Docker
- CI/CD

---

# Stack Python khuyến nghị cho Dev Backend năm 2026

- Python 3.13+
- uv
- FastAPI
- Pydantic v2
- SQLAlchemy 2
- Alembic
- pytest
- Ruff
- Pyright
- Docker
- PostgreSQL
- Redis

# Điều khó nhất với Dev C#

1. Dynamic typing.
2. Mutable object.
3. Import system.
4. Asyncio.
5. Pythonic thinking.

Nếu vượt qua 5 phần này thì tốc độ làm việc sẽ tăng rất nhanh.
