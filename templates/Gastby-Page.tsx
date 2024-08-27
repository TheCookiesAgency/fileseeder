---
import { getCollection} from "astro:content";
import { getSlugWithLang } from "@/translations/modules/getSlugWithLang";
import { type ${namePage} } from "@/shared/sanity/sanity.types";
import Layout from "../astro/layouts/Layout.astro";
import {type PrototypePageData} from "@/shared/utils/thecookies";


interface Props {
    data: PrototypePageData<${namePage}>;
}

export async function getStaticPaths() {
    const landingsList = await getCollection("legalsInSanity");
    return landingsList.map((landing) => ({
        params: {
    ${namePage}: `${getSlugWithLang(landing.data.slug, landing.data.language)}`,
},
    props: { data: landing.data },
}));
}
const { data } = Astro.props;


---

    <Layout id={data._id}>
${LAYOUT}
    </Layout>