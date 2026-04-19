```python
import json

data = {"name": "小明", "age": 20}
json_str = json.dumps(data)

translated_data = json.loads(json_str)
```
