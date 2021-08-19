import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';

export default class Logout extends Component {
    @service store;

    get name() {
        return this.store.peekRecord('item', this.item.id).name;
    }

    setConsumableValue(value) {
        this.item.consumable = value
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
            }
        })
        await post.save()
        this.store.findRecord('person', this.personid)
    }
}
