---
import {sanityClient} from "sanity:client";
import type { ${NAME} } from "@/shared/sanity/sanity.types"
import {getHtmlSimpleCopy} from "@/shared/utils/get-html-render";

import type {TagTitle} from "@/shared/utils/get-html-render";


interface Props {
    _id: string;
    headingLevel?: TagTitle
}

const {  _id, headingLevel } = Astro.props;
// change firsLetter to lowercase in query
const data = await sanityClient.fetch<${NAME}>(
    `*[_id == "${_id}" ][0]{ ...${lowerCamelName}}`,
);
const copy = getHtmlSimpleCopy(data.copy, headingLevel );
 ---
<section class={`o-${className}`}>
  <div class={`c-${className}`}>
      <h1>Hola! soy ${NAME},</h1>
      <pre>{JSON.stringify(data,  null, 2)}</pre>
  </div>
</section>
