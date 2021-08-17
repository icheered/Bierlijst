import JSONSerializer from '@ember-data/serializer/json';

export default class ItemSerializer extends JSONSerializer {
  attrs = {
    name: { key: 'name' },
    container_size: { key: 'container_size' },
    is_active: { key: 'is_active' },
  };
}
