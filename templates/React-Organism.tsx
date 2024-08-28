---
import {sanityClient} from "sanity:client";
import type { ${NAME} } from "@/shared/sanity/sanity.types";


const {  _id} = Astro.props;
// change firsLetter to lowercase in query
const data = await sanityClient.fetch<${NAME}>(
    `*[_id == "${_id}" ][0]{ ...${lowerCamelName}}`,
);

 ---
<section class={`o-${className}`}>
  <div class={`c-${className}`}>
      <h1>Hola! soy ${NAME},</h1>
      <pre>{JSON.stringify(data,  null, 2)}</pre>
  </div>
</section>
