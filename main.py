#!/usr/bin/env python3
"""Entry program for "One-Liner Laugh Lab" (make.fun).

Writes one short funny line to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The line must be 1 to 200 characters of UTF-8 text.

Candidate one-liners drafted for this entry (first pass):
  1. Scientists say the universe keeps expanding, which finally
     explains why nothing in my apartment stays where I left it.
  2. My goldfish forgets me every ten seconds, so every lap of
     its bowl is a gap year abroad with a brand-new landlord.
  3. An octopus has three hearts and still plays it cool; I have
     one heart and it panics at a text.
  4. Evolution spent 3.8 billion years making me, and I spend
     most of that inheritance rehearsing arguments in the shower.
  5. I set my clock five minutes fast to be on time, then spend
     six minutes each morning doing maths to forgive myself.
  6. English put 'i before e except after c' in the rulebook,
     then spelled 'weird' like it had never read it.
  7. My houseplant died of neglect, which is impressive, because
     neglect was the one thing I gave it consistently.
  8. A snail carries its whole house everywhere and still gets
     overtaken by life; honestly, the most relatable commute ever.
  9. Time flies like an arrow and I am the banana in the fruit
     bowl, sitting still while everything ripens around me.
 10. The cat has 230 bones and total flexibility, yet chooses
     to sit on the one page I am reading; flexibility was never
     the problem, intent was.

First-pass pick: candidate 3 (science/animal contrast, tight).

Second edit pass: candidate 3's ending, "panics at a text," is too
vague to land. The final line names the exact text everyone dreads
-- "we need to talk" -- so the panic is instant and specific, and
tightens the parallel: three hearts, cool; just one heart, panic
at a single message.
"""

import os

LINE = "An octopus has three hearts and plays it cool; I have just one, and it panics at a single 'we need to talk' text."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
