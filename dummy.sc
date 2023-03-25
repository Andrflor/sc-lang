Dat: type = i32 * f32;
a : Dat = 0,0;
main(): void -> i32 = 0;

main(): void -> i32 {
  a: Dat = 0, 0;
  0
}

main(args): char^ -> i32 {
  args |> map;
  args.length;
}

test(): void -> i32 = 0;


f(x): i32 -> ?f32 = x == 0 ? null : 1/x;
g(x): f32 -> i32 = (i32)x;

gf: i32 -> ?i32 = f |> g;
main(argc, argv): i32 * char^ -> i32 = argc |> gf ?? 0;

main(argc, argv): i32 * char^ -> i32 = argc |> f |> g ?? 0;


sum_of_squares(n): i32 -> i32 {
  helper(i, acc): i32 * i32 -> i32 =
    i > n ? acc :
    helper(i+1, acc + (i*i));
  helper(1, 0)
}

average(nums): f32^ -> f32 =
  (nums |> fold(0.0, (+))) / (nums |> length |> f32);

reciprocals(nums): i32^ -> (?f32)^ =
  nums |> map((x) = x == 0 ? null : 1.0 / x);

main(argc, argv): i32 * char^ -> i32 {
  n: u32 = argv[1] |> parse_int;
  s: u32 = n |> sum_of_squares;

  nums: f32^ = [1.0, 2.0, 3.0, 4.0, 5.0];
  avg: f32 = nums |> average;

  ints: u32^ = [1, 2, 3, 4, 5];
  recip: (?f32)^ = ints |> reciprocals;

  println("Sum of squares from 1 to $n: $s");
  println("Average of array $nums: $average");
  println("Reciprocals of array $ints: $recip");
  0
}

num: type = i32 | f32;
morph(T): type -> type = T -> T;
bimorph(T): type -> type = T * T -> T;
manymorph(i, T): i32 * type -> type = T^i -> T;
anymorph(T): type -> type = T^ -> T;

f(x): morph(num) = x+3;
g(x,y): bimorph(num) = x+y;
h(x,y,z,a,b,c): manymorph(6, num) = x+y+z+a+b+c;
i(x): anymorph(num) = ......;
i(x): num^ -> num = ......;

even: type = x: u8, x%2==0;
palindrome: type = x: String, x == x |> reverse;

process_palin(x): palindrome -> String {
  "Process done"
}

m : u32 = 22;
s: String = "Some String";

main(): void -> i32 {
  if(m==10) {
    s >= palimdrom ? s |> process_palin |> print : print("Not palindrom");
  }
  0
}

minmaxgcd: i32^ -> i32 = (min,max)|>gcd;
minmaxgcd(x): i32^ -> i32 = (x|>min, x|>max)|>gcd;
minmaxgcd(x): i32^ -> i32 = gcd(min(x), max(x));


mapping(x, y): type * type -> type = x->y;

data: type = u8 * (u8 | f32) * u32
val : data = 0, 0, 0;

type1: type = u8 * value: i32 * count: i32;
type2: type = f32 * count: i32 * double;

data: type = type1 & type2; // count: i32;
