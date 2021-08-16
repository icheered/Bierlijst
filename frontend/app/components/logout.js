import Component from '@ember/component';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class Logout extends Component {
  @service session;
  @service router;
  @service sessionAccount;

  @action
  logout() {
    console.log('Logging out');
    this.session.invalidate();
  }
}
