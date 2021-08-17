import Model, { attr } from '@ember-data/model';

export default class AccountModel extends Model {
  @attr('string') name;
  @attr('string') color;
  @attr balance;
  @attr('boolean') is_active;
}
