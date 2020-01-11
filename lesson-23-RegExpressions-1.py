import re

mytext = 'vasya	vasyavasya 1976, Pet - 1988: Olya 1992,felicia@yandex.ru,' \
    'Lance,	Maecenas@gmail.org	Vietri di Potenza,	Ross Booth	1908,' \
    'Zeus	risus@sedfacilisisvitae.edu	Werder,	Gwendolyn, Berry	1928,' \
    'Erich , vulputate.mauris@iaculisquispede.edu,	Sevastopol	Ebony Blackburn,	1908'\
    'Berk	sit.amet.nulla@yandex.uk	Boca del Rio	Flynn Tanner , 	2008'\
    'Thomas,	ultricies@gmail.com	Belem,	Nerea Mercer	1804,'
'''
\d  = any Digital 0-9
\D  = any non Digital
\w  = any Alphabeet symbol [ A-Z a-z]
\W  = any non Alphabeet symbol
\s  = space
\S  = any non space

[A-Z][a-z]+ = SEARCH FIRST BIG THEN SMALL LETTER 
@\w+\.\w+   = SEARCH MAIL 

[0-9](3)

'''

lool_searching = r"@\w+\.\w+"
all_results = re.findall(lool_searching, mytext)

print(all_results)
