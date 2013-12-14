var cashRegisterWithChange = {
	total: 0,
	change: 0,
	setTotal: function (amount) {
		this.total = amount;
	},
	getPaid: function (amountPaid) {
		if (this.total > amountPaid) {
			console.log ("Not enough!");
		} else {
			this.change = amountPaid - this.total;
			console.log ("Give them:");
			this.howManyCoins("dollar bills", 1.00, 0);
			this.howManyCoins("quarters", 0.25, 0);
			this.howManyCoins("dimes", 0.10, 0);
			this.howManyCoins("nickels",0.05,0);
			this.howManyCoins("pennies",0.01,0);
		}
	},
	howManyCoins: function (coinName, coinAmount, coinsSoFar) {
    if (this.change < coinAmount) {
        console.log(coinsSoFar + ' ' + coinName);
        return this.change;
    } else {
        this.change -= coinAmount;
        return this.howManyCoins(coinName, coinAmount, coinsSoFar + 1);
    }
}
};

cashRegisterWithChange.setTotal(5.06);
cashRegisterWithChange.getPaid(10.00); //to get our $4.94 of change!

