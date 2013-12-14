//Your three dimensional array from the last exercise probably
//looked something like this:
var hands = [];
hands[0] = [ [3,"H"], ["A","S"], [1,"D"], ["J","H"], ["Q","D"] ];
hands[1] = [ [9,"C"], [6,"C"], ["K","H"], [3,"C"], ["K","H"] ];

//Loop over every dimension in the array, logging out the suit and rank
//of each card in both hands
//1. loop over each hand
for (var i=0;i<hands.length;i++) {
    //2. loop over each card array in each hand
    for (var j=0;j<hands[i].length;j++) {
        //3. loop over each rank/suit array for each card in each hand
        for (var k=0;k<hands[i][j].length;k++) {
            //4. log the value of the rank/suit array item
            console.log(hands[i][j][k]);
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////

//students on the roll
var roll = ["robert","joe","sharon"];

//students actually in the class
var students = {"sharon":true, "robert":true};

//Loop over the roll array. For each name in the roll array, check if 
//that name exists in the students associate array.
//Whenever you find a student that is present, increment the numPresent
//counter by 1
var numPresent = 0;
for (var i=0;i<roll.length;i++){
    if (students[roll[i]] === true) {
        numPresent +=1;
    }
}


////////////////////////////////////////////////////////////////////////////////////////////

var hand = [];
hand[0] = {'suit':'clubs','rank':8};
hand[1] = {'suit':'spades','rank':'A'};
hand[2] = {'suit':'hearts','rank':2};
hand[3] = {'suit':'hearts','rank':'K'};
hand[4] = {'suit':'clubs','rank':9};

for (var h in hand){
    console.log(hand[h].suit + ' ' + hand[h].rank);
}