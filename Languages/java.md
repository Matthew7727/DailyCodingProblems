```java
byte b = 10;      // 8-bit signed integer
short s = 20;     // 16-bit signed integer
int i = 30;       // 32-bit signed integer
long l = 40L;     // 64-bit signed integer

float f = 3.14f;  // 32-bit floating point
double d = 3.14;  // 64-bit floating point

char c = 'A';     // 16-bit Unicode character

boolean bool = true;  // boolean type

String str = "Hello, World!";

// Accessing Characters
char firstChar = str.charAt(0);  // 'H'
char lastChar = str.charAt(str.length() - 1);  // '!'

// Common Methods
String lowerStr = str.toLowerCase();  // "hello, world!"
String upperStr = str.toUpperCase();  // "HELLO, WORLD!"
String trimmedStr = str.trim();  // Removes surrounding whitespace
String replacedStr = str.replace("Hello", "Hi");  // "Hi, World!"
String[] splitStr = str.split(", ");  // ["Hello", "World!"]
String joinedStr = String.join(",", "a", "b", "c");  // "a,b,c"

// Checking Content
boolean startsWith = str.startsWith("He");  // true
boolean endsWith = str.endsWith("!");  // true
boolean isAlpha = str.matches("[a-zA-Z]+");  // false (includes non-alphabetic characters)
boolean isDigit = str.matches("\\d+");  // false (not only digits)
boolean isAlnum = str.matches("[a-zA-Z0-9]+");  // false (not alphanumeric)

// Array Creation
int[] arr = {1, 2, 3, 4};

// Accessing Elements
int firstElem = arr[0];  // 1
int lastElem = arr[arr.length - 1];  // 4

// Common Methods (via Arrays class)
import java.util.Arrays;
Arrays.sort(arr);  // Sorts the array in place
int index = Arrays.binarySearch(arr, 3);  // 2 (index of the element 3)
int[] copiedArr = Arrays.copyOf(arr, arr.length);  // [1, 2, 3, 4]

import java.util.ArrayList;
import java.util.List;

// List Creation
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4));

// Accessing Elements
int firstElem = list.get(0);  // 1
int lastElem = list.get(list.size() - 1);  // 4

// Common Methods
list.add(5);        // [1, 2, 3, 4, 5]
list.addAll(Arrays.asList(6, 7));  // [1, 2, 3, 4, 5, 6, 7]
list.remove(Integer.valueOf(3));  // [1, 2, 4, 5, 6, 7]
list.clear();       // Clears the list

// Checking Content
boolean contains = list.contains(3);  // false
int index = list.indexOf(3);  // -1 (not found)

import java.util.HashMap;
import java.util.Map;

// Map Creation
Map<String, Integer> map = new HashMap<>();
map.put("name", 25);

// Accessing Elements
int value = map.get("name");  // 25
int defaultValue = map.getOrDefault("address", 0);  // 0

// Common Methods
map.put("age", 26);  // Updates the map
map.remove("name");  // Removes the entry for 'name'
map.clear();  // Clears the map

// Checking Content
boolean containsKey = map.containsKey("age");  // true
boolean containsValue = map.containsValue(26);  // true

import java.util.HashSet;
import java.util.Set;

// Set Creation
Set<Integer> set = new HashSet<>(Arrays.asList(1, 2, 3, 4));

// Common Methods
set.add(5);            // [1, 2, 3, 4, 5]
set.addAll(Arrays.asList(6, 7));    // [1, 2, 3, 4, 5, 6, 7]
set.remove(3);         // [1, 2, 4, 5, 6, 7]
set.clear();           // Clears the set

// Checking Content
boolean contains = set.contains(3);  // false

// Set Operations
Set<Integer> a = new HashSet<>(Arrays.asList(1, 2, 3));
Set<Integer> b = new HashSet<>(Arrays.asList(3, 4, 5));

Set<Integer> union = new HashSet<>(a);
union.addAll(b);  // Union: [1, 2, 3, 4, 5]

Set<Integer> intersection = new HashSet<>(a);
intersection.retainAll(b);  // Intersection: [3]

Set<Integer> difference = new HashSet<>(a);
difference.removeAll(b);  // Difference: [1, 2]

Set<Integer> symmetricDifference = new HashSet<>(union);
symmetricDifference.removeAll(intersection);  // Symmetric Difference: [1, 2, 4, 5]

if (condition) {
    // code
} else if (anotherCondition) {
    // code
} else {
    // code
}

// For Loop
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// While Loop
int i = 0;
while (i < 5) {
    System.out.println(i);
    i++;
}

// Do-While Loop
int j = 0;
do {
    System.out.println(j);
    j++;
} while (j < 5);

// Loop Control
for (int k = 0; k < 5; k++) {
    if (k == 3) {
        break;       // Exit loop
    }
    if (k == 2) {
        continue;    // Skip to next iteration
    }
    System.out.println(k);
}

import java.util.Collections;
import java.util.List;

// List of Numbers
List<Integer> numbers = Arrays.asList(4, 1, 7, 3);
int max = Collections.max(numbers);  // 7
int min = Collections.min(numbers);  // 1

// List of Strings
List<String> words = Arrays.asList("apple", "banana", "cherry");
String maxStr = Collections.max(words);  // "cherry"
String minStr = Collections.min(words);  // "apple"

import java.util.Arrays;

// Array of Numbers
int[] numArray = {4, 1, 7, 3};
int max = Arrays.stream(numArray).max().getAsInt();  // 7
int min = Arrays.stream(numArray).min().getAsInt();  // 1

// Array of Strings
String[] strArray = {"apple", "banana", "cherry"};
String maxStr = Arrays.stream(strArray).max(String::compareTo).get();  // "cherry"
String minStr = Arrays.stream(strArray).min(String::compareTo).get();  // "apple"



