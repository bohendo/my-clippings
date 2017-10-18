
---
#  Ruby on Rails
## by Michael Hartl
---

 - loc 490 - technical sophistication: the combination of hard and soft skills that make it seem like you can magically solve any technical problem

 - loc 496 - Because web applications have so many moving parts, they offer ample opportunities to develop your technical sophistication.

 - loc 788 - using two spaces for indentation is a near-universal convention in Ruby,

 - loc 909 - since the structure is common to all Rails apps, you can immediately get your bearings when looking at someone else’s code.

 - loc 1029 - the >= notation always installs the latest gem, whereas the ~> 4.0.0 notation only installs updated gems where the last digit differs (e.g., from 4.0.0 to 4.0.1), but the digits before that releases (e.g., from 4.0 to 4.1).

 - loc 1029 - the >= notation always installs the latest gem, whereas the ~> 4.0.0 notation only installs updated gems where the last digit differs (e.g., from 4.0.0 to 4.0.1),

 - loc 1372 - repositories while charging for private repos, whereas Bitbucket allows unlimited free private repos while charging for more than a certain number of collaborators.

 - loc 1373 - Bitbucket allows unlimited free private repos while charging for more than a certain number of collaborators.

 - loc 1377 - growing concerns about security have led me to recommend that all web application repositories be private by default.

 - loc 1493 - Note that we write the commit message in the present tense (and, technically speaking, the imperative mood).

 - loc 1536 - deploying early and often allows us to catch any deployment problems early in our development cycle. The alternative—deploying only after laborious effort sealed away in a development environment—often leads to terrible integration headaches when launch time comes.

 - loc 2158 - the index, show, new, and edit actions all correspond to pages from Section 2.2.1, but there are additional create, update, and destroy actions as

 - loc 2195 - “REST”, which is an acronym for REpresentational State Transfer. REST is an architectural style for developing distributed, networked systems and software applications such as the World Wide Web and web applications. Although REST theory is rather abstract, in the context of Rails applications REST means that most application components (such as users and microposts) are modeled as resources that can be created, read, updated, and deleted—operations that correspond both to the CRUD operations of relational databases and to the four fundamental HTTP request methods: POST, GET, PATCH, and DELETE.

 - loc 2240 - Variables that start with the @ sign, called instance variables, are automatically available in the views;

 - loc 2556 - both the User model and the Micropost model inherit (via the left angle bracket <) from ApplicationRecord, which in turn inherits from ActiveRecord::Base,

 - loc 2556 - both the User model and the Micropost model inherit (via the left angle bracket <) from ApplicationRecord, which in turn inherits from ActiveRecord::Base, which is the base class for models provided by Active Record;

 - loc 2960 - these two commands cancel each other out: $ rails generate controller StaticPages home help $ rails destroy controller StaticPages home help

 - loc 2970 - Migrations change the state of the database using the command $ rails db:migrate We can undo a single migration step using $ rails db:rollback To go all the way back to the beginning, we can use $ rails db:migrate VERSION=0

 - loc 3144 - When done right, writing tests also allows us to develop faster despite requiring extra code, because we’ll end up wasting less time trying to track down bugs. This is true only once we get good at writing tests, though, which is one reason it’s important to start practicing as early as possible.

 - loc 3148 - test-driven development (TDD),8 a testing technique in which the programmer writes failing tests first, and then writes the application code to get the tests to pass.

 - loc 3164 - many developers find that, as they get better at writing tests, they are more inclined to write them first.

 - loc 3168 - When a test is especially short or simple compared to the application code it tests, lean toward writing the test first. When the desired behavior isn’t yet crystal clear, lean toward writing the application code first, then write a test to codify the result. Because security is a top priority, err on the side of writing tests of the security model first. Whenever a bug is found, write a test to reproduce it and protect against regressions, then write the application code to fix it. Lean against writing tests for code (such as detailed HTML structure) likely to change in the future. Write tests before refactoring code, focusing on testing error-prone code that’s especially likely to break.

 - loc 3175 - we’ll usually write controller and model tests first and integration tests (which test functionality across models, views, and controllers) second. And when we’re writing application code that isn’t particularly brittle or error-prone, or is likely to change (as is often the case with views), we’ll often skip testing altogether.

 - loc 3240 - test-driven development involves writing a failing test first, writing the application code needed to get it to pass, and then refactoring the code if necessary. Because many testing tools represent failing tests with the color red and passing tests with the color green, this sequence is sometimes known as the “Red, Green, Refactor” cycle.

 - loc 3242 - Because many testing tools represent failing tests with the color red and passing

 - loc 3629 - (The distinction between the two types of embedded Ruby is that <% ... %> executes the code inside, while <%= ... %> executes it and inserts the result into the template.)

 - loc 3722 - using this layout ensures that, for example, visiting the page /static_pages/home converts the contents of home.html.erb to HTML and then inserts it in place of <%= yield %>.

 - loc 4394 - Ruby comments start with the pound sign # (also called the “hash mark” or (more poetically) the “octothorpe”)

 - loc 4395 - pound sign # (also called the “hash mark” or (more poetically) the “octothorpe

 - loc 4454 - nil is a special Ruby value for “nothing at all”.

 - loc 4478 - Ruby won’t interpolate into single-quoted strings:

 - loc 4491 - inside double-quoted strings, a literal backslash is represented with two backslashes.

 - loc 4529 - Note the question mark at the end of the empty? method. This is a Ruby convention indicating that the return value is boolean: true or false.

 - loc 4548 - Booleans can also be combined using the && (“and”), || (“or”), and ! (“not”) operators:

 - loc 4592 - It’s worth noting that the nil object is special, in that it is the only Ruby object that is false in a boolean context, apart from false itself.

 - loc 4592 - It’s worth noting that the nil object is special, in that it is the only Ruby object that is false in a boolean context, apart from false itself. We can see this using !! (read “bang bang”), which negates an object twice, thereby coercing it to its boolean value:

 - loc 4648 - Ruby functions have an implicit

 - loc 4648 - Ruby functions have an implicit return, meaning they return the last statement evaluated—

 - loc 4794 - Note that none of the methods above changes a itself. To mutate the array, use the corresponding “bang” methods (so-called because the exclamation point is usually pronounced “bang” in this context):

 - loc 4794 - Note that none of the methods above changes a itself. To mutate the array, use the corresponding “bang” methods

 - loc 4801 - You can also add to arrays with the push method or its equivalent operator, <<, called the “shovel operator”:

 - loc 4819 - Closely related to arrays are ranges, which can probably most easily be understood by converting them to arrays using the to_a method:

 - loc 4829 - Though 0..9 is a valid range, the second expression above shows that we need to add parentheses to call a method on it.

 - loc 4836 - use the index -1 at the end of the range to select every element from the starting point to the end of the array without explicitly having to use the array’s length:

 - loc 4874 - (1..5).each { |i| puts 2 * i }

 - loc 4880 - This code calls the each method on the range (1..5) and passes it the block { |i| puts 2 * i }. The vertical bars around the variable name in |i| are Ruby syntax for a block variable, and it’s up to the method to know what to do with the block. In this case, the range’s each method can handle a block with a single local variable, which we’ve called i, and it just executes the block for each value in the range.

 - loc 4894 - we’ll follow the common convention of using curly braces only for short one-line blocks and the do..end syntax for longer one-liners and for multi-line blocks:

 - loc 4912 - 3.times { puts "Betelgeuse!" } # 3.times takes a block with no variables.

 - loc 4915 - (1..5).map { |i| i**2 } # The ** notation is for 'power'.

 - loc 4920 - %w makes string arrays.

 - loc 4925 - %w[A B C].map { |char| char.downcase }

 - loc 5003 - Hashes are essentially arrays that aren’t limited to integer indices. (In fact, some languages, especially Perl, sometimes call hashes associative arrays for this reason.)

 - loc 5019 - pair of braces with no key-value pairs—i.e., {}—is an empty hash.

 - loc 5019 - a pair of braces with no key-value pairs—i.e., {}—is an empty hash.

 - loc 5024 - If order matters, use an array.

 - loc 5026 - “hashrocket”: >> user = { "first_name" => "Michael", "last_name" => "Hartl" }

 - loc 5026 - =>, called a “hashrocket”: >> user = { "first_name" => "Michael", "last_name" => "Hartl" }

 - loc 5031 - I’ve used the usual Ruby convention of putting an extra space at the two ends of the hash—

 - loc 5034 - Symbols look kind of like strings, but prefixed with a colon instead of surrounded by quotes. For example, :name is a symbol. You can think of symbols as basically strings without all the extra baggage:

 - loc 5066 - > h1 = { :name => "Michael Hartl", :email => "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h2 = { name: "Michael Hartl", email: "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h1 ==

 - loc 5066 - > h1 = { :name => "Michael Hartl", :email => "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h2 = { name: "Michael Hartl", email: "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h1 == h2 => true

 - loc 5066 - >> h1 = { :name => "Michael Hartl", :email => "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h2 = { name: "Michael Hartl", email: "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h1 == h2 => true

 - loc 5066 - > h1 = { :name => "Michael Hartl", :email => "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h2 = { name: "Michael Hartl", email: "michael@example.com" } => {:name=>"Michael Hartl", :email=>"michael@example.com"} >> h1

 - loc 5120 - Note that, while the each method for arrays takes a block with only one variable, each for hashes takes two, a key and a value. Thus, the each method for a hash iterates through the hash one key-value pair at a time.

 - loc 5138 - using inspect to print an object is common enough that there’s a shortcut for it, the p function:

 - loc 5184 - where are the parentheses? In Ruby, they are optional,

 - loc 5194 - When hashes are the last argument in a function call, the curly braces are optional,

 - loc 5207 - Ruby doesn’t distinguish between newlines and other whitespace

 - loc 5231 - Ruby, like many object-oriented languages, uses classes to organize methods; these classes are then instantiated to create objects.

 - loc 5247 - s = String.new("foobar") # A named constructor for a string

 - loc 5252 - This is equivalent to the literal constructor, but it’s more explicit about what we’re doing.

 - loc 5259 - While the array constructor Array.new takes an initial value for the array, Hash.new takes a default value for the hash, which is the value of the hash for a nonexistent key:

 - loc 5337 - class Word < String # Word inherits from String.

 - loc 5344 - Here Word < String is the Ruby syntax for inheritance

 - loc 5374 - inside the String class the use of self. is optional on a method or attribute (unless we’re making an assignment),

 - loc 5530 - attr_accessor :name, :email creates attribute accessors corresponding to a user’s name and email address. This creates “getter” and “setter” methods that allow us to retrieve (get) and assign (set) @name and @email instance variables,

 - loc 5536 - In Rails, the principal importance of instance variables is that they are automatically available in the views, but in general they are used for variables that need to be available throughout a Ruby class.

 - loc 5540 - The first method, initialize, is special in Ruby: it’s the method called when we execute User.new.

 - loc 5598 - initializing objects using a hash argument, a technique known as mass assignment, is common in Rails applications.

 - loc 5654 - Ruby, they’re the same thing: all methods are functions, and all functions are methods, because everything is an object.

 - loc 5654 - in Ruby, they’re the same thing: all methods are functions, and all functions are methods, because everything is an object.

 - loc 5670 - blocks are closures, which are one-shot anonymous functions with data attached.

 - loc 5863 - the first argument to link_to is the link text, while the second is the URL.

 - loc 5863 - the first argument to link_to is the link text, while the second is the URL. We’ll fill in the URLs with named routes in Section 5.3.3, but for now we use the stub URL ’#’ commonly used in web design (i.e., ’#’ is just a “stub”, or placeholder, for the real URL). The third argument is an options hash, in this case adding the CSS id logo to the sample app link.

 - loc 6091 - In other words, the dot . in .center indicates that the rule styles a class. (As we’ll see in Listing 5.9, the pound sign # identifies a rule to style a CSS id.)

 - loc 6224 - Note the leading underscore on the filename _shim.html.erb; this underscore is the universal convention for naming partials, and among other things makes it possible to identify all the partials in a directory at a glance.

 - loc 6370 - From the perspective of a typical Rails developer, there are three main features to understand about the asset pipeline: asset directories, manifest files, and preprocessor engines.

 - loc 6417 - We tell Rails which processor to use using filename extensions;

 - loc 6425 - foobar.js.erb.coffee gets run through both CoffeeScript and ERb (with the

 - loc 6425 - foobar.js.erb.coffee gets run through both CoffeeScript and ERb (with the code running from right to left, i.e., CoffeeScript first).

 - loc 6488 - In order to nest the second rule, we need to reference the parent element #logo; in SCSS, this is accomplished with the ampersand character &

 - loc 6504 - Sass changes &:hover into #logo:hover as part of converting from SCSS to CSS.

 - loc 6662 - Rails conventionally uses named routes, which involves code like <%= link_to "About", about_path %> This way the code has a more transparent meaning, and it’s also more flexible since we can change the definition of about_path and

 - loc 6662 - Rails conventionally uses named routes, which involves code like <%= link_to "About", about_path %> This way the code has a more transparent meaning, and it’s also more flexible since we can change the definition of about_path and have the URL change everywhere about_path is used.

 - loc 6786 - get '/help', to: 'static_pages#help' This new pattern routes a GET request for the URL /help to the help action in the Static Pages controller.

 - loc 7183 - As with the other routes, get ’signup’ automatically gives us the named route signup_path,

 - loc 7278 - You might notice that the img tag, rather than looking like <img>...</img>, instead looks like <img ... />. Tags that follow this form are known as self-closing tags.

 - loc 7365 - In Rails, the default data structure for a data model is called, naturally enough, a model (the M in MVC

 - loc 7365 - In Rails, the default data structure for a data model is called, naturally enough, a model (the M in MVC from Section 1.3.3). The default Rails solution to the problem of persistence is to use a database for long-term data storage, and the default library for interacting with the database is called Active Record.1 Active Record comes with a host of methods for creating, saving, and finding data objects, all without having to use the structured query language (SQL)2 used by relational databases. Moreover, Rails has a feature called migrations to allow data definitions to be written in pure Ruby, without having to learn an SQL data definition language (DDL).

 - loc 7637 - it’s often convenient to make and save a model in two steps as we have above, but Active Record also lets you combine them into one step with User.create:

 - loc 7657 - Like create, destroy returns the object in question,

 - loc 7768 - The update_attributes method accepts a hash of attributes, and on success performs both the update and the save in one step (returning true to indicate that the save went through).

 - loc 8137 - Note that we’ve included an optional second argument to the assertion with a custom error message, which in this case identifies the address causing the test to fail: assert @user.valid?, "#{valid_address.inspect} should be valid"

 - loc 8179 - The application code for email format validation uses the format validation, which works like this: validates :email, format: { with: /<regular expression>/ }

 - loc 8243 - Here the regex VALID_EMAIL_REGEX is a constant, indicated in Ruby by a name starting with a capital letter.

 - loc 8428 - Luckily, the solution is straightforward to implement: we just need to enforce uniqueness at the database level as well as at the model level. Our method is to create a database index on the email column (Box 6.2), and then require that the index be unique.

 - loc 8443 - To understand a database index, it’s helpful to consider the analogy of a book index. In a book, to find all the occurrences of a given string, say “foobar”, you would have to scan each page for “foobar”—the paper version of a full-table scan. With a book index, on the other hand, you can just look up “foobar” in the index to see all the pages containing “foobar”.

 - loc 8537 - inside the User model the self keyword is optional on the right-hand side:

 - loc 8537 - inside the User model the self keyword is optional on the right-hand side: self.email = email.downcase

 - loc 8635 - Most of the secure password machinery will be implemented using a single Rails method called has_secure_password,

 - loc 8640 - When included in a model as above, this one method adds the following functionality: The ability to save a securely hashed password_digest attribute to the database A pair of virtual attributes18 (password and password_confirmation), including presence validations upon object creation and a validation requiring that they match An authenticate method that returns the user when the password is correct (and false otherwise)

 - loc 8659 - We can choose any migration name we want, but it’s convenient to end the name with to_users, since in this case Rails automatically constructs a migration to add columns to the users table.

 - loc 9039 - course, we could just edit the migration file for the users table in Listing 6.2, but that would require rolling back and then migrating back up. The Rails Way™ is to use migrations every time we discover that our data model needs to change.

 - loc 9039 - Of course, we could just edit the migration file for the users table in Listing 6.2, but that would require rolling back and then migrating back up. The Rails Way™ is to use migrations every time we discover that our data model needs to change.

 - loc 9138 - <%= debug(params) if Rails.env.development? %>

 - loc 9164 - If you ever need to run a console in a different environment (to debug a test, for example), you can pass the environment as a parameter to the console script: $ rails console test

 - loc 9164 - If you ever need to run a console in a different environment (to debug a test, for example), you can pass the environment as a parameter to the console script: $ rails console test Loading test environment

 - loc 9168 - rails server --environment production

 - loc 9257 - We’ll follow the conventions of the REST architecture favored in Rails applications (Box 2.2), which means representing data as resources that can be created, shown, updated, or destroyed—four actions corresponding to the four fundamental operations POST, GET, PATCH, and DELETE defined by the HTTP standard

 - loc 9262 - When following REST principles, resources are typically referenced using the resource name and a unique identifier. What this means in the context of users—which we’re now thinking of as a Users resource—is that we should view the user with id 1 by issuing a GET request to the URL /users/1.

 - loc 9824 - the code type="email" will cause some mobile devices to display a special keyboard optimized for entering email addresses.)

 - loc 10090 - we’ll render an error-messages partial on the user new page while adding the CSS class form-control (which has special meaning to Bootstrap) to each entry field,

 - loc 10184 - pluralize takes an integer argument and then returns the number with a properly pluralized version of its second argument. Underlying this method is a powerful inflector that knows how to pluralize a large number of words, including many with irregular plurals:

 - loc 10294 - By wrapping the post in the assert_no_difference method with the string argument ’User.count’, we arrange for a comparison between User.count before and after the contents inside the assert_no_difference block.

 - loc 10294 - By wrapping the post in the assert_no_difference method with the string argument ’User.count’, we arrange for a comparison between User.count before and after the contents inside the assert_no_difference block. This is equivalent to recording the user count, posting the data, and verifying that the count is the same:

 - loc 10506 - The Rails way to display a temporary message is to use a special method called the flash, which we can treat like a hash.

