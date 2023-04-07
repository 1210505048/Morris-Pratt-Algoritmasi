def compute_lps(pattern):
   
    lps = [0] * len(pattern)
    len_prefix = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[len_prefix]:
            len_prefix += 1
            lps[i] = len_prefix
            i += 1
        else:
            if len_prefix != 0:
                len_prefix = lps[len_prefix - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def morris_pratt(text, pattern):
    
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    count = 0  # Belirli kelimenin kaç kez geçtiğini saymak için sayaç

    i = 0  # text dizisinin indeksi
    j = 0  # pattern dizisinin indeksi
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                
                count += 1
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count


def count_word_in_file(file_path, word):
    with open(file_path, "r") as file:
        text = file.read()
        count = morris_pratt(text, word)
        return count


file_path = "dosya.txt" 
word1 = "upon" 
count1 = count_word_in_file(file_path, word1)
print(f"'{word1}' kelimesi dosyada {count1} kez geçiyor.")

word2 = "sigh" 
count2 = count_word_in_file(file_path, word2)
print(f"'{word2}' kelimesi dosyada {count2} kez geçiyor.")

word3 = "Dormouse"
count3 = count_word_in_file(file_path, word3)
print(f"'{word3}' kelimesi dosyada {count3} kez geçiyor.")

word4 = "jury-box" 
count4 = count_word_in_file(file_path, word4)
print(f"'{word4}' kelimesi dosyada {count4} kez geçiyor.")

word5 = "swim" 
count5 = count_word_in_file(file_path, word5)
print(f"'{word5}' kelimesi dosyada {count5} kez geçiyor.")
