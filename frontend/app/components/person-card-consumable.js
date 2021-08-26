import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';

export default class PersonCardConsumable extends Component {
  @service store;
  @service snackbar;

  getitemname(itemid) {
    return this.store.peekRecord('item', itemid).name;
  }

  setConsumableValue(value) {
    console.log('Setting consumable value');
    this.item.consumable = value;
  }

  showMessage(personname) {
    console.log('Showing message');
    var quotes = [
      personname + ' gaat zuipen!',
      'Biertje gestreept voor ' + personname,
      'Pilsje voor ' + personname,
      personname + ' drinkt pils!',
      personname + ' gaat gezellig doen!',
      personname + ' gaat helemaal wild!',
      personname + ' gaat helemaal los!',
      'Cheers, ' + personname + '!',
      'Proost, ' + personname + '!',
      personname + ' gaat even lekker genieten!',
    ];

    var quote = quotes[Math.floor(Math.random() * quotes.length)];

    this.snackbar.show({
      message: quote,
      dismiss: true,
    });
  }

  hasSingleActiveItem(personid) {
    let balance = this.store.peekRecord('person', personid).balance;
    let trueCounter = 0;
    for (var i = 0; i < balance.length; i++) {
      if (balance.objectAt(i).is_active) {
        trueCounter += 1;
      }
    }
    return trueCounter == 1 ? true : false;
  }

  getSingleActiveItem(personid) {
    let balance = this.store.peekRecord('person', personid).balance;
    for (var i = 0; i < balance.length; i++) {
      if (balance.objectAt(i).is_active) {
        return balance.objectAt(i).id;
      }
    }
  }

  @action
  async decrement(personid, itemid, personname) {
    console.log('Decrementing');
    // Create a new transactions
    // Refetch
    let post = this.store.createRecord('transaction', {
      itemid: itemid,
      personid: personid,
      change: {
        consumable: -1,
      },
    });
    await post.save();
    this.store.findRecord('person', personid);
    this.showMessage(personname);
  }
}
