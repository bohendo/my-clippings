---
# Javascript: The Good Parts
### By Douglas Crockford
---

>Bo's notes: This is a mixture of syntax rules and best practices. Some of the style guidelines are a little extreme so don't take these best practices to be absolute truths. I break some of this advice regularly and I'm ok with that. Regardless, these are good ideas to be exposed to.

# Grammar
---

 - In general, prefer // comments over /* */ because slashes and stars show up in string literals somewhat often
 - Warning: undefined, NaN, Infinity are not enforced as being reserved words. Don't use them as variable names!
 - Infinity represents all numbers greater than 1.8e+308
 - Falsy: false, null, undefined, '', 0, Nan... all other values are truthy
 - Check object.hasOwnProperty() when writing for-in loops to make sure that properties aren't pulled from the prototype chain.
 - Break statements can be followed by a label to specify which statement to break from
 - Operator Precedence:
     1: .[]()
     2: unary operators: delete new typeof + - !
     3: * / %
     4: + -
     5: > < >= <=
     6: === !==
     7: &&
     8: ||
     9: ternary operator aka ?:
 - && produces the value of the first operand if it is falsy, otherwise returns the second
 - || produces the value of the first operand if it is truthy, otherwise returns the second
 - LIST OF RESERVED WORDS: abstract boolean break byte case catch char class const continue debugger default delete do double else enum export extends false final finally float for function goto if implements import in instanceof int interface long native new null package private protected public return short static super switch synchronized this throw throws transient true try typeof var volatile void while with

# Objects
---

 - Arrays are objects, functions are objects, regular expressions are objects
 - The || operator is useful in assigning object properties default values
 - Objects are passed around by reference and are never copied
 - If we request an object property and it's not found, JS looks at the prototype and it's prototype's prototype until it bottoms out at Object.prototype: the ancestor of all objects.
 - Typeof operator and hasOwnProperty() are valuable when inspecting object properties
 - Delete removes object properties but might allow prototype properties to shine through if it was overwritten
 - One way to minimize the use of global variables is to create your own, controlled global object

# Functions
---

 - Function objects are linked to Function.prototype which inherits from Object.prototype
 - Function objects have two hidden properties: the function's context and the code to be executed
 - In addition to their parameters, every function receives two additional parameters: this and arguments
 - The value of a function's 'this' depends on how the function is invoked
 - When a function is invoked as a method ie myObject.increment();, 'this' refers to the parent object
 - When a function is invoked as a function ie var a = sum(2,3);, 'this' refers to the global object.. That's not good. In this way, inner functions of methods don't have access to the same this.. but there's an easy solution: bind a new variable ie self or that to this in the method so that the inner function can refer to it.
 - Constructors are functions designed to be called with a new prefix. By convention, capitalize these function names because bad things can happen if constructors are called without the new prefix so it's important to be able to tell constructors apart. Constructors initialize objects by setting some this.properties.. you don't want to accidentally start clobbering the global object! There are better constructor alternatives though. see ./code/javascript-good-parts/apply-example.js
 - The apply method allows us to construct an array of parameters to pass to a function in addition to allowing us to set this. apply is a function method that can be used to invoke an object method on an unrelated object. see ./apply-example.js
 - A function's arguments parameter stores all parameters including those which overflowed the defined parameters. It can be looped through to create a function that accepts an arbitrary number of parameters. It is generally better to accomplish this kind of task by adding a method to an array as the arguments object lacks array methods.
 - Usually when a function doesn't specify it's return value, undefined is returned. When a function invocation is prefixed by new and an object is not explicitly returned, this is returned instead of undefined.
 - A try statement has a single catch block that will handle all exceptions. The error's name can be inspected in this catch block to handle different types of errors differently.
 - Prototypes can be modified to affect all objects. In this way, a trim() method can be added to the String.prototype or a toInt() method can be added to the Number.prototype. see ./augmentations.js. JS is very dynamic, even Strings/Numbers defined before these changes were implemented are affected by them. In complicated projects, you might want to add a check to ensure this new method doesn't exist yet. Remember to use hasOwnProperty()!
 - JS doesn't provide tail recursion optimization so be careful when using deep recursion.
 - JS doesn't have block scope so as far as variable visibility is concerned, curly braces don't matter (there is function scope though). The lack of block scope means it's best to define all variables used in a function at the top of the function to clarify which variables are available.
 - Objects can be insulated from the rest of the program by wrapping them up in a function. see ./isolated-object.js
 - Outer function variables will persist if needed by an inner function even after the outer function has returned.
 - Thanks to closure, modules can be defined using a self-executing function. This eliminates the need for global variables and mitigates JS's biggest weakness. In the same way, secure objects can be created whose values can only be accessed via their own methods.
 - It's common for an object method to modify values but not return anything. If we have these methods return this, we can enable cascades ie: element.set('property').move('up').setHidden('false')
 - Currying allows us to predefine some function arguments, see ./augmentations.js for implementation + an example
 - Closure is invaluable when memoizing. For example, a fibonocci function can include a built in array of previously computed values which is checked before any new values are computed. check out ./memoization.js for some very cool examples.

# Inheritance
---

 - Capitalizing only functions that need to be prefixed by new is an attempt at lessening the dangers of these constructor functions.. A better solution is to just not use the new prefix at all. JS is very powerful, it doesn't need it.
 - When a long list of parameters are required, remembering the order can be difficult. It's often better to accept a single object parameter which contains all the required arguments as property values. In this way, order doesn't matter and it's very clear where your data's going.
 - To grant privacy to variables, confine these variables to an object in the scope of a new function within which another object is created and returned. This inner object has access to this secret data. See ./private-variables.js for a cool example. This example outlines the creation of durable objects aka objects that cannot be compromised. Make sure none of the methods make use of this or that however.

# Arrays
---

 - In a lot of languages, arrays are adjacent memory positions and operations dealing with arrays are very fast.. that's not the case with JS but what we lose in efficiency is gained in convenience. Being able to mix up types within an array is one example of JS array flexibility.
 - JS arrays never really throw out of bounds exceptions. They grow/shrink dynamically.
 - When you store an element in a JS array at an index greater than the array's length, the array will automatically be lengthened to accommodate this new value. The length property will track the largest index rather than the number of defined values. max array length is 4 billion.
 - The length property can be set manually. Increasing it does not increase the amount of memory the array requires. Decreasing it will delete any elements that are now out of bounds.
 - Using the keyword delete on an array element will set that index to undefined and will not shrink the array's length. The splice(n, m) method can achieve a cleaner delete where n is the index of the element of interest and m is the number of elements to remove. In this case, higher indices will be shifted and the array length will decrease. This is not a very efficient method though..
 - Use conventional for statements to iterate over an array to avoid involving any methods or inherited values. Also, the order in which properties are accessed during a for-in loop can't be guaranteed.
 - Identifying something as an array is not straightforward, the typeof function just returns object. The workaround is provided in ./arrays.js.
 - We can add methods to the array prototype to affect ALL arrays or, because arrays are just fancy objects, we can whatever methods we like to arrays. Beware, if you add a method to an array and name it with an integer string, the length property will be affected.
 - If you want to initialize an array, you'll have to do it yourself (or augment the Array prototype to include an init function as seen in ./arrays.js)
 - JS does not support multidimensional arrays but it does support arrays of arrays of arrays so that's basically the same thing since these elements can still be accessed like arr[1][2]. No matrix initialization functions are provided but these are easy enough for us to add on our own as seen in ./arrays.js

# Regular Expressions
---

 - methods: exec, test, match, replace, search, and split.. these will be covered in more detail in the next section.
 - properties: global (true/false depending on flag), ignoreCase (true/false depending on flag), lastIndex (zero initially, index at which to start matching), multiline (true/false depending on flag), source (text that generated the regex).
 - Regular expressions are dangerous to create and edit without a complete understanding of the regex rules. It's best to use a subset of the most intuitive features whenever possible. Regular expressions are a popular source of security exploits! Keep them as short and simple as possible. Performance issues might pop up if a regex gets complicated or especially when dealing with nested regexes.
 - start of string anchor: ^ also matches line endings if m flag is provided
 - end of string anchor:   $ also matches line endings if m flag is provided
 - any of a range of characters: [a-z]
 - anything except this range of characters: [^a-z]
 - capturing group:    (...)
 - noncapturing group: (?:...)
 - capturing a group has a performance penalty so don't capture unless you have to.
 - It's valuable to nest capturing groups within noncapturing groups. What I want might be a port number that I could capture with (?:port:(/d+))
 - regex literal: var newRegEx = /regex/flag; where flag is one or more of i (case insensitive), m (multi-line), g (global)
 - regex constructors are good if you need to build a regex at runtime given some variables: var newRegEx = new RegExp("string that compiles to a regex", "flags"); but be careful because the syntax is different than in regex literals. In generally, you'll want to double backslashes and escape quotes but beware, there might be other differences.
 - variables assigned to a regexp object all share a single instance. Edit the lastIndex in one and you edit it in all of them.
 - a bar | is similar to an 'or' where a match is attempted against each expression left-to-right so /in|int/ would always match in.
 - control characters need to be escaped w backslash to make literal: ( ) [ ] { } \ / ? + * | . ^ $
 - within a character class enclosed with [], \b IS backspace and we have a different set of control chars that need to be escaped w \ to be made literal: - / [ \ ] ^
 - beware: regexes have pathetic multilingual support
 - \f is formfeed character, \n is newline, \r is carriage return, \t is tab, \u#### is unicode char w # being a hexadecimal digit.
 - \b is NOT a backspace char like in strings
 - \d === [0-9] && \D === [^0-9]
 - \s === [\f\n\r\t\u000B\u0020\u00A0\u2028\u2029], \S === [^\f\n\r\t\u000B\u0020\u00A0\u2028\u2029]
 - \w === [0-9A-Z_a-z], \W === [^0-9A-Z_a-z]
 - A more elaborate letter class: [A-Za-z\u00C0-\u1FFF\u2800-\uFFFD] but this includes thousands of non-letter characters
 - \b is a word boundary using \w to define words
 - \1 is a reference to the text that was captured by group one. Take note that capture indices do NOT start at zero. The first group is defined by the first occurrence of (
 - \2 references text captured by group 2 and on and on.
 - quantifiers define how many matches are ok like so: {min, max}
 - ? === {0,1}, + === {1,}, * === {0,}
 - quantifiers are greedy by default: they attempt to match as many as possible and increment down to min
 - adding an ? to a quantifier (ie ?? +? \*?) makes them lazy: they attempt to match as few as possible and increment up. Greedy is usually faster.

# Methods
---

 - array.concat(item...) == concatenates the list of arguments to the end of the array. Flattens input arrays to avoid having arrays of arrays.
 - array.join(separator) == generate a string from the array w each element separated by separator
 - array.pop() == removes and returns the last element of the array
 - array.push(item...) == appends items to the end of the array. Does not do any flattening. Returns the new length.
 - array.reverse() == both reverses the input array and returns this new array
 - array.shift() == removes and returns the first element of the array. Not as quick as pop().
 - array.slice(start, end) == returns elements from [start] to [end - 1] but does not modify the array
 - array.sort(compareFn) == Converts all elements to strings and sorts alphabetically by default.. You definitely want to use a different compareFn to sort numbers. compareFn(a, b) needs to return 0 if elements are equal, negative if a should come first, and positive if b should come first. return a - b is good for sorting numbers. To sort objects or strings you'll want to do something like return [comparison] ? -1 : 1;
 - array.splice(start, deleteCount, item...) == removes deleteCount items starting at start. If additional arguments are passed, they are inserted in place of the removed items.
 - array.unshift() == Just like push() except it adds elements to the front of the array
 - function.apply(thisArg, argArray) == invokes a function but binds this to thisArg and passes each element of the argArray to the function as parameters.
 - number.toExponential(fractionDigits) == converts number to exponential form with the given number of digits
 - number.toFixed(fractionDigits) == converts number to string in decimal form with the given number of digits (defaults to 0)
 - number.toPrecision(precision) == converts number to string in decimal form with the given number of significant figures
 - number.toString(radix) == can also be written as String(number) if radix is 10 (this is the default case)
 - object.hasOwnProperty(name) == returns true if the object has a property called name, prototype chain is NOT checked
 - regexp.exec(string) == returns an array with element 0 being the substring that matched the regexp, element 1 is the text captured by group 1, etc. If the 'g' flag is set, searching begins at position regexp.lastIndex. A successful match sets regexp.lastIndex to the first char after the match, an unsuccessful match sets it to 0.
 - regexp.test(string) == returns true if the regexp matches the string, false otherwise. This one is much faster than regexp.exec(). Don't use the 'g' flag here.
 - string.charAt(pos) == returns string containing the character at position pos. Returns empty string if out of bounds.
 - string.charCodeAt(pos) == same as string.charAt() except it return an integer representing the code point of that char. Returns NaN if out of bounds.
 - string.concat(string...) == rarely used because + is more convenient
 - string.indexOf(searchString, position) == returns the position of the searchString within string. Searching starts at position if that parameter is given. Returns -1 if no match is found.
 - string.lastIndexOf(searchString, position) == same as above but it start searching from the end of the string.
 - string.localCompare(that) == compares strings like: 'a' < 'A' < 'aa' < 'Aa' < 'aaa' < 'AAA'
 - string.match(regexp) == if there's no 'g' flag, the result is the same as regexp.exec(string). If there is a 'g' flag, then this returns an array of matches but ignores capturing groups.
 - string.replace(searchValue, replaceWith) == replaces searchValue with replaceWith in string. searchValue can be a string or regexp. Only the first occurrence will be replaced unless searchValue is a regexp with the 'g' flag. $ is a special control character in the replaceWith string: $$ -> $, $& -> matched text, $number -> capture group text, $` -> text preceding the match, $' -> text after match. replaceWith can also be a function, in this case it will be called for every match and the return value will be used as the replacement text. The first argument passed to this function is the matched text, the second is text from the first capturing group, etc.
 - string.search(regexp) == like indexOf except it accepts a regexp instead of a string. the 'g' flag is ignored and -1 is returned if there is no match.
 - string.slice(start, end) == returns the substring from start to end (exclusive of end). end is optional and defaults to string.length. If either parameter is negative, string.length is added to it.
 - string.split(separator, limit) == inverse of array.join(). creates an an array separated on each occurrence of separator which can be a string or regexp. After we've created limit-1 array elements, the rest of the string is used as the last element. Empty strings are inserted if the string starts or ends with the separator but this is an unreliable edge case. 'g' flag is ignored and text from captured groups will also be included.
 - string.substring(start, end) == depreciated, use slice instead.
 - string.toLowerCase() == self explanatory
 - string.toUpperCase() == self explanatory
 - String.fromCharCode(charCode...) == produces a string from a series of numbers representing code points. Note: this is a method to be called on the String prototype.

# Style
---

 - Indention is 4 spaces unless that would be ambiguous ie after a line break in an if condition in which cases 8 spaces are used.
 - Whitespace around all operators except . and [
 - Only omit a space between something and ( when invoking a function.
 - Spaces after colons + commas
 - Only one statement per line! aka semicolons should be followed by a line break.
 - always use {blocks} with statements like if, while, and for.
 - Don't duplicate knowledge in comments, they should add new info. Keep comments up to date, bad comments can be worse than no comments.
 - Not style, necessary: { must be at the end of the line instead of on it's own line. This avoids a horrible design blunder regarding the return statement.


# Bad & Awful Parts
---

 - Global Variables... unlike most languages, JS doesn't just allow global variables. It requires them. Mitigate the risks by being careful to always declare variables (undeclared variables are global by default), and minimize the declaration of variables outside of a function. It is suggested that you declare a global object and ONLY attach global variables to this object so that it is very clear which variables are intended to be global.
 - Scope... despite using block syntax, JS does not provide block scope. Declare all variables at the top of the function to clarify which scope each variable belongs to.
 - Semicolon Insertion... Do not depend on automatic semicolon insertion! Especially make sure 'return' is never on it's own line, at least start the return statement on the same line.
 - Reserved Words... avoid them.
 - Unicode... JS interprets unicode characters above 16 bits to be two separate characters as the JS char type is 16 bits. The basic multilingual plane is covered though so I'm not worried about this.
 - typeof... typeof null returns 'object'... that's not good. if you want to know whether something's an object, you'll have to check truthiness in addition to typeof.
 - parseInt... always supply the radix parameter to avoid any strange input interpretations
 - +... either concatenates or adds. Be careful when using this operator, if you want to add then both parameters must be numbers. this is also true of +=
 - Floating Point... 0.1 + 0.2 is not exactly equal to 0.3 but integer arithmetic is exact. So scale up (ie do arithmetic for money in cents instead of dollars) to avoid weird results ie multiply everything by 1000 before calculations then divide by 1000 afterwards.
 - NaN... typeof NaN is 'number' and NaN does not equal itself. NaN in any arithmetic operation will return Nan. isNaN() and isFinite() are good ways to test for valid numbers.
 - Phony Arrays... relatively inefficient and typeof an array returns 'object'. The arguments object is a weird object/array hybrid so be careful with that one. see ./arrays.js for a good way to test for arrays
 - Falsy Values... there are 6 falsy values, memorize them: 0, '', NaN, false, null, undefined.
 - hasOwnProperty... it's method instead of an operator so be careful not to overwrite it.
 - Object... objects are never truely empty because of inheritance from their prototype chain. Make liberal use of hasOwnProperty()
 - ==... evil. Makes unpredictable type assignments to return unintuitive values. Always use === and !==
 - with statement... can potentially save you a couple lines of code but that comes at the cost of inconsistency. the result can change from one running of the program to the next and even at different points withing one execution. Just don't use it.
 - eval... compromises the security of your application as it provides direct access to the compiler. The Function constructor is similarly evil as are setTimeout and setInterval when string arguments are passed.
 - continue... similar downfalls as goto, your code will be cleaner if you refactor it to not need continue.
 - switch fall through... very very easy to miss bugs within clever uses of switch-case fall through. Slightly more verbose, bug free code is better.
 - block-less statements... The space saved by omitting brackets in single line for/while loops is a small price to pay for code that clearly does what you want it to.
 - ++/--... too clever and compact. Spread your code out a little bit so you can really see and understand what you've written. benefits don't outweigh the risks.
 - bitwise operators... these are NOT at all close to the hardware. They require type conversions so are inefficient. Besides, javascript is very rarely used to do bit manipulation.
 - function statement vs function expression... use function statements "var foo = function () {};" instead of function expressions "function foo() {}" as it clarifies that foo is a variable. Function expressions are hoisted to the top to allow sloppiness, that's not at all necessary.
 - typed wrappers... Don't use new Boolean() or new Number() or new String() or new Array() or new Object(). They are entirely unnecessary and the latter two are better replaced with [] or {}.
 - new... if you forget to use new with constructors that expect the new prefix, global variables with by clobbered with no warning whatsoever. By convention, constructors should be capitalized as a warning to always use new but a safer option is to just not use new at all.
 - void... not useful, don't use it.
