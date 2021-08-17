import ApplicationAdapter from './application';

export default class PersonAdapter extends ApplicationAdapter {
    pathForType(person) {
        return 'person';
    }
}
