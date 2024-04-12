var arrLang = {
    'en': {
        'about': 'About us',
        'result': 'Result',
        'story': 'Story about me',
        'application': 'Applications for release from prison',
        'new1': 'On July 23, 2023, the leader of the Al-Fatah coalition in the Iraqi parliament, Sadiq Abdullah, announced the Iraqi-Syrian agreement on the dismantling of the Al-Hol camp.'
        },
    'rus':
        {
    'about': 'О нас',
    'result': 'Результаты',
    'story': 'Расскажи свою историю',
    'application': 'Прием заявок выхода из лагерей',
    'new1': '23 июля 2023 года лидер коалиции «Аль-Фатх» в иракском парламенте Садик Абдулла сообщил об иракско-сирийском соглашении о демонтаже лагеря «Аль-Холь»',
}
}

    $(function(){
        $(".translate").click(function() {
            var lang = $(this).attr('id');

            $('.lang').each(function(index, item) {
                $(this).text(arrLang[lang][$(this).attr('key')]);
            });
        });
    });