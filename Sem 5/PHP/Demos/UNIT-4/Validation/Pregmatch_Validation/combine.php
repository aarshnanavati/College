preg_match() is very powerful tool that validate many kinds of input.
Some validation examples in PHP:

1. Validate Username (letters, numbers, underscores, 3–16 chars)
if (preg_match("/^[A-Za-z0-9_]{3,16}$/", $username))
{ 
   echo "Valid username";
} 

else 
{
   echo "Invalid username";
}

Examples:
 bharti_99, User123
 ab (too short), hello@123 (invalid char)


2. Validate Mobile Number (10 digits only)
if (preg_match("/^[0-9]{10}$/", $mobile)) {
    echo "Valid mobile number";
} else {
    echo "Invalid mobile number";
}

Examples:
 9876543210
 98765-43210, 1234
 

3. Validate Postal PIN Code (India, 6 digits)
if (preg_match("/^[1-9][0-9]{5}$/", $pincode)) {
    echo "Valid PIN code";
} else {
    echo "Invalid PIN code";
}

Explanation:
/ ... / → Pattern is written between forward slashes.

^ → Start of the string.

[1-9] → First digit must be between 1 and 9 (so it cannot start with 0).

[0-9]{5} → Next 5 digits can be anything from 0 to 9.

{5} means exactly 5 times.

$ → End of the string.

 Examples:
 380015
 012345 (can’t start with 0), 123


4. Validate Date (DD-MM-YYYY format)
if (preg_match("/^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-[0-9]{4}$/", $date)) {
    echo "Valid date";
} else {
    echo "Invalid date";
}
Explanation
^ → Start of the string.

(0[1-9]|[12][0-9]|3[01])

This matches the day part (DD).

0[1-9] → 01 to 09

[12][0-9] → 10 to 29

3[01] → 30 or 31
So valid days = 01 to 31

- → Hyphen separator.

(0[1-9]|1[0-2])

This matches the month part (MM).

0[1-9] → 01 to 09

1[0-2] → 10, 11, or 12
 So valid months = 01 to 12

- → Another hyphen separator.

[0-9]{4}

This matches the year part (YYYY).

Exactly 4 digits (0000–9999).

$ → End of the string.
Examples:
 25-12-2025
 32-01-2025, 2025-12-25


5. Validate URL
if (preg_match("/\bhttps?:\/\/[A-Za-z0-9.-]+\.[A-Za-z]{2,}(\/\S*)?/", $url)) {
    echo "Valid URL";
} else {
    echo "Invalid URL";
}

Examples:
https://example.com, http://openai.com/blog
ftp://file.com, example

