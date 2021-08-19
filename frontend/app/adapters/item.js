import ApplicationAdapter from './application';

export default class ItemAdapter extends ApplicationAdapter {
  pathForType(item) {
    return 'item';
  }
}
