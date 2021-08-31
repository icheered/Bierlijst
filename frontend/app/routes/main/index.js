import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import RSVP from 'rsvp';

export default class MainIndexRoute extends Route {
  @service store;

  async model() {
    console.log('Loading Beerlist');
    return RSVP.hash({
      people: await this.store.findAll('person'),
      items: await this.store.findAll('item'),
    });
  }
}
