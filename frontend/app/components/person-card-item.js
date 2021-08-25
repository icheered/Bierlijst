import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';

export default class Logout extends Component {
  @service store;
  @service snackbar;

  get name() {
    return this.store.peekRecord('item', this.item.id).name;
  }

  setConsumableValue(value) {
    this.item.consumable = value;
  }

  showMessage() {
    var quotes = [
      this.personname + ' gaat zuipen!',
      'Biertje gestreept voor ' + this.personname,
      'Pilsje voor ' + this.personname,
      this.personname + ' drinkt pils!',
      this.personname + ' gaat gezellig doen!',
      this.personname + ' gaat helemaal wild!',
      this.personname + ' gaat helemaal los!',
      'Cheers, ' + this.personname + '!',
      'Proost, ' + this.personname + '!',
      this.personname + ' gaat even lekker genieten!',
    ];

    var quote = quotes[Math.floor(Math.random() * quotes.length)];

    this.snackbar.show({
      message: quote,
      dismiss: true,
      action: { label: 'linkje', click: this.printSome },
    });
  }

  printSome() {
    console.log('Printing some');
  }

  @action
  async decrement() {
    // Create a new transactions
    // Refetch
    let post = this.store.createRecord('transaction', {
      itemid: this.item.id,
      personid: this.personid,
      change: {
        consumable: -1,
      },
    });
    await post.save();
    this.store.findRecord('person', this.personid);
    this.showMessage();
  }
}
