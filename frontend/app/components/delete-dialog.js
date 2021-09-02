


import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class EdititemDialog extends Component {
    @service store;
    @tracked open;

    @action
    openDialog() {
        console.log('Showing Dialog');
        this.open = true;
    }
    @action
    async delete() {
        console.log(`Deleting ${this.type} ${this.id}`)
        let obj = this.store.peekRecord(this.type, this.id)
        obj.deleteRecord();
        obj.save()
    }
}
