import random
import time
table = [
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""]
]
formas = {
    "square": [
        ["#", "#"],
        ["#", "#"]
    ],
    "line": [
        [["#"],
         ["#"],
         ["#"],
         ["#"]],
        ["#", "#", "#", "#"]
    ],
    "lr": [
        [["#", "#", "#"],
         ["#", "", ""]],
        [["#", "#"],
         ["", "#"],
         ["", "#"]],
        [["", "", "#"],
         ["#", "#", "#"]],
        [["#", ""],
         ["#", ""],
         ["#", "#"]]
    ],
    "ll": [
        [["#", "", ""],
         ["#", "#", "#"]],
        [["#", "#"],
         ["#", ""],
         ["#", ""]],
        [["#", "#", "#"],
         ["", "", "#"]],
        [["", "#"],
         ["", "#"],
         ["#", "#"]]
    ],
    "t": [
        [["", "#", ""],
         ["#", "#", "#"]],
        [["#", ""],
         ["#", "#"],
         ["#", ""]],
        [["#", "#", "#"],
         ["", "#", ""]],
        [["", "#"],
         ["#", "#"],
         ["", "#"]]
    ],
    "zr": [
        [["", "#", "#"],
         ["#", "#", ""]],
        [["#", ""],
         ["#", "#"],
         ["", "#"]]
    ],
    "zl": [
        [["#", "#", ""],
         ["", "#", "#"]],
        [["", "#"],
         ["#", "#"],
         ["#", ""]]
    ]
}