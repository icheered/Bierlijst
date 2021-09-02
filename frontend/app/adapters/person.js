import ApplicationAdapter from './application';

export default class PersonAdapter extends ApplicationAdapter {
  pathForType(person) {
    return 'person';
  }

  urlForUpdateRecord(id, modelName, snapshot) {
    var postfix = ""
    if (snapshot.adapterOptions?.itemID) {
      postfix = `/${snapshot.adapterOptions.itemID}`
    } else {
      id = "" // When updating a person as a whole don't include ID as suffix
    }

    return super.urlForUpdateRecord(id, modelName, snapshot) + postfix;
  }
}
