// app/controllers/login.js
import Controller from '@ember/controller';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class LoginController extends Controller {
  @tracked errorMessage;
  @service session;
  @service router;

  @action
  async authenticate(e) {
    e.preventDefault();
    let { identification, password } = this;
    try {
      await this.session.authenticate(
        'authenticator:oauth2',
        identification,
        password
      );
    } catch (error) {
      if (error.status === undefined) {
        this.errorMessage = 'Server could not be reached';
      } else if (error.status === 404) {
        this.errorMessage = 'API endpoint not found';
      } else if (error.status === 400 || error.status === 422) {
        this.errorMessage = 'Incorrect username/email or password';
      } else {
        this.errorMessage = 'Unknown error occurred';
      }
    }

    if (this.session.isAuthenticated) {
      this.router.transitionTo('main');
    }
  }

  @action
  updateIdentification(e) {
    this.identification = e.target.value;
  }

  @action
  updatePassword(e) {
    this.password = e.target.value;
  }
}
