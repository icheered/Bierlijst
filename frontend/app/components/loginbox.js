import Component from '@glimmer/component';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class Loginbox extends Component {
  @service router;

  @tracked username = '';
  @tracked password = '';

  @action
  login() {
    console.log(this.username);
    console.log(this.password);
    // Do API call to get session token
    // Store session token (where?)
    this.router.transitionTo('main');
  }
}
