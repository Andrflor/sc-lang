#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 256

typedef enum { STRUCT, UNION, TYPEDEF } DefinitionType;

#define SKIP_WHITESPACE                                                        \
  while (line[i] == ' ' || line[i] == '\t') {                                  \
    i++;                                                                       \
  }

#define ALPHA                                                                  \
  (((line[i] >= 'a') && (line[i] <= 'z')) ||                                   \
   ((line[i] >= 'A') && (line[i] <= 'Z'))) ||                                  \
      line[i] == '_'

#define START_WITH_TYPEDEF strncmp(&line[i], "typedef", 7) == 0
#define START_WITH_STRUCT strncmp(&line[i], "struct", 6) == 0
#define START_WITH_UNION strncmp(&line[i], "union", 5) == 0

#define NEW_LINE new_line()

#define ERROR(string)                                                          \
  fprintf(                                                                     \
      stderr,                                                                  \
      "\033[1m%s:%i:%i: \033[31merror:\033[0m %s\n    %i |    %s       |\n",   \
      filename, lnum, i, string, lnum, line);                                  \
  exit(1)

#define ERROR_EXPECTED_BRACKET_SEMICOLON_EQUAL                                 \
  ERROR("expected \033[1m‘=‘\033[0m or \033[1m‘;‘\033[0m or "          \
        "\033[1m‘{‘\033[0m")

#define ERROR_NOT_PROPER_GENERIC                                               \
  ERROR("Non respected generic \033[1m<T>\033[0m or "                          \
        "\033[1m<K,V...>\033[0m syntax")

#define ERROR_NON_TERMINATED_GENERIC                                           \
  ERROR("Cannot find the closing > character")

typedef struct {
  DefinitionType type;
  char name[MAX_LINE_LENGTH];
  char parameters[MAX_LINE_LENGTH];
} Definition;

int i;
int lnum = 0;
char line[MAX_LINE_LENGTH];
char *filename;
FILE *file;

int new_line() {
  i = 0;
  lnum++;
  return fgets(line, MAX_LINE_LENGTH, file) != NULL;
}

int main(int argc, char **argv) {

  filename = argv[1];
  file = fopen(filename, "r");

  if (!file) {
    printf("Error opening file\n");
    return 1;
  }

  Definition *definitions = NULL;
  size_t numDefinitions = 0;

  while (NEW_LINE) {
    i = 0;
    SKIP_WHITESPACE;
    if (START_WITH_TYPEDEF) {
      i += 7;
      SKIP_WHITESPACE;
      if (START_WITH_STRUCT) {
        i += 6;
      } else if (START_WITH_UNION) {
        printf("typedef union\n");
        i += 5;
      } else {
        printf("typedef\n");
      }

    } else if (START_WITH_STRUCT) {
      i += 6;
      SKIP_WHITESPACE;
      while (line[i] != '\0') {
        if (line[i] == '<') {
          i++;
        token_loop:
          SKIP_WHITESPACE;
          if (!ALPHA) {
            ERROR_NOT_PROPER_GENERIC;
          }
          while (ALPHA) {
            // TODO: add the keys
            i++;
          }
          SKIP_WHITESPACE;
          if (!ALPHA) {
            if (line[i] == '>') {
              i++;
              goto token_next;
            }
            if (line[i] == ',') {
              i++;
              goto token_loop;
            }
            if (line[i] == '\n') {
              ERROR_NON_TERMINATED_GENERIC;
            }
            ERROR_NOT_PROPER_GENERIC;
          }
        }
        i++;
      }
      continue;
    token_next:
      SKIP_WHITESPACE;
      if (line[i] == '{') {
        if (NEW_LINE) {
          // TODO: parse the content
        } else {
          ERROR_EXPECTED_BRACKET_SEMICOLON_EQUAL;
        }
      } else if (line[i] == '\n') {
        if (NEW_LINE) {
          goto token_next;
        } else {
          ERROR_EXPECTED_BRACKET_SEMICOLON_EQUAL;
        }
      } else if (line[i] == ';') {
        // TODO: parse as expanding
        // TODO: and multiple int a,b; syntax
        // TODO: parse nested tokens <List<int>, v>
        // TODO: parse assignent struct test = {};
      } else {
        ERROR_EXPECTED_BRACKET_SEMICOLON_EQUAL;
      }

    } else if (START_WITH_UNION) {
      i += 5;
      SKIP_WHITESPACE;
      printf("Union:\n");
    } else {
      printf("Neither struct nor typedef nor union");
    }
  }
  fclose(file);

  return 0;
}
