import Model, { attr } from '@ember-data/model';

export default class ItemModel extends Model {
  @attr('string') name;
  @attr('number') container_size;
  @attr('boolean') is_active;
}
