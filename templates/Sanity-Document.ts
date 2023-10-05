import {defineField, defineType} from 'sanity';
import { landing } from "./base/landing";
${IMPORTS}

export default defineType({
  name: '${NAME}',
  title: '${NAME}',
  type: 'document',
  groups: [
    { name: "seo", title: "Metas" },
    { name: "content", title: "Contenido" },
    { name: "shared", title: "Compartido" },
    { name: "settings", title: "Configuración" },
  ],
  fields: [
      ...landing,
    ${FIELDS}],
  preview: {
    select: {
      title: 'name',
      subtitle: "language",
    }
  }
})