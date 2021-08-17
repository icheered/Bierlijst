import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';

export default class Main extends Component {
  @service session;
  @service sessionAccount;

  account = this.sessionAccount.account;

  @action
  logout() {
    this.session.invalidate();
  }
}
