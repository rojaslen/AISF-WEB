# Unicode Charmap Reference
# Windows ALT+Code / Linux CTRL+SHIFT+U+Code
# https://symbl.cc/en/unicode-table/

---

— (em dash)    Alt+0151 /

¶ (paragraph)  Alt+     /

§ (section)    Alt+0167 /

± (plus/minus) Alt+0177 /

≈ (approx.)    Alt+247 /

≠ (not equal)  / 2260

© (copyright)  Alt+0169 /

™ (trademark)  Alt+0153 /

® (registered) Alt+0174 /

---

# Debian/XFCE ALT+Code Reference

Right Alt is the Compose key.

Type this in any window: RIGHT Alt, release, then ', then e → should give é

The pattern is exactly what you asked for — consistent across every accented character, and it
works in either order, so you don't have to remember which comes first:

  ┌───────────┬─────────────────────┬───────────────┐
  │ You want  │ Press Compose, then │      Or       │
  ├───────────┼─────────────────────┼───────────────┤
  │ á é í ó ú │ ' then the letter   │ letter then ' │
  ├───────────┼─────────────────────┼───────────────┤
  │ ñ         │ ~ then n            │ n then ~      │
  ├───────────┼─────────────────────┼───────────────┤
  │ ü         │ " then u            │ u then "      │
  ├───────────┼─────────────────────┼───────────────┤
  │ à è ì ò ù │ ` then the letter   │ letter then ` │
  ├───────────┼─────────────────────┼───────────────┤
  │ ç         │ , then c            │ c then ,      │
  ├───────────┼─────────────────────┼───────────────┤
  │ ¿         │ ? then ?            │               │
  ├───────────┼─────────────────────┼───────────────┤
  │ ¡         │ ! then !            │               │
  └───────────┴─────────────────────┴───────────────┘

  Capitals work the same way — Compose ' E gives É. So your three artists are: Rubén = Compose ' e;
  Colón = Compose ' o; Santamaría = Compose ' i.

---

# HTML Copy-Pasta Templates

- GitHub Pages/Jekyll Kramdown-formatted with attributes:
  [text](https://example.com){: target="_blank" rel="noopener noreferrer" }

<img src="image.jpg" alt="text-left_inline_image-right" class="float-right">

<a href="https://example.com" target="_blank" rel="noopener noreferrer">Open in new tab</a>

<p style="font-size: x-small;">This is a paragraph of x-small text.</p>

This is <div style="font-size: x-small;">x-small text</div> inside a paragraph.



Value     Description
medium    Sets the font-size to a medium size. This is default
xx-small  Sets the font-size to an xx-small size
x-small   Sets the font-size to an extra small size
small     Sets the font-size to a small size
large     Sets the font-size to a large size
x-large   Sets the font-size to an extra large size
xx-large  Sets the font-size to an xx-large size
smaller   Sets the font-size to a smaller size than the parent element
larger    Sets the font-size to a larger size than the parent element
length    Sets the font-size to a fixed size in px, cm, etc. Read about length units
%         Sets the font-size to a percent of  the parent element's font size
initial   Sets this property to its default value. Read about initial
inherit   Inherits this property from its parent element. Read about inherit
