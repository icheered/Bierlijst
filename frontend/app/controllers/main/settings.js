import Controller from '@ember/controller';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class SettingsController extends Controller {
    @service store;
    @service snackbar;

    get getfullname() {
        return this.store.peekAll('account').objectAt(0).full_name;
    }

    get getItems() {
        return this.store.peekAll('item')
    }

    get getPeople() {
        return this.store.peekAll('person')
    }

    @action
    updateFullname(e) {
        console.log('Updating Fullname');
        this.set('fullname', e.target.value);
    }

    @action
    async save() {
        console.log();
        if (this.fullname == undefined) {
            this.snackbar.show({
                message: 'Name was not changed',
                dismiss: true,
            });
        } else {
            this.snackbar.show({
                message: 'Saving name: ' + this.fullname,
                dismiss: true,
            });
            console.log('Saving new name: ' + this.fullname);
            let transaction = this.store.peekAll('account').objectAt(0);
            transaction.full_name = this.fullname;
            await transaction.save()
        }
    }

    @action
    delete(itemid) {
        console.log("Deleting: " + itemid)
    }
    @action
    edit(itemid) {
        console.log("Edit: " + itemid)
    }
}
