(function() {
    'use strict';

    app.controller('mainCtrl', ControllerCtrl)

    /** @ngInject */
    function ControllerCtrl($scope) {

        var _randomNumber = function(min, max) {
                var number = (Math.floor(Math.random() * (max - min)) + min);
                return number;
            },

            _tcos = function(elem, aClass, tam) {
                var _activeScroll = function() {
                    $(window).scrollTop() > tam ? $(elem).addClass(aClass) : $(elem).removeClass(aClass);
                }
                $(window).on('scroll', function() {
                    _activeScroll();
                });
                _activeScroll();
            };

        _tcos('.details__item', 'details__item--fixed', 700);

        $scope.changePhrase = function(number, onClick) {
            $scope.trump.src = 'head-trump-' + number + '.png';
            $scope.trump.animate = 'rubberBand';
            if (onClick) {
                $scope.trump.currentItem = number;
                var _phrases = '';
                for (var i = 0; i < number; i++) {
                    _phrases = _phrases + "<div class='phrases__item animated fadeIn'>" + $scope.phrases[_randomNumber(0, $scope.phrases.length)] + "</div>";
                }
                $scope.trump.phrase = _phrases;
            }
        }


        $scope.phrases = [
            "You know, it really doesn’t matter what the media write as long as you’ve got a young and beautiful piece of ass.",
            "The concept of global warming was created by and for the Chinese in order to make U.S. manufacturing non-competitive.",
            "Listen you mother fuckers, we're going to tax you 25 percent!",
            "When was the last time anybody saw us beating, let's say, China in a trade deal? They kill us. I beat China all the time. All the time.",
            "The U.S. will invite El Chapo, the Mexican drug lord who just escaped prison, to become a U.S. citizen because our leaders can't say no!",
            "I will build a great wall — and nobody builds walls better than me, believe me —and I’ll build them very inexpensively. I will build a great, great wall on our southern border, and I will make Mexico pay for that wall. Mark my words.",
            "The wall will go up and Mexico will start behaving.",
            "Laziness is a trait in the blacks. ... Black guys counting my money! I hate it.",
            "The only kind of people I want counting my money are little short guys that wear yamakas every day.",
            "If you can’t get rich dealing with politicians, there’s something wrong with you.",
            "A certificate of live birth is not the same thing by any stretch of the imagination as a birth certificate.",
            "He's not a war hero. He's a war hero because he was captured. I like people that weren't captured, OK, I hate to tell you.",
            "One of the key problems today is that politics is such a disgrace. Good people don’t go into government."
        ];

        $scope.trump = {
            animate: '',
            src: '',
            phrase: '',
            currentItem: ''
        }

        $scope.changePhrase(6, true);

    }

}());