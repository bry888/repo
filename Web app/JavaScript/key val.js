var deck = [];
var a = ['clubs','spades','hearts','diamonds'];
var b = [2,3,4,5,6,7,8,9,10,'J','D','K','A'];
for (var i=0;i<a.length;i++) {
    for (var j=0;j<b.length;j++){
        var card = {'rank': a[i], 'suit': b[j]};
        deck.push(card);
        console.log(card);
    }
}