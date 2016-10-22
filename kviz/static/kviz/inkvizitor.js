var new_word;
var base="http://127.0.0.1:8000/";


function getWord(type) {
    var msg = $.ajax({
        type: "GET",
        url: base + 'quiz/word/' + type,
        async: false
    }).responseText.toLowerCase();
    return msg;
};

$(document).ready(function () {
    $('.selection').click(function () {
        $('.selection').attr('disabled', 'disabled');
        $('.selection').addClass('disable');
        $(this).addClass('clicked');
        var category = $(this).val();
        switch (category) {
            case 'f' :
                var word = getWord(1);
                new_word = word;
                break;
            case 'i' :
                var word = getWord(0);
                new_word = word;
                break;
            case 'z' :
                var word = getWord(2);
                new_word = word;
                break;
            case'g' :
                var word = getWord(3);
                new_word = word;
                break;
            default :
                alert('prvo odaberite kategoriju');

        }
        ;

        for (i = 0; i < word.length; i = i + 1) {
            $('.word').append('<p>-</p>');
        }
        ;
    });
});

$(document).ready(function () {
    $('.letter').click(function () {
        var real_found;
        var letter = $(this).attr('name');
        for (i = 0; i < new_word.length; i++) {
            if (letter === new_word[i]) {
                found = true;
                real_found = found;
                var true_letter = $('.word p');
                $(true_letter[i]).text(letter);
                $(this).css('background-color', '#339966');
                var end = $('.word p').text();
                if (end == new_word) {
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', '/quiz/score', false); // sync request
                    xhr.send();
                    $('.new_game').fadeIn(1500);
                    $('.game_result').html('Cestitam Pobedili Ste');
                    $('.letter').attr('disabled', 'disabled');
                }
                ;
            }
            ;

        }
        ;

        if (!real_found) {
            $(this).css('background-color', 'red');
            $(this).fadeOut();
            $('.faild').append('|' + '');
            var broj_promasaja = $('.faild').text();
            var kraj_igre = '||||||';
            if (broj_promasaja === kraj_igre) {
                var word = new_word.toUpperCase();
                $('.letter').attr('disabled', 'disabled');
                $('.new_game').fadeIn(1500);
                $('.game_result').html('Izgubili ste trazena rec je' + " " + word);

            }
            ;

        }
        ;
    });


});

$(document).ready(function () {
    $('.selection ').mouseenter(function () {
        $(this).addClass('hoverButton');
        $(this).mouseleave(function () {
            $(this).removeClass('hoverButton');
        });
    });

});

$(document).ready(function () {
    $('.letter').mouseenter(function () {
        $(this).addClass('hoverletter');
        $(this).mouseleave(function () {
            $(this).removeClass('hoverletter');
        });
    });
});

$(document).ready(function () {
    $('.new_game_button').click(function () {
        window.location.assign(base + "quiz/");
    });
    $('.new_game_button').mouseenter(function () {
        $(this).css('border', '3px solid #339966');
    });
    $('.new_game_button').mouseleave(function () {
        $(this).css('border', '1px solid #339966');
    });

});

$(document).ready(function () {
    $('.logout_button').click(function () {
        window.location.assign(base + "logout/");
    });
});

$(document).ready(function () {
    $('.top_ten').click(function () {
        window.location.assign(base + "quiz/top/");
    });
});

$(document).ready(function () {
    $('.login_button').click(function () {
        window.location.assign(base + "login/");
    });
});

function register() {
    window.location.assign(base + "register/");
};

function login() {
    window.location.assign(base + "login/");
};

