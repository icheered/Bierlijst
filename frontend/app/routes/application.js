import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class ApplicationRoute extends Route {
  @service session;

  beforeModel(transition) {
    console.log('Requiring Authentication');
    this.session.requireAuthentication(transition, 'login');
  }

  model() {
    console.log('Application startup');
  }
}
