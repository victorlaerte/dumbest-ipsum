(function() {
    'use strict';

    app.controller('mainCtrl', ControllerCtrl)

    /** @ngInject */
    function ControllerCtrl($scope) {

        $scope.bodyTrump = {
            animate: 'flipInY',
            src: 'head-trump-' + 1 + '.png'
        }

        $scope.changePhrase = function(number) {
            $scope.bodyTrump.src = 'head-trump-' + number + '.png';
            $scope.bodyTrump.animate = 'rubberBand';
        }
    }

}());