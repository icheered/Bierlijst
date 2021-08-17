import Component from '@ember/component';
import { inject as service } from '@ember/service';



export default class Logout extends Component {
    @service store;

    get name() {
        return this.store.peekRecord('item', this.item.id).name
    }
}
