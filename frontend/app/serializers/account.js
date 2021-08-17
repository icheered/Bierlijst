import JSONSerializer from '@ember-data/serializer/json';

export default class AccountSerializer extends JSONSerializer {
  attrs = {
    email: { key: 'email' },
    full_name: { key: 'full_name' },
    username: { key: 'username' },
    is_premium: { key: 'is_premium' },
    is_verified: { key: 'is_verified' },
    is_active: { key: 'is_active' },
  };
}
