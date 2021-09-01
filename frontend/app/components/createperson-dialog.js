import Component from '@ember/component';
import { inject as service } from '@ember/service';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class ContainerDialog extends Component {
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
    if (this.personName == undefined) {
      this.snackbar.show({
        message: 'No name was given, person not created',
        dismiss: true,
      });
    } else {
      console.log('Saving');
      console.log(this.personName)
      let person = this.store.createRecord('person', {
        name: this.personName
      });
      await person.save();
      await this.store.findAll('person');
    }



    // let person = this.store.peekRecord('person', this.person.id)
    // person.name = this.personName
    // person.save()
  }

  @action
  updateName(e) {
    console.log('Updating person name');
    this.set('personName', e.target.value);
  }
}
