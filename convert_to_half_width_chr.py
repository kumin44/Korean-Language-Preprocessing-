import sys
import unicodedata

# switch all words over to half-width-characters. 
def convert_to_half(fn1):
    sentences = []
    with open(fn1, 'r', encoding = 'UTF-8') as file:
         for line in file:
             line = unicodedata.normalize('NFKC', line)
             sentences.append(line)
    
    return sentences

# make a new file composed of half-width-caharacters only. 
def main(fn1, fn2):
    with open(fn2, 'w', encoding = 'UTF-8') as file:
        sentences = convert_to_half(fn1)    
        for line in sentences:
            file.write(''.join(line))       

# arg[1] : name of file to be switched over to half-width-character. -> fn1
# arg[2] : name of new file composed of half-width-characters only. -> fn2
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
    
   
   
  
	
    
	
