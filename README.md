# sywtltc_chapter_3_5
Types and Typeful programming

You're helping your fellow programmer Brad to figure out a project your tech lead Susan gave you.

Brad needs to put together some simple business logic to figure out how to charge fees for members. He's
put the business logic in some of the doc strings.

Susan has said that this project must treat input strings carefully and ensure there's no SQL in them.
She has said that she'll be procuring an actual validation function, but for now, Brad threw one together
as a place holder.

Brad recently learned about assertions and thinks its a good way to enforce that no potential SQL gets
into any of the strings. After getting to a certain point, though, he has found it a bit cumbersome.

He's also running into a bug now that he's live testing.

Can strong types help here? Specifically, what if there was a user ID and safe_string objects? Could
a safe_string object simply validate SQL once, and then the type system can enforce that only safe strings
are passed?

Can a user ID type help figure out whats going on in the business logic? And/or maybe a strong type for Age,
or name?

Add types and type decorations. Create classes, and add validation to the safe_string class you'll create.
See if using a class for that kind of validation makes things a little less cluttered.

Ensure everything is pylint clean (as possible, sometimes pylint complains about too few methods on objects.
We'll ignore that for now), and add unit tests. Brad has been live testing, but you know that to make
testing fast, its best to make automated unit tests so a person doesn't have to type things in.
