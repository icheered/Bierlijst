import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';

export default class TransactionList extends Component {
  @service store;

  getitemname(itemid) {
    return this.store.peekRecord('item', itemid).name;
  }

  getpersonname(personid) {
    return this.store.peekRecord('person', personid).name;
  }

  getTransactions() {
    this.store.findAll('transaction-list-item').then(function (transactions) {
      console.log(transactions);
    });
  }

  @action
  async toggle(transactionsid) {
    console.log('Toggling ' + transactionsid);
    let transaction = this.store.peekRecord(
      'transaction-list-item',
      transactionsid
    );
    await transaction.save();
  }
}
