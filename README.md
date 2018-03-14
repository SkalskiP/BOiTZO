# Operational research and complexity theory
[Badania operacyjne i teoria złożoności obliczeniowej]

## AHP Project

### File format

```
{
  "alternatives": [
    "Accord Sedan",
    "Accord Hybrid",
    ...
  ],

  "goal": {
    "name": "Buy Car",
    "preferences": [
      [1.0, 3.0, ... ],
      [ ... ],
      [ ... ],
      [ ... ]
      ],
    "children": [
      {
        "name": "Cost",
        "preferences": [],
        "children": []
      },
      ...
    ]
  }
} 
```
