import Component from '@ember/component';
import { inject as service } from '@ember/service';

import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class DropdownMenu extends Component {
  @tracked open;
  @service session;

  @action
  openMenu() {
    this.open = true;
  }

  @action
  alert() {
    alert('Menu item clicked.');
  }

  @action
  logout() {
    console.log('Logging out');
    this.session.invalidate();
  }
}
