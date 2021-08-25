import { helper } from '@ember/component/helper';

export default helper(function functionHelper([scope, fn]) {
  let args = arguments[0].slice(2);
  let res = fn.apply(scope, args);
  return res;
});
