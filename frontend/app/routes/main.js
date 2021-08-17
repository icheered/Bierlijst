import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

// Only allow access to this route when authenticated
export default class MainRoute extends Route {
  @service session;
  @service store;
  @service sessionAccount;

  async model() {
    console.log('Loaded main');
    let userprofile = await this.store.findAll('account');
    let user = userprofile.objectAt(0);
    this.set('account', user);
    return user;
  }
}
