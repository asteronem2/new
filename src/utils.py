rus_to_eng_dict = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'y',
    'ф': 'ph',
    'х': 'h',
    'ц': 'c',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sh',
    'ъ': 'y',
    'ы': 'yi',
    'ь': '',
    'э': 'e',
    'ю': 'u',
    'я': 'ya',
    ' ': '-',


}


async def slugify(text: str) -> str:
    res = ''

    for i in text.lower():
        translated = rus_to_eng_dict.get(i, i)
        res += translated

    return res
