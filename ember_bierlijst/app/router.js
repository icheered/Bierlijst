import EmberRouter from '@ember/routing/router';
import config from 'ember-bierlijst/config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.rootURL;
}

Router.map(function () {
  this.route('login');
  this.route('main', function () {
    this.route('settings');
    this.route('containers');
    this.route('transactions');
  });
  this.route('not-found', { path: '/*path' });
});