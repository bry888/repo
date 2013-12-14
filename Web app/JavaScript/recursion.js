var currency = [5.00, 1.00, 0.25, 0.10, 0.01];
var coinNames = ["five dollar bills", "one dollar bills", "quarters", "dimes", "pennies"];

function makeChange (coinNames, currency, index) {
	if (index>=list.length) {
		return;
	} else if (change<currency[index]) {
        index +=1;
        change -= currency[index];
        console.log(currency[index] + ' ' + coinNames[index]);
        makeChange(coinNames[index], currency[index], index);
	} else {
        change -= currency[index];
		console.log(currency[index] + ' ' + coinNames[index]);
        makeChange(coinNames[index], currency[index], index);
	}
}

change = 18.94;
makeChange(coinNames, currency, 0);