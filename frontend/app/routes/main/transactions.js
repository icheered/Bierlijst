import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
import RSVP from 'rsvp';

export default class MainTransactionsRoute extends Route {
  @service store;

  async model() {
    console.log('Loading transactions');
    return RSVP.hash({
      transactions: await this.store.findAll('transaction-list-item'),
      items: await this.store.findAll('item'),
      people: await this.store.findAll('person'),
    });
  }
}
