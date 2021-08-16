import JSONAPIAdapter from '@ember-data/adapter/json-api';
import { inject as service } from '@ember/service';
import { underscore } from '@ember/string';

export default class ApplicationAdapter extends JSONAPIAdapter {
    @service session;
    host = 'http://localhost:8001';
    namespace = 'api'

    get headers() {
        let headers = {};
        if (this.session.isAuthenticated) {
            headers['Authorization'] = `Bearer ${this.session.data.authenticated.access_token}`;
        }
        return headers;
    }

    pathForType(accounts) {
        return "user/me";
    }

}
