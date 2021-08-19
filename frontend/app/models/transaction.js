import Model, { attr } from '@ember-data/model';

export default class TransactionModel extends Model {
  @attr('string') itemid;
  @attr('string') personid;
  @attr change;
}
