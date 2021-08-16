import { inject as service } from '@ember/service';

import SessionService from 'ember-simple-auth/services/session';

export default SessionService.extend({
  sessionAccount: service(),

  handleAuthentication() {
    console.log('Handling authentication');
    this._super(...arguments);

    this.sessionAccount.loadCurrentUser().catch(() => this.invalidate());
  },
});
