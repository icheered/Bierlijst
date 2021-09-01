import ApplicationAdapter from './application';

export default class TransactionListItemAdapter extends ApplicationAdapter {
  pathForType(transactionListItem) {
    return 'transaction';
  }
}
