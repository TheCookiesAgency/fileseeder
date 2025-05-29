---
import { getCollection } from "astro:content";


export async function getStaticPaths() {
    const landingsList = await getCollection("${lowerCamelName}");
    return landingsList.map((landing) => ({
        params: {
            ${lowerCamelName}: landing.data.slug,
},
    props: { data: landing.data },
}));
}
const { data } = Astro.props;


---

<${lowerCamelName}Page _id={data.id} />

${LAYOUT}
