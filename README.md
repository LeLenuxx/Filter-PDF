# Filter-PDF

## the script extracts texts from a PDF and writes that to text file (-later use of nltk)

## Prompt for "separate.py"

```txt
I have a long text file, with lots of articles in it, it's normal text format, you will write a python script that does the following:

1. any line starting with a number, followed by a dot, you take this whole line start at the dot, then put it into a list of strings, with the article names
2. You extract each article, and put it in a separate text file, with the previously extracted name from the index as its filename
3. To extract each article, you take the text between the following two "keys" where a key, is a string that appears in a single line

   1. Text starts at "Body"

   2. Text ends at "End of Document"
   
   3. Each "Body" key is preceded by "Byline:" and "Length:" put these lines at the top of text in each text files

4. When taking text between the two "Body" and "End of Document" keys, remove any line matching "Page X of X" where X is a number
```