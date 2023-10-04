import {defineField, defineType} from 'sanity';
import { landing } from "./base/landing";
${IMPORTS}

export default defineType({
  name: '${NAME}',
  title: '${NAME}',
  type: 'document',
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