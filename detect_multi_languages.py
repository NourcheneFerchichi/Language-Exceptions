from collections import Counter
from langdetect import detect
from typing import List

class Solution():
  """
  Detect languages in a text message, in a context where users often write 
  messages containing multiple languages.
  """

  def __init__(self, words_to_combine: int, message: str, max_lang: int):
    """ Class initialiser
    
    Args:
        words_to_combine (int): The number N of N-grams.
        message (str): The user's multilangual text message.
        max_lang (int): The maximun number of languages to be detected.
    """
    self.words_to_combine = words_to_combine
    self.message = message
    self.max_lang = max_lang

  def generate_ngrams(self) -> List[str]:
      """ Creates an N-grams of all possible combinations of “N” successive
      words from a text.
      
      Returns:
          output (List[str]): The list of the generated N-grams. 
      """
      words = self.message.split()
      output = []  
      for i in range(len(words)-self.words_to_combine+1):
          output.append(" ".join(words[i:i+self.words_to_combine-1]))
      return output

  def detect_languages(self):
    """Detect the language of a text message. 
    
    Returns:
        detected_languages (dict): The dictionary of detected languages.
                detected_languages[n_gram_text] = language
        n (int): The number on generated N-grams.
    """
    detected_languages = {}
    n_grams = self.generate_ngrams()
    for sub_set in n_grams:
        detected_languages[sub_set] = detect(sub_set)
    return detected_languages, len(n_grams)
    
  def get_top_languages(self) -> None:
      """Extract the top self.max_lang languages
      """
      detected_languages, total_grams = self.detect_languages()
      count = Counter(detected_languages.values())
      sorted_count = sorted(
          dict(count).items(), key=lambda x: x[1], reverse=True)

      if sorted_count[0][1]/total_grams >= 0.80: # Only one Language is present
        detected_languages = sorted_count[0]
        print(f"The detected language in: '%s' is: %s" %(self.message, detected_languages[0][0].upper()))
      else:
        detected_languages = sorted_count[:self.max_lang] # Multiple languages are present
        print(f"The detected languages in: '%s' are: %s and %s" %(self.message, detected_languages[0][0].upper(), detected_languages[1][0].upper()))

### Test Solution ###
document = ["Hello, tu as vu Lost in the Middle of Night l’autre jour ?",
        "This is an English sentence written in english, dans un endroit frais et sec",
        "Who are you? 小家伙 or just what we call 非常小的家伙",
        "توفر Analytics Vidhya بوابة معرفية قائمة على المجتمع لمحترفي التحليلات وعلوم البيانات",
        "Hello, how are you doing?"]

solution = Solution(words_to_combine=3, message=document[1], max_lang=2)
solution.get_top_languages()
