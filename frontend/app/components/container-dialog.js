import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class ContainerDialog extends Component {
    @service store;
    @service snackbar;
    @tracked open

    @action
    openDialog() {
        console.log("Showing Dialog")
        this.open = true
    }

    @action
    async decrement() {
        console.log('Decrementing container');
        let post = this.store.createRecord('transaction', {
            itemid: this.itemid,
            personid: this.personid,
            change: {
                container: -1,
            },
        });
        await post.save();
        this.store.findRecord('person', this.personid);
        this.snackbar.show({
            message: this.personname + " heeft een kratje ingeleverd!",
            dismiss: true,
        });
    }

    @action
    async increment() {
        console.log('Incrementing container');
        let post = this.store.createRecord('transaction', {
            itemid: this.itemid,
            personid: this.personid,
            change: {
                container: 1,
                consumable: this.containersize
            },
        });
        await post.save();
        this.store.findRecord('person', this.personid);
        this.snackbar.show({
            message: this.personname + " heeft een kratje gekocht!",
            dismiss: true,
        });
    }
}