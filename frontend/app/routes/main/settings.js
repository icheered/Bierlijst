import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import RSVP from 'rsvp';

export default class MainSettingsRoute extends Route {
    @service store;

    async model() {
        console.log('Loading transactions');
        return RSVP.hash({
            account: await this.store.findAll('account'),
            items: await this.store.findAll('item'),
            people: await this.store.findAll('person'),
        });
    }
}
