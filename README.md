# EasyAHPTool

### Introduction

Library was originally created as part of a semester project on Operational research and complexity theory - fourth semester subject on Computer Science. Currently, the library allows you to build complex AHP decision structures, save them to a file, re-read them, as well as calculating the ranking with three methods:
* Eigenvector method
* Geometric mean method
* Normalized columns method

### Hit the ground running

To use library, it is necessary to have Python 3.5 installed along with the basic libraries supporting the calculation of the linear albebra. If you are a Ubuntu distribution user you are lucky, you can install all dependencies using the simple script contained inside repository. ``` setup_python_with_env.sh ``` For Windows users, the easiest way will be to install [Anaconda][1] and downloading the source code.

### Demo

Check how EasyAHPTool handles the calculation of the ranking based on the data read from the file.

<p align="center"> 
<img src="AHP/doc/ahp_demo.gif">
</p>

### Input file format

The library requires that the load file that defines the AHP decision tree has the following [structure][2].

```
{
  "alternatives": [
    "Tom",
    "Dick",
    ...
  ],

  "goal": {
    "name": "Most Suitable Leader",
    "preferences": [
      [1, 4, ... ], ... ],
    "children": [
      {
        "name": "Experience",
        "preferences": [...],
        "children": [...]
      },
      ... ]
   }
} 
```

[1]: https://www.anaconda.com/download/#windows
[2]: https://github.com/SkalskiP/BOiTZO/blob/master/AHP/output/MostSuitableLeader.json
