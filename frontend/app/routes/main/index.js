import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import RSVP from 'rsvp';

export default class MainIndexRoute extends Route {
    @service store;

    async model() {
        console.log('Loaded Beerlist');
        // let people = await this.store.findAll('person')
        // let items = await this.store.findAll('item')
        // console.log(people.objectAt(0).id)
        // console.log(items.objectAt(1).name)
        return RSVP.hash({
            people: await this.store.findAll('person'),
            items: await this.store.findAll('item'),
        });
    }
}
