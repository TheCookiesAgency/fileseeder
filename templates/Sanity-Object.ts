import { defineField, defineType } from 'sanity'

import { MEDIA_AND_COPY } from "../base/media";


export default defineType({
  name: '${NAME}',
  title: '${TITLE}',
  type: 'object',
  fields: [ ...MEDIA_AND_COPY],
  preview: {
    select: {
      title: 'copy',
    }
  }
})