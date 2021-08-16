import Controller from '@ember/controller';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';

// Only allow access to the application when authenticated
export default class ApplicationController extends Controller {
  @service session;

  @action
  invalidateSession() {
    this.session.invalidate();
  }
}
