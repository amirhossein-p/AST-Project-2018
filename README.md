# Object List Merger

The goal of this project is to combine information obtained from different vision sensors that are passed through different object recognition algorithms. The program is to use this combined information to select the object recognized with the highest precision value.
For example, the following list of tuples can be received by this program:
Case 1
camera 1: [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%), (spoon, 4, 80%), (keys, 5, 95%)]
camera 2: [(knife,1, 55%), (scissor, 2, 95%), (fork, 3, 99%), (spoon, 4, 99%), (keys, 5, 95%) ]

Each of the lists above are obtained from two different cameras passed through an object recognition algorithm. The precision values above mention how accurately the algorithm was able to recognize the object. Since the algorithm used was the same for above cameras, the precision here depends on the type of camera being used.

In addition, this project can also take lists that can compare between two different algorithms used. For example:
Case 2:
camera 1, algorithm 1: [(knife,1, 20%), (scissor, 2, 25%), (spoon, 3, 83%), (spoon, 4, 50%), (keys, 5, 45%)]
camera 2, algorithm 1: [(knife,1, 95%), (scissor, 2, 55%), (fork, 3, 99%), (spoon, 4, 99%), (keys, 5, 75%) ]

camera 1, algorithm 2: [(knife,1, 59%), (scissor, 2, 75%), (spoon, 3, 83%), (spoon, 4, 30%), (keys, 5, 85%)]
camera 2, algorithm 2: [(knife,1, 35%), (scissor, 2, 95%), (fork, 3, 49%), (spoon, 4, 89%), (keys, 5, 25%) ]


In both the above cases, the program returns one list with the items that have the highest precision value. For example, the algorithm and the camera that most worked for knife would be camera 2, algorithm 1. Thus, in the list, the program will return (knife,1,95%) for knife.

## Getting Started

In the terminal, run the following command:
python3 ObjectListMerger_v3.py

### Prerequisites

This code has been developed using python 3 version 3.5.

### Installing

To clone this program, run the following command in the terminal:
```
git clone git@github.com:amirhossein-p/AST-Project-2018.git
```


## Running the tests

The development code includes a test file that contains test cases for different scenarios.
To run the test file, type the following:
```
python3 ObjectListMerger_v3_test.py
```

### Break down into end to end tests

The test file tests the different functionalities of the development code.
There are three main functionalities that are being tested:


1. get_input()
Example test_case:
```
input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]

```
2. get_output()
Example test_case:
```
input1 = [("knife",1, 99), ("scissor", 2, 65)],  input2 = [("fork", 3, 99), ("spoon", 4, 99)]
```
3. multiSelect()
Example test_case:
```
3. input11 = [['knife',1, 89]], input21 = [['knife',1, 35]], input21 = [['knife',1, 69]], input22 = [['knife',1, 80]]

```

## Deployment

The code will have to be linked to another program which will output the precision values of object recognition along with the object being recognized. The output should be in the form of a list that contains the information as tuples or lists.

```
[("knife",1, 99), ("scissor", 2, 65)],  input2 = [("fork", 3, 99), ("spoon", 4, 99)]
```

```
[["knife",1, 99], ["scissor", 2, 65]],  input2 = [["fork", 3, 99)], ["spoon", 4, 99]]
```



## Contributing

For contributing to our program, you can submit pull requests.

## Versioning

Current version is version 3.0 release 1.0

## Authors

* **Sidra Rashid** - *Initial work* - [sidra718](https://github.com/sidra718)
* **Amirhossein Pakdaman** - *Initial work* - [amirhossein-p](https://github.com/amirhossein-p)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

There is no license associated with this program.

## Acknowledgments

* Deebul Nair - https://github.com/deebuls/ast-2018
