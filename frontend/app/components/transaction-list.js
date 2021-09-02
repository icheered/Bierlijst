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

  getTimeFromTimestamp(timestamp) {
    let date = new Date(timestamp * 1000)
    let minutes = (String(date.getMinutes()).length == 1 ? "0" + String(date.getMinutes()) : String(date.getMinutes()))
    let seconds = (String(date.getSeconds()).length == 1 ? "0" + String(date.getSeconds()) : String(date.getSeconds()))

    let datetime = date.getDate() +
      "/" + (date.getMonth() + 1) +
      "/" + date.getFullYear() +
      " " + date.getHours() +
      ":" + minutes +
      ":" + seconds;
    return datetime
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
