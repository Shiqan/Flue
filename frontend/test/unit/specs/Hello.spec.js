import Vue from 'vue'
import StartPage from '@/pages/Start'

describe('StartPage.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(StartPage)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.content .Search__button').textContent)
      .to.equal('Find')
  })
})
