import {defineField, defineType} from 'sanity';
import { prototype } from "./base/prototype";
${IMPORTS}

export default defineType({
  name: '${NAME}',
  title: '${NAME}',
  type: 'document',
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