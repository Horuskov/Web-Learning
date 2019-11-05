// Object
let person = {
    name: 'Truc',
    age: 27
};

// Access the Object
person.age = 50;

let selection = 'name';
person[selection] = 'Bidule';

// Array represents a list of items
let selectedColors = ['red', 'blue'];
selectedColors[2] = 'green';

// Function to perform a task
function greet(name, lastName) { // name is a parameter
    alert('Welcome ' + name + ' ' + lastName);
}

greet('Phil', 'The Fourth'); // Phil is an argument to the parameter 'name'

// Function to calculate a value
function square(number) {
    return number * number;
}

let number = square(2);

console.log(number);