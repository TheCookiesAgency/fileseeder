import {defineField, defineType} from 'sanity';

import { landing } from "./base/landing";


export default defineType({
  name: '${NAME}',
  title: '${TITLE}',
  type: 'document',
  groups: [
    { name: "seo", title: "Metas" },
    { name: "content", title: "Contenido" },
    { name: "settings", title: "Configuración" },
  ],
  fields: [...landing],
  preview: {
    select: {
      title: 'name',
    }
  }
})