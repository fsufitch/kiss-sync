import 'vuetify/styles';
import * as Vue from 'vue';
import Application from '@kiss-sync/components/Application.vue';

async function main() {
  const app = Vue.createApp(Application);

  const { createVuetify } = await import('./vuetify-loader');
  const vuetify = await createVuetify();
  app.use(vuetify);

  app.mount('#app-container');
}

(() => main())();
