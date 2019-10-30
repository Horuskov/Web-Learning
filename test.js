// Example
function ourReusableFunction(name) {
    this.name = name;

    // print in the console when a function starts
    this.fStart = function () {
        console.log("This function started properly: " + name + "().");
    }

    // print in the console when a function ends
    this.fEnd = function () {
        console.log("This function ended properly: " + name + "().");
    }
}

function checkingFunction() {
    var namefunction = 'checkingFunction';
    ourReusableFunction(namefunction).fStart;

    console.log(1 + 1);
};


checkingFunction();

  // Only change code below this line
