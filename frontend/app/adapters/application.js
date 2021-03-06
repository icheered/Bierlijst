import JSONAPIAdapter from '@ember-data/adapter/json-api';
import { inject as service } from '@ember/service';
import config from '../config/environment';


export default class ApplicationAdapter extends JSONAPIAdapter {
  @service session;
  @service router;

  host = config.BACKEND_ADDRESS
  namespace = config.BACKEND_API_PATH

  get headers() {
    let headers = {};
    if (this.session.isAuthenticated) {
      headers[
        'Authorization'
      ] = `Bearer ${this.session.data.authenticated.access_token}`;
    }
    return headers;
  }

  handleResponse(status, headers, _payload, requestData) {
    if (status === 401) {
      console.log('Unauthorized API request, logging out');
      this.session.invalidate();
      //this.router.transitionTo('login');
    }
    return super.handleResponse(status, headers, _payload, requestData);
  }
}
