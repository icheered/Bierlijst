import Model, { attr } from '@ember-data/model';

// This is a transaction item that is received from the server on request
export default class TransactionListItemModel extends Model {
  @attr('number') timestamp;
  @attr('boolean') is_active;
  @attr('string') itemid;
  @attr('string') personid;
  @attr change;
}
