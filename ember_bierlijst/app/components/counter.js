import Component from '@glimmer/component';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';


export default class CounterComponent extends Component {
    @tracked count = 0;

    @action
    change(amount) {
        this.count = this.count + amount;
    }
}