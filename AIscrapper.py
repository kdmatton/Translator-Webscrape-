from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# input text
source_key = str(input("Enter Your Language: "))          # Use Full and not Abbreviation
target_key = str(input("Enter The Targeted Language : ")) # Use Full and not Abbreviation
text = str(input("Enter Text: "))                         # Enter the text related to language, or there is no result or error 

# setting for chrome / driver
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

#langauges 
language_dict = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Assamese": "as",
    "Aymara": "ay",
    "Azerbaijani": "az",
    "Bambara": "bm",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bhojpuri": "bho",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dhivehi": "dv",
    "Dogri": "doi",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Ewe": "ee",
    "Filipino (Tagalog)": "fil",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Guarani": "gn",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "he or iw",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Ilocano": "ilo",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv or jw",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Konkani": "gom",
    "Korean": "ko",
    "Krio": "kri",
    "Kurdish": "ku",
    "Kurdish (Sorani)": "ckb",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lingala": "ln",
    "Lithuanian": "lt",
    "Luganda": "lg",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Maithili": "mai",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Meiteilon (Manipuri)": "mni-Mtei",
    "Mizo": "lus",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Nyanja (Chichewa)": "ny",
    "Odia (Oriya)": "or",
    "Oromo": "om",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese (Portugal, Brazil)": "pt",
    "Punjabi": "pa",
    "Quechua": "qu",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Sanskrit": "sa",
    "Scots Gaelic": "gd",
    "Sepedi": "nso",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala (Sinhalese)": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tagalog (Filipino)": "tl",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Tigrinya": "ti",
    "Tsonga": "ts",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Twi (Akan)": "ak",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}

# scource and target for language
source = language_dict[source_key]
target = language_dict[target_key]
driver.get(f"https://translate.google.com/?sl={source}&tl={target}&text=&op=translate")

# Enters text into the translator
input_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'er8xn'))
    )
input_box.send_keys(text)

# Waits for the tranlation to be visible
translated_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'ryNqvb'))
    )

# Gets translation
translation = translated_box.text
print(f'The Translation is: {translation}')
