
/*
    SigilPal.js
    This is a JavaScript implementation of my earlier 
    SigilPal.py program. This contains the back-end logic 
    that will be rendered on screen by the included webApp

*/

var numerology = {
"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
"J":10,"K":20,"L":30,"M":40,"N":50,"O":60,"P":70,"Q":80,"R":90,
"S":100,"T":200,"U":300,"V":400,"W":500,"X":600,"Y":700,"Z":800,
    }


function getNumList(string_val) {
    var i = 0; result = [];
    var str = string_val.toUpperCase();
    while (i < string_val.length) {
        var x = str[i];
        if (x === " ") {
            i = i + 1;
            continue;
            }
        else {
            result.push(numerology[x]);
            i = i + 1;
            }
        };
    return result;
    }

function getNumVal(int_list) {
    var result = 0;
    for (var i in int_list) {
        result = result + int_list[i];
        };
    return result;
    }

function getBaseNum(int_val) {
    var str = String(int_val);
    var list = []; i = 0;
    var result =0;
    while (str.length > 1) {
        while (i < str.length) {
            list.push(Number(str[i]));
            i = i + 1;
            };
        for (var x in list) {
            result = result + list[x];
            };
        str = Number(result);
        }
    return result;
    }
