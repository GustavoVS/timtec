
(function (angular) {
    'use strict';

    // Declare app level module which depends on filters, and services
    angular.module('courseMaterial', ['django', 'courseMaterial.services', 'courseMaterial.controllers',
                                  'courseMaterial.directives', 'courseMaterial.filters',
                                  'directive.markdowneditor',]);
})(angular);
