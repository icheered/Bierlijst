import Service, { inject as service } from '@ember/service';

export default class SessionAccountService extends Service {
  @service session
  @service store

  async loadCurrentUser() {
    console.log('Loading current user');
    let userprofile = await this.store.findAll('account');
    let account = userprofile.objectAt(0);
    this.set('account', account);
    return account;
  }
}
