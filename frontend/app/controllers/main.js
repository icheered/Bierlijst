import Component from '@ember/component';
import Controller from '@ember/controller';

import { inject as service } from '@ember/service';
import { action } from '@ember/object';

export default class MainController extends Controller {
  @service session;
  @service sessionAccount;

  account = this.sessionAccount.account;

  @action
  logout() {
    this.session.invalidate();
  }

  @action
  showmessage() {
    this.snackbar.show({
      message: 'Testmessage',
      dismiss: true,
    });
  }

  get getfullname() {
    return this.store.peekAll('account').objectAt(0).full_name;
  }
}
