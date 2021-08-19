import ApplicationAdapter from './application';

export default class TransactionAdapter extends ApplicationAdapter {
  pathForType(transaction) {
    return 'transaction';
  }
}
