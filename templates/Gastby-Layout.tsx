---
import { getCollection} from "astro:content";
import { getSlugWithLang } from "@/translations/modules/getSlugWithLang";
import { type ${namePage} } from "@/shared/sanity/sanity.types";
import Layout from "../astro/layouts/Layout.astro";
import {type PrototypePageData} from "@/shared/utils/thecookies";


interface Props {
    data: PrototypePageData<${namePage}>;
    sharedId: string;
}

export async function getStaticPaths() {
    const landingsList = await getCollection("${lowerCamelName}");
    const sharedList = await getCollection("shared");

    return landingsList.map((landing) => ({
        params: {
    ${lowerCamelName}: `${getSlugWithLang(landing.data.slug, landing.data.language)}`,
},
    props: { data: landing.data },
}));
}
const { data, sharedId } = Astro.props;


---

    <Layout id={data._id}>
        ${LAYOUT}
    </Layout>