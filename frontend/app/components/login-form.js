import Component from '@ember/component';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class LoginForm extends Component {
  @service session;
  @service router;

  @action
  async authenticateWithOAuth2() {
    console.log('Authenticating with OAuth2');
    try {
      let { identification, password } = this;
      await this.session.authenticate(
        'authenticator:oauth2',
        identification,
        password
      );

      if (this.rememberMe) {
        // Store session in cookie for 2 weeks
        this.session.set('store.cookieExpirationTime', 60 * 60 * 24 * 14);
      }
    } catch (error) {
      let errormessage = 'Error';

      if (error.status === undefined) {
        errormessage = 'Server could not be reached';
      } else if (error.status === 404) {
        errormessage = 'API endpoint not found';
      } else if (error.status === 400 || error.status === 422) {
        errormessage = 'Incorrect username/email or password';
      } else {
        errormessage = 'Unknown error occurred';
      }

      this.set('errorMessage', errormessage);
    }

    if (this.session.isAuthenticated) {
      this.router.transitionTo('main');
    }
  }

  @action
  updateIdentification(e) {
    console.log('Updating Identification');
    this.set('identification', e.target.value);
  }

  @action
  updatePassword(e) {
    console.log('Updating Password');
    this.set('password', e.target.value);
  }

  @action
  updateRememberMe(e) {
    console.log('Updating RememberMe');
    this.set('rememberMe', e.target.checked);
  }
}
