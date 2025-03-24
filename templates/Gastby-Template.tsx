---
import { getCollection } from "astro:content";
import { getSlugWithLang } from "@global-shared/translations/utils/getSlugWithLang";


export async function getStaticPaths() {
    const landingsList = await getCollection("${lowerCamelName}");
    return landingsList.map((landing) => ({
        params: {
    ${lowerCamelName}: `${getSlugWithLang(landing.data.slug, landing.data.language)}`,
},
    props: { data: landing.data },
}));
}
const { data } = Astro.props;


---

<${lowerCamelName} id={data._id} />

    ${LAYOUT}
