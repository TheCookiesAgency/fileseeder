import {defineField, defineType} from 'sanity';

export default defineType({
  name: '${NAME}',
  title: '${NAME}',
  type: 'object',
  fields: [
    defineField({
      name: 'name',
      title: 'Nombre',
      type: 'string'
    }),
  ],
  preview: {
    select: {
      title: 'name',
    }
  }
})