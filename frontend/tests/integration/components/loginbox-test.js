import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import { hbs } from 'ember-cli-htmlbars';

module('Integration | Component | loginbox', function (hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function (assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`<Loginbox />`);

    assert.dom(this.element).hasText('');

    // Template block usage:
    await render(hbs`
      <Loginbox>
        template block text
      </Loginbox>
    `);

    assert.dom(this.element).hasText('template block text');
  });
});
