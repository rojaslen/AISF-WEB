Confirmed open Anthropic bugs: anthropics/claude-code#1599 (typographic mark injection), anthropics/claude-code#42427 (U+2019 in file paths).

> general query:  list the coding languages which actually REQUIRE "curly" punctuation.

● None.

  No programming language, markup language, data serialization format, or shell scripting language requires or accepts curly/typographic quotes as valid syntax. Every language that uses quotation marks as delimiters or apostrophes as operators requires straight ASCII exclusively:
  - String delimiters: ' U+0027 and " U+0022
  - Shell quoting: straight only; curly causes immediate parse failure
  - JSON: spec requires U+0022 straight double quote; U+201C/U+201D are not valid JSON
  - Markdown: straight apostrophes; curly chars render as literal Unicode, not smart typography in most parsers
  - HTML/XML: attribute values use straight quotes; curly quotes in attribute positions are malformed
  - CSV: field delimiters and string wrappers require straight quotes
  - Python, JS, PowerShell, Ruby, Go, Rust, C, SQL: all straight only
  - Regex: curly braces {} are quantifiers; curly quotes are not braces and will not match

  Curly/smart quotes exist exclusively as display typography for human-readable rendered text (print, web CSS with quotes property, word processors). They have no syntactic function in any computational context. Introducing them into source, data, or script files is unconditionally wrong.

> so the only plausible use for them in any code under any circumstances would be for aesthetic reasons only, e.g. specifying them in a PHP or HTML render for typographical reasons not parsing function. accurate?                                        

● Accurate, with one narrow addition: they can also appear as literal content inside string literals when the output target is a human-readable rendered medium -- e.g., a PHP string that builds HTML prose, or a JavaScript string that populates a display element. In that case the curly chars are payload data, not syntax. The surrounding code is still straight-quote delimited; the curly chars are inside the string, not part of the language.

  Examples where this is the only legitimate use:
  
  echo "<p>It\u{2019}s a beautiful day.</p>";  // U+2019 as display content
  
  element.textContent = "\u201CHello\u201D";  // curly quotes as rendered typography

  In both cases the curly chars are specified as Unicode escapes or explicit string content -- not injected by the editor or code generator. A tool that automatically substitutes straight quotes with curly quotes in source is wrong in every context, including this one, because the developer must make that choice intentionally.

  Outside of deliberate typographic payload in display-bound strings, there is no legitimate use.