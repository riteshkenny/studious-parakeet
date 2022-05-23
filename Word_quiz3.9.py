import csv,re,sys,random,glob,os
from collections import defaultdict


	
	
word = {}
word_files = {}
wordlist = []
meaning1 = defaultdict(list)
synonym1 = defaultdict(list)
antonym1 = {}
meaning = {}
synonym = {}
antonym = {}
sentence = []

def main():
	print("Hello World!")
	

def file_import():


            

    with open("Digest_eng_sentences.tsv", encoding='utf8') as s:
        for line in s:
            line = line.rstrip("\n")
            (line_word, line_meaning, line_sent) = line.split("\t")
            if not (re.search("(\s[sS][Ee][Xx])|(\s[fF][uU][Cc][kK])|(\s[S][e][e]\s)", line_sent)):
                sentence.insert(len(sentence) - 1, line_sent)
        
    with open("Digest_Synonyms.tsv", encoding='utf8') as s:
        for line in s:
            line = line.rstrip("\n")
            (line_word, line_syn) = line.split("\t")
            synonym1[line_word].append(line_syn)
            
    with open("Digest_Antonyms.tsv", encoding='utf8') as s:
        for line in s:
            line = line.rstrip("\n")
            (line_word, line_syn) = line.split("\t")
            antonym1[line_word] = (line_syn)
    with open("Digest_Meanings.tsv") as s:
        for line in s:
            line = line.rstrip("\n")
            (line_word, line_syn) = line.split("\t")
            meaning1[line_word].append(line_syn)


    cwd = os.getcwd()
    os.chdir(f"{cwd}/wordbundles")
    file_counter = 1
    for file in glob.glob("*.txt"):
        print(f"{file_counter}:\t", end = "")
        print(f"{file}")
        word_files[file_counter] = file
        file_counter += 1
        
    file_no = input("Enter the file number:")
    file_no = int(file_no)
    print(f"File is {word_files[file_no]}")
    with open(word_files[file_no]) as f:

        for line in f:
            line = line.rstrip("\n")
            (line_word, line_meaning, line_synonym, line_antonym) = line.split('BBBB')
            wordlist.insert(len(wordlist) - 1, line_word)
            meaning[line_word] = line_meaning
            synonym[line_word] = line_synonym
            antonym[line_word] = line_antonym
    




def final_brief(first_q,right_counter,wrong_counter,series_counter):
    
    nl = "\n"
    tb = "\t"
    
    print(f'Example Sentences:{nl}++++++++++++++++++{tb}')
    counter_ex = 1
    
    for i in range(0, len(sentence) -1):
        search_word = "\s" + first_q.lower() + "\s"
        
        if (re.search(search_word, sentence[i])):
            if (counter_ex <4):
                print(f'\t\t{sentence[i]}')
                counter_ex += 1
    
    synonym2 = ""
    antonym2 = ""

    if first_q.lower() in synonym1:
        synonym2 = synonym[first_q] + str(synonym1[first_q.lower()])
    else:
        synonym2 = synonym[first_q]
        
    if first_q.lower() in antonym1:
        antonym2 = antonym[first_q] + str(antonym1[first_q.lower()])
    else:
        antonym2 = antonym[first_q]
    
    print(f'\nSynonyms:{nl}---------{nl}{tb}{synonym2}{tb}')
    print(f'\nAntonyms:{nl}---------{nl}{tb}{antonym2}{tb}')
    print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n Correct: {right_counter} Incorrect: {wrong_counter} Questions left: {series_counter}\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
    input()


def example_sentence(word):
    if word in meaning1:
        set1 = set(meaning1[word])
        opt_1 = random.choice(list(set1))
        match = re.search(f"(\s[sS][Ee][Xx])|(\s[fF][uU][Cc][kK])|(\s[S][e][e]\s)|(\s[oO][f]\s[o][r]\s)|{word.lower()}|{word}|[p][.]\s[p]", opt_1)
        counter = 1
        if match:
            while match is not None and counter < 3:
                counter += 1
                opt_1 = random.choice(list(set1))
                match = re.search(f"(\s[sS][Ee][Xx])|(\s[fF][uU][Cc][kK])|(\s[S][e][e]\s)|(\s[oO][f]\s[o][r]\s)|{word.lower()}|{word}|[p][.]\s[p]", opt_1)
            if not match:
                print(f'\t{opt_1}\n\n:')
        else:
            print(f'\t{opt_1}\n\n:')


def start():
    word_list_no = []
    rand_or_sequence = input("How do you want questions to be? \n1) Random:\n2) Sequence\n\tEnter:")
    rand_or_sequence = int(rand_or_sequence)
    w_2_m =  input("Word to Meaning or Meaning to word? \n1) Word to Meaning:\n2) Meaning to Word\n\tEnter:")
    w_2_m = int(w_2_m)
    right_counter = 0
    wrong_counter = 0
    exit_counter = 0
    wordlist_start = wordlist.copy()
    if (rand_or_sequence == 1):
        random.shuffle(wordlist_start)
    
    
    while (len(wordlist_start) > 0):
        exit_counter = 0
        first_q = wordlist_start.pop(len(wordlist_start) - 1)
        random.shuffle(wordlist)
        answer_opt = [first_q, wordlist[0], wordlist[1], wordlist[2]]
        
        random.shuffle(answer_opt)
        
    
        while ((w_2_m == 1) and (exit_counter < 3)):

            
            print("------------------------------------------------------------------\n")
            print(f'{first_q}:\n======================')
            print(f'Option 1:\n\t{meaning[answer_opt[0]]}')
            example_sentence(answer_opt[0])
            print(f'Option 2:\n\t{meaning[answer_opt[1]]}')
            example_sentence(answer_opt[1])
            print(f'Option 3:\n\t{meaning[answer_opt[2]]}')
            example_sentence(answer_opt[2])
            print(f'Option 4:\n\t{meaning[answer_opt[3]]}')
            example_sentence(answer_opt[3])

            
            ans_capture = input(f'Please enter answer [1-4]')
            # ans_capture = int(ans_capture)
            while ans_capture not in ["1", "2", "3", "4"]:
            # if ((ans_capture == '1') or (ans_capture == '2') or (ans_capture == '3') or (ans_capture == '4')):
            
                # else:
                print("Please enter valid number between [1-4]")
                ans_capture = input(f'Please enter answer [1-4]')
            ans_capture = int(ans_capture)
            
            
            if (first_q == answer_opt[ans_capture - 1]):
                print("££££££££££££££££££££££££££££££\nCorrect answer!!! Well done!!!\n££££££££££££££££££££££££££££££\n")
                right_counter += 1
                exit_counter = 4
                final_brief(first_q,right_counter,wrong_counter,len(wordlist_start))
            else:
                exit_counter += 1
                print(f'*************************************************\n Wrong answer {3 - exit_counter} tries left:\n *************************************************************\n')
            if (exit_counter == 3):
                print("Wrong Answer :( :( :(\nAnswer is:\n")
                right_answer = meaning[first_q]
                print(f'{right_answer}\n')
                wrong_counter += 1
                final_brief(first_q,right_counter,wrong_counter,len(wordlist_start))
            
        while ((w_2_m == 2) and (exit_counter < 3)):
            print("------------------------------------------------------------------\n")
            question = meaning[first_q]

            print(f'{question}\n')
            example_sentence(first_q)
            
            ans_opt1 = answer_opt[0]
            ans_opt2 = answer_opt[1]
            ans_opt3 = answer_opt[2]
            ans_opt4 = answer_opt[3]        
            print(f'Option 1:\n\t{ans_opt1} \nOption 2:\n\t{ans_opt2}\nOption 3:\n\t{ans_opt3}\nOption 4:\n\t{ans_opt4}')
            
            ans_capture = input(f'Please enter answer [1-4]')
            while (ans_capture == ""):
                print("Please enter valid number between [1-4]")
                ans_capture = input(f'Please enter answer [1-4]')
            ans_capture = int(ans_capture)
            if (first_q == answer_opt[ans_capture - 1]):
                print("££££££££££££££££££££££££££££££\nCorrect answer!!! Well done!!!\n££££££££££££££££££££££££££££££\n")
                right_counter += 1
                exit_counter = 4
                final_brief(first_q,right_counter,wrong_counter,len(wordlist_start))
            else:
                exit_counter += 1
                print(f'*************************************************\n Wrong answer {3 - exit_counter} tries left:\n *************************************************************\n')
            if (exit_counter == 3):
                print(f'Wrong Answer :( :( :(\nAnswer is:\n {first_q}')

                wrong_counter += 1
                final_brief(first_q,right_counter,wrong_counter,len(wordlist_start))



if __name__ == "__main__":
    # main()
    file_import()
    start()
