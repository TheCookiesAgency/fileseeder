import {defineField, defineType} from 'sanity';
import { prototype } from "./base/prototype";
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
      ...prototype,
    ${FIELDS}],
  preview: {
    select: {
      title: 'name',
      subtitle: "language",
    }
  }
})