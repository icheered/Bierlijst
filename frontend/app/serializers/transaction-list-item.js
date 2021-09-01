import JSONSerializer from '@ember-data/serializer/json';

export default class TransactionListItemSerializer extends JSONSerializer {
  attrs = {
    timestamp: { key: 'timestamp' },
    is_active: { key: 'is_active' },
    itemid: { key: 'itemid' },
    personid: { key: 'personid' },
    change: { key: 'change' },
  };

  serialize(snapshot, options) {
    // This removes all attributes from the request
    return;
  }
}
