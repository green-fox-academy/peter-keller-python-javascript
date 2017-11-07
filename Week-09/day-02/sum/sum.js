var sum = {
    
    sumElements: function(numList){
        var summ = 0;
        numList.forEach(function(element) {
            summ += element;
        })
        return summ;
    }
}

module.exports = sum;