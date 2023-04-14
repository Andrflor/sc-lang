import 'dart:convert';
import 'dart:io';

abstract class Tokens {
  static const VOID = 'void';
  static const BOOL = 'bool';
  static const CHAR = 'char';
  static const BYTE = 'byte';
  static const U8 = 'u8';
  static const I8 = 'i8';
  static const F8 = 'f8';
  static const U16 = 'u16';
  static const I16 = 'i16';
  static const F16 = 'f16';
  static const GLYPH = 'glyph';
  static const U32 = 'u32';
  static const I32 = 'i32';
  static const F32 = 'f32';
  static const U64 = 'u64';
  static const I64 = 'i64';
  static const F64 = 'f64';
  static const SIZE = 'size';
  static const USIZE = 'usize';
  static const TYPE = 'type';
  static const NULL = 'null';
  static const SEMICOLON = ';';
  static const PIPE_FORWARD = '|>';
  static const ARROW = '->';
  static const ASTERISK = '*';
  static const SLASH = '/';
  static const PLUS = '+';
  static const MINUS = '-';
  static const AMPERSAND = '&';
  static const LOGICAL_AND = '&&';
  static const COLON = ':';
  static const LOGICAL_OR = '||';
  static const DOUBLE_SLASH = '//';
  static const COMMENT_START = '/*';
  static const COMMENT_END = '*/';
  static const TILDE_SLASH = '~/';
  static const TILDE_EQUAL = '~=';
  static const DOUBLE_RIGHT_SHIFT = '>>';
  static const RIGHT_SHIFT_EQUAL = '>>=';
  static const DOUBLE_LEFT_SHIFT = '<<';
  static const LEFT_SHIFT_EQUAL = '<<=';
  static const TILDE = '~';
  static const BITWISE_XOR = '~|';
  static const BITWISE_XOR_EQUAL = '~|=';
  static const VERTICAL_BAR = '|';
  static const COMMA = ',';
  static const CARET = '^';
  static const CARET_EQUAL = '^=';
  static const QUESTION_MARK = '?';
  static const PERCENT = '%';
  static const DOUBLE_QUESTION_MARK = '??';
  static const DOUBLE_QUESTION_MARK_EQUAL = '??=';
  static const NOT_EQUAL = '!=';
  static const INCREMENT = '++';
  static const DECREMENT = '--';
  static const PLUS_EQUAL = '+=';
  static const MINUS_EQUAL = '-=';
  static const ASTERISK_EQUAL = '*=';
  static const SLASH_EQUAL = '/=';
  static const TILDE_SLASH_EQUAL = '~/=';
  static const PERCENT_EQUAL = '%=';
  static const EQUAL = '=';
  static const LOGICAL_NOT = '!';
  static const DOUBLE_LOGICAL_NOT = '!!';
  static const NOT_NULL_ASSERTION = '!.';
  static const OPTIONAL_CHAINING = '?.';
  static const BANG_NOT_NULL_ASSERTION = '?!.';
  static const NOT_BANG_OPTIONAL_CHAINING = '!?.';
  static const RETURN_ON_ERROR = '!@';
  static const RETURN_ON_NULL = '?@';
  static const RETURN_ON_ERROR_OR_NULL = '!?@';
  static const RETURN_ON_NULL_OR_ERRROR = '?!@';
  static const PANIC_ON_ERROR = '!#';
  static const PANIC_ON_NULL = '?#';
  static const PANIC_ON_ERROR_OR_NULL = '!?#';
  static const PANIC_ON_NULL_OR_ERRROR = '?!#';
  static const LESS_THAN = '<';
  static const LESS_THAN_OR_EQUAL = '<=';
  static const GREATER_THAN_OR_EQUAL = '>=';
  static const GREATER_THAN = '>';
  static const EQUAL_EQUAL = '==';
  static const ELLIPSIS = '...';
  static const RANGE = '..';
  static const RANGE_EQUAL = '..=';
  static const DOT = '.';
  static const DOUBLE_QUOTE = '"';
  static const SINGLE_QUOTE = '\'';
  static const DOLLAR = '\$';
  static const UNDERSCORE = '_';
  static const HASH = '#';
  static const AT = '@';
  static const LEFT_BRACKET = '[';
  static const RIGHT_BRACKET = ']';
  static const LEFT_PARENTHESIS = '(';
  static const RIGHT_PARENTHESIS = ')';
  static const LEFT_CURLY_BRACE = '{';
  static const RIGHT_CURLY_BRACE = '}';
  static const FOR = 'for';
  static const WHILE = 'while';
  static const DO = 'do';
  static const IF = 'if';
  static const ELSE = 'else';
  static const IN = 'in';
  static const SWITCH = 'switch';
  static const DEFAULT = 'default';
  static const BREAK = 'break';
  static const CONTINUE = 'continue';
  static const CASE = 'case';
  static const MATCH = 'match';
  static const IMPORT = 'import';
  static const MUT = 'mut';
  static const RETURN = 'return';
}

void main(List<String> args) {
  if (args.length != 1) {
    print('Usage: sc <filename>');
    exit(1);
  }

  final File file = File(args[0]);
  var inputStream = file.openRead();

  inputStream.transform(utf8.decoder).listen(tokenize);
}

int line = 0;
final List<Token> tokens = [];

void tokenize(String content) {
  for (int i = 0; i < content.length; i++) {
    String char = content[i];
  }
  line++;
}

class Token {
  int line;
  int position;
  String kind;
  String? value;

  Token(
      {required this.line,
      required this.position,
      required this.kind,
      this.value});
}

class Type<T> {
  Type? fr;
  T? to;

  bool get isMapping => fr != null;
  bool get isType => false;
  bool get isTypeMap => isType && isMapping;
}

class Definition {
  String name;
  Type type;
  late String value;
  late Scope scope;

  Definition(this.name, this.type);

  @override
  bool operator ==(Object other) =>
      other is Definition &&
      other.runtimeType == runtimeType &&
      other.name == name;

  @override
  int get hashCode => value.hashCode;
}

class Scope {
  static final Scope root = Scope('');
  static Scope current = root;

  String name;
  late Scope parent;
  List<Scope> children = [];
  List<Definition> definitions = [];

  bool get isRoot => parent == this;

  Scope(this.name, [Scope? parent]) {
    this.parent = parent ?? this;
  }

  Scope push(String name) {
    final Scope scope = Scope(name, this);
    children.add(scope);
    current = scope;
    return scope;
  }

  Scope pop() {
    parent.children.remove(this);
    current = parent;
    return current;
  }

  Definition? inScope(String identifier) {
    for (final Definition definition in definitions) {
      if (definition.name == identifier) {
        return definition;
      }
    }
    if (isRoot) {
      return null;
    }
    return parent.inScope(identifier);
  }

  void define(Definition definition) {
    if (definitions.contains(definition)) {
      // TODO: figure out exceptions
    } else {
      definitions.add(definition);
    }
  }
}
