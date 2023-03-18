TODO: explain how monad works in it
TODO: document autofree
TODO: better control-flow example
TODO: add a bit better explanation to |> operator

The journey to create Syntact began with a deep sense of disappointment about the state of modern programming.
We put a lot of effort into creating encapsulations, but then we end up writing a lot of code just to get around them, and it feels like there's no real purpose to them.
With all the technological advancements we have, we should be able to create applications that run incredibly fast and smoothly, but instead, we're constantly dealing with frustratingly slow programs and artificial boundaries imposed by frameworks upon frameworks.
It's clear that the current programming languages are inadequate, and we need to develop new ones that prioritize both expressiveness and high-order programming capabilities without compromising performance.
That's why I believe that Syntact is a step in the right direction, with its emphasis on flexibility, efficiency, and simplicity, making it a more powerful tool for developers to create expressive and efficient code.

The current state of programming languages is inadequate in terms of expressiveness and high-order programming capabilities.
Despite incorporating genericity, most languages require an excessive amount of boilerplate code for simple memory operations and fail to match C's level of performance while restricting the extent of genericity.
Although some languages attempt to address these issues with zero cost abstraction ownership systems like Rust, they end up with narrow and constrained syntax and ultra-slow compile time.
On the other hand, others rely on garbage collection, which incurs a hidden performance cost.
Therefore, there is a need to develop a new language that meets these requirements without compromising performance.

At its core, Syntact is built around the idea that programming is simply the act of manipulating data.
In this sense, functions and types are themselves just data that can be manipulated like any other.
Syntact leverages this fundamental concept by providing a type algebra that allows developers to easily compose complex types using operators.
By treating functions and types as data that can be freely manipulated, Syntact provides developers with a more flexible and powerful toolset for creating expressive and efficient code.
By emphasizing a functional programming style and avoiding the need for classes, Syntact helps developers to create more readable and maintainable code that is easier to reason about.

Moreover, Syntact's efficiency and simplicity are enhanced by its use of autofree memory management, which eliminates the need for garbage collection. (See the autofree section for more details)
Additionally, the language is efficiently compiled to C89, making it highly portable and compatible with a wide range of platforms.
This, combined with its fast compilation times, makes Syntact a joy to use and helps to facilitate rapid development and experimentation.

Syntact programing language features overview
  - General purpose programming languages
  - Compiles to c and focuses on genericity and expressiveness
  - Uses the |> operator to chain functions.
  - Uses monads to handle null-values, errors, and other scenarios.
  - Does not allow hidden control-flow or jumps
  - Compiles fast
  - Manage memory at compile time using autofree
  - Algebraic data types to express type structure
  - Type safe structural typing for maximum flexibility and genericity

Very simple hello world:
  main: void -> void = println("Hello world");

As you can see a Syntact program use a main function as it's enty point
The function is define with a type void -> void, meaning that it goes from void to void
Because it's coming from void you don't need parenthesis, and because the function is a single line you can use = instread of {
More on that later

The compiled c code is efficent and lightweight
For example this hello world would compile to that simple c
  int main(void) {
    printf("Hello world\n");
    return 0;
  }

In Syntact, the primitive types are:
  void: nothing
  bool: true or false
  char: 8 bit signed character
  byte: unsigned 8 bit
  u8: unsigned 8 bit integer
  i8: signed 8 bit integer
  f8: 8 bit floating point number
  u16: 16 bit unsigned integer
  i16: 16 bit signed integer
  f16: 16 bit floating point number
  glyph: 32 bit unicode character
  u32: 32 bit unsigned integer
  i32: 32 bit signed integer
  f32: 32 bit floating point number
  u64: 64 bit unsigned integer
  i64: 64 bit signed integer
  f64: 64 bit floating point number
  size: architecture number of bit signed
  usize: architecture number of bit unsigned
  type: used for type definition

In Syntact we don't talk about variable but we talk about data
This choice is due to the fact that unless specified data is immutable by default
Calling immutable data "a variable" makes no sense
Everything that exist in syntact is refered as data

To define any new data (or new variable in other programing languages)
  You can use equal sign
    data_name: data_type = data_value;

  As you can see you put the name then use : to pass the type and then = to assign the value
  As you can see statement end with ; this is a choice to allow faster compilation
  Don't worry in a few days it will become a psychomotor reflex.

  You can also use curly braces with implicit return
    data_name: data_type {
        // Any kind of process
        data_value
    }

  As you can see i used // to define a comment
  Multiline comments are also suported with /* multiline comment */

  Using curly brase is well suited when you have a lot of operations to de before assignement
  Especially if you want to create variable that belong to that particular scope
  It's also well suited to define functions with multiple instructions

  You can also use curly braces with explicit return
    data_name: data_type {
        // Any kind of process
        return data_value;
    }

  This can be particulary useful when implicit return cannot work because of control-flow for example
  In syntact functions and types are first class citizens
  And the syntax is the consistant same no matter what you want to define

  You may want to define mutable data
  you can use the keyword mut to do so

  mut data_name : data_type = data_value;

  This will allow you to modify the data
  Otherwhise you will not be able to make any modifications

In programing any type that you manipulate is nothing more than the composition of particular type
most programming language offert you various syntaxes to achieve particular compositions
In syntact you don't need those special declarations and keywords like function, enum, typedef, struct, class...
To achieve type composition Syntact rely solely on type algebra
The idea of type algebra is that type is data and like any other data you can compose types using operators

In programming, every type that you work with is essentially a combination of the primitive types.
Programming languages provide various syntaxes to accomplish these combinations.
In Syntact thanks to type algebra, you don't need special declarations or keywords like function, enum, typedef, struct, class...
With type algebra types are data and this allow you to compose types using operators, just like any other data.

The operators defined by Syntact to operate on types are as follow
  -> define a mapping from any type into any type
  You can use it to define functions
  main: void -> i32 = 0;
  * is the cartesian product
  You can use it to define tuples or records
  my_tuple: i32 * u8 = 2,4;
  * can also be used to create name products
  my_record: value: i32 * u8 * another: f64 = value: 3, 6, another: 4.2;
  / is the cartesian division
  i32 * u8 * u8 / u8; // i32;
  i32 * value: u8 * u8 / u8; // i32 * value: u8
  i32 * value: u8 * u8 / value: u8; i32 * u8
  i32 * value: u8 * u8 / :u8; // i32
  by using :u8 why speicify u8 with any name
  i32 * value: u8 * u8 / i32 * u8; //value: u8
  it will raise a compile time error if you try to divide something that isn't here
  + is the summation
  It allow to fusion two types
  animal: type = name: glyph^ * age: u32;
  pet: type = animal + owner: glyph^;
  type summation is different than product
  animal * owner: glyph^;
  animal + owner: glyph^; // (name: glyph^ * age: u32 * owner: glyph^)
  With + animal is expanded directly and not use as a field type
  - is the substraction
  It allow to remove property from type
  animal: type = pet - owner: glyph^;
  it will raise a compile time error if you try to remove something that isn't here
  i32 * u8 * u8 - u8; // i32 * u8;
  you can also use - :u8 that will remove the last u8 no matter the name
  & is the intersection operator
  animal: type = name: glyph^ * age: u32;
  pet: type = animal + owner: glyph^;
  person: type = name: glyph^ * age: u32;
  animal & pet & person; // (name: glyph^ * age: u32)
  | is a either
  data: i32 | f64 = 3.2;
  meaning that data is either i32 or f64
  you can than use a match statement to dispatch cases
  you can also use that as function entry type for generic implementation
  , is an enumeration
  symbol: type = glyph, char;
  This mean that symbol is a new type that contains two elements glyph and char
  This is particulary helpful when you want to have constrained genericity
  ^ is the cartesian power
  for example i32^3 is i32*i32*i32
  But ^ can also be used with ranges
  for example i32^1..3 means from one to 3 i32
  ^ can also specify infinite range
  i32^3.. range from 3 to infinity
  i32^ can be use as a shorthand for i32^0..
  ^ operator can also be used with 3 types
  in that case f64^glyph for example would mean
  f64 indexed by a gplyh same as a map with f64 value and glyph keys
  ? is the operator for the optional
  data: ?u8; here data is null so we need to define it with ?
  = is used for default value
  defaulted: type = u8 * u8 = 22 * value: glyph^ = "somestring" * ?u16=;
  You can omit the value the field is equal on some types
  optional will default to null, strings to "" and the other default type to 0
  This can be pretty practical especially to define a function that have optional arguments
  Default values can lead to ambiguity and unexpected behavior, so they should be used with caution.
  ! is the operator for the Error
  This is a shorthannd for Error | T where T is a type
  data: !u8 = 3;
  This mean that data may be error or u8
  < <= >= > == != are used to compare types
  == allow to check if two types are the same
  != allow to check if two types differ
  < and <= allow to check if a type is a (strict or not) subtype of another
  > and >= allow to check if a type is a (strict or not) supertype of another

More on cartesian proudct
  To access a cartesian product member you can specify the name
  or you can specifty the field number with $
  Example:
    record_type: type = value: i32 * u8 * another: f64;
    my_record: record_type = value: 3, 6, another: 4.2;
    my_record.$1 // This is the first unamed member (6)
    my_record.value // This is the `value` member (3)
  You can also destucture product types:
    value: i32, unamed: u8 , another: f64 = my_record;
    unnamed; // 6
    value; // 3
    another; // 4.2
  You can also use _ or .. for destructuring
    .., another: f64 = my_record;
  is equivalent to
    _, _, another: f64 = my_record;
  In addition product types that are a product of same size types
  can be accessed by index
    three_same_size: type = f64 * tagged: i64 * u64;
    data: three_same_size = 3.2, 18, tagged: -12;
    data[1]; // second member (-12)
  Note that the index is the index of the structure not of the assignement

More on functions
  When you define a function you may want to use the parameter
  To do do simply use the syntax
    process(data): u8 -> u8 = data - 3;
  You can also use product type in functions
    process(data, another): u8 * i16 -> i16 = data + another;
  Or you can do the same without destructuring data
    process(tuple): u8 * 16 -> i16 = tuple.$1 + tuple.$2;
  You can of course use function to define type
    morphism(T): type -> type = T -> T;
  That mean that morphism(u8) is u8 -> u8;
    mapping(T1,T2): type -> type = T1 -> T2;
    array(T, length): u8 -> type = T^length;
  This is very cool for generic types

Contol flow
  Like many other programing languages syntact allow to use of control
  Those are like in most programing languages
  for, while, if, else , else if, ternary, switch and match
  The match statement is particulary helpful as an exhaustive variant of switch

The piping |> operator
  |> is the piping operator it allow to pass a function directly passing the left as first argument
  This is similar to the syntax of elixir
  process(data): u8 -> u8 = data + 3;
  transform(data): u8 -> u8 = data*2;
  number: u8 = 10;
  new_num : u8 = number |> process |> transform; // same as transform(process(data))
  The |> operator allow you to define function without having to use parameters
  prcoess_transform: u8 -> u8 = process |> transform;
  Note that this can also be used with default operators
  addthree: u8 -> u8 = +3;
  second: u8^ -> u8 = [2];
  The |> operator can also be used for partial call
    f: T1 -> T2 = // Do something
    data: T3 = // Some definition
    data |> f; // Work only if T3 & T1 = T1
  The |> operator also allow for monadic operations
  For example using the error monad
  process(data): u8 -> !u8 = data < 3 ? Error("Underflow") : data -3;
  new_num : !u8 number |> process |> transform;  // same as transform(process(data))
  Notice that new_num is of type !u8 because if an error occur it will be passed to it before transform is called
  You can do the exact same with null and the ? monad
  Indeed you can also use that behavior with any monad
  You may also want to return early or panic instead of the default behavior
  @ is used to return
  new_num : u8 number |> process !@|> transform;
  note that new_num is now u8 again thanks to the return
  the return type of the function should be u8!
  If you return in main like that in main the program will panic instead
  Note that you can also return something else
  nope: char^ = "Nope";
  new_num : u8 number |> process !@nope|> transform;
  This time the return type of the function should be char^
  In other context you may want to panic
  # is used to return
  new_num : u8 number |> process !#|> transform;
  By default it will panic with the error
  On the optional monad it will panic with expected non null but got null
  As for @ you can also specify a value for the panic
  new_num : u8 number |> process !#Error("Calm down bill")|> transform;
  You can also have a function that takes multiple argument and pipe it
  imagine a map function
  map(data, op): u8^* (u8 -> u8) -> u8^ = for(elt: u8 in data) op(elt);
  Then you can use it like so to get same results
  array: u8^ = 2,4,3,65,7;
  addthree: u8 -> u8 = +3;
  array |> map addthree;
  array |> map +3;
  array, addthree |> map;
  array, +3 |> map;
