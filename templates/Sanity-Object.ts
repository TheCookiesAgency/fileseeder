import {defineField, defineType} from 'sanity'

export default defineType({
  name: '${NAME}',
  title: '${TITLE}',
  type: 'object',
  fields: [
    defineField({
      name: 'copy',
      title: 'Texto',
      type: 'markdown'
    }),
  ],
  preview: {
    select: {
      title: 'name',
    }
  }
})