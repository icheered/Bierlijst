import JSONSerializer from '@ember-data/serializer/json';

export default class PersonSerializer extends JSONSerializer {
  attrs = {
    name: { key: 'name' },
    color: { key: 'color' },
    balance: { key: 'balance' },
    is_active: { key: 'is_active' },
  };
}
