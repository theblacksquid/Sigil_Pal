
/*
 * SigilPal.js is a JavaScript implementation of my SigilPal.py
 * program that turns a statement of intent into a string of letters
 * and provide numerological values to it for sigilwork.
 */
 
numerology = {
	"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,
	"J":10,"K":20,"L":30,"M":40,"N":50,"O":60,"P":70,"Q":80,"R":90,
	"S":100,"T":200,"U":300,"V":400,"W":500,"X":600,"Y":700,"Z":800,
	} 

function getNumList(string) {
	var index = 0; result = [];			// turns a string value into
	var str = string.toUpperCase()		// an array of its numerical
	for (var char in str) {			// equivalents based on object
		if (str[index] === " ") {	// numerology
			index = index + 1;
			continue;
			}
			
		else {
			var i = str[index];
			var num = numerology[i];
			result.push(num);
			index = index + 1;
			}
		};
	
	return result;
	}

function getNumVal(numArray) {
	var result = 0;
	for (var i in numArray) {
		result = result + numArray[i];
		};
	return result;
	}
	
function getBaseNum(int_val) {
	var string = String(int_val);
	while (string.length != 1) {
		var result = 0;
		for (var i in string) {
			result = result + Number(string[i])
			};
		string = String(result);
		};
	return result;
	}
	
function check(item, list) {
	for (var i in list) {
		var n = list[i];
		if (n === item) {
			return true;
			}
		};
	return false;
	}

function xtract_letters(string) {
	var result = ""; already = [];
	for (var i in string) {
		var letter = string[i].toUpperCase();
		if (check(letter, already) == true) {
			continue;
			}
		else {
			already.push(letter);
			result = result + letter
			}
		};
	return result;
	}
	

	
	
	
