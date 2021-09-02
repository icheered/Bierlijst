


import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class EdititemDialog extends Component {
  @service store;
  @service snackbar;
  @tracked open;

  @action
  openDialog() {
    console.log('Showing Dialog');
    this.open = true;
  }
  @action
  save() {
    if (this.itemName == undefined && this.itemContainersize == undefined) {
      console.log("No values were updated, not saving")
      return
    }
    this.itemName ? this.itemName = this.itemName : this.itemName = this.item.name
    this.itemContainersize ? this.itemContainersize = this.itemContainersize : this.itemContainersize = this.item.container_size
    console.log('Saving');
    console.log(this.itemName, this.itemContainersize)

    let item = this.store.peekRecord('item', this.item.id)
    item.name = this.itemName
    item.container_size = this.itemContainersize
    person.save()
  }

  @action
  updateName(e) {
    console.log('Updating item name');
    this.set('itemName', e.target.value);
  }
  @action
  updateContainersize(e) {
    console.log('Updating item container size');
    this.set('itemContainersize', e.target.value);
  }
}
