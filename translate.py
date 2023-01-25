from translate import Translator

obj=Translator(from_lang="english",to_lang="hindi")
new_name=obj.translate("Good Morning!")
print(new_name)
