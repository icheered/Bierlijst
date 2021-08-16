import Model, { attr } from '@ember-data/model';

export default class AccountModel extends Model {
  @attr('string') email;
  @attr('string') full_name;
  @attr('string') username;
  @attr('boolean') is_premium;
  @attr('boolean') is_verified;
  @attr('boolean') is_active;
}
