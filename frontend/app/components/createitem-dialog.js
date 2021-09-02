import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class CreateitemDialog extends Component {
  @service store;
  @service snackbar;
  @tracked open;

  @action
  openDialog() {
    console.log('Showing Dialog');
    this.open = true;
  }
  @action
  async save() {
    if (this.itemName == undefined) {
      this.snackbar.show({
        message: 'No name was given, item not created',
        dismiss: true,
      });
    } else {
      this.itemContainersize ? this.itemContainersize = this.itemContainersize : this.itemContainersize = 24
      console.log(`Saving item: ${this.itemname}`);
      let item = this.store.createRecord('item', {
        name: this.itemName,
        container_size: this.itemContainersize,
      });
      await item.save();
      await this.store.findAll('item');
      await this.store.findAll('person');
    }
  }

  @action
  updateName(e) {
    console.log('Updating item name');
    this.set('itemName', e.target.value);
  }
  @action
  updateContainersize(e) {
    console.log('Updating container size');
    this.set('itemContainersize', e.target.value);
  }
}
