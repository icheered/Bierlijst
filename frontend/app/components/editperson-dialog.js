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
  save() {
    this.personName ? this.personName = this.personName : this.personName = this.person.name
    this.personColor ? this.personColor = this.personColor : this.personColor = this.person.color
    console.log('Saving');
    console.log(this.personName, this.personColor)

    let person = this.store.peekRecord('person', this.person.id)
    person.name = this.personName
    person.color = this.personColor
    person.save()
  }

  @action
  updateName(e) {
    console.log('Updating person name');
    this.set('personName', e.target.value);
  }
  @action
  updateColor(e) {
    console.log('Updating person color');
    this.set('personColor', e.target.value);
  }
}
