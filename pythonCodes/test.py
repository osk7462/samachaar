country_list = "ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za".split(" ")
with open("country.html", "w") as file:
    for country in country_list:
        file.writelines(r"<a href=""\"{{% url 'home' '{}' %}}\""">{}</a>\n".format(country, country))

# #
# language_list = "ar de en es fr he it nl no pt ru se ud zh".split(" ")
# with open("language.html", "w") as file:
#     for language in language_list:
#         file.writelines("<a href=""#"">{}</a>\n".format(language))
