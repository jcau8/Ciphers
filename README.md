# Ciphers

### Warning!<br />
**The developers of this program shall not be held responsible for any misuse or illegal activities conducted by users of this program.**

#

Transopition (T) <br />
Reverse (R) <br />
Caesar (C) <br />
Hill (H) <br />

With the Caesar cipher you can choose what alphabets you would like to encode in. When the option "alphabetic key" appears you can type 0, 1, 2 and or 3, each of these numbers correspond to an alphabet; type "0123" for maximum encryption security, this makes use of all of the alphabets. You may get 'a' at the end of your message, this is pretty much unavoidable due to the nature of the hill cipher. The development of this program will not continue due to issues with compatibility.

<br />

> [!TIP]
> The ideal numeric key is around half of your message's length, as longer keys than that may result in text being more understandable!

<br />

## Changelog
<details open><summary><b>v2.5.2 - Apr 14, 2025</b></summary>
<ul>
  <li>Fixed many issues with hill cipher</li>
  <li>Added modulus and determinant comprime error</li>
  <li>Made ASCII alphabet comprime (may result in 'a' appearing at the end of your message)</li>
</ul>
</br>
</details>

<details closed><summary><b>v2.4.2 - Mar 9, 2025</b></summary>
<ul>
  <li>Merged pull request #9</li>
  <li>Added<code>lib.py</code></li>
</ul>
</br>
</details>

<details closed><summary><b>v2.4.1 - Feb 26, 2025</b></summary>
<ul>
  <li>Added hill cipher</li>
  <li>Converted to numpy instead of math</li>
  <li>Changed padding character</li>
  <li>Added<code>lib.py</code></li>
</ul>
</br>
</details>

<details closed><summary><b>v2.3.1 - Dec 15, 2024</b></summary>
<ul>
  <li>Added padding and decrypting will auto delete padding</li>
  <li>Added pytest</li>
  <li>Fixed #5</li>
  <li>Created .gitignore</li>
</ul>
</br>
</details>

<details closed><summary><b>v2.3.0 - Dec 07, 2024</b></summary>
<ul>
  <li>Added logging system (Set on <code>WARNING</code> by default)</li>
  <li>Merged TRC-DEBUG with TRC
  <li>Minor bug fixes</li>
  <li>Deleted <code>dev</code> branch</li>
</ul>
</br>
</details>
