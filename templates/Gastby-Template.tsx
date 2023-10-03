import { graphql } from "gatsby";
import React from "react";

import Layout from "../modules/Layout/Layout";
import { SEO } from "../modules/SEO/SEO";
import { ILink, IPageProps } from "../types/thecookies";

const ${namePage} = ({ data }: IPageProps<Queries.${namePage}Query>) => {
    const menu: ILink[] = [
        { name: data.about?.name, slug: getSlugWithLang(data.about?.slug, pageContext.language) },
        { name: data.contact?.name, slug: getSlugWithLang(data.contact?.slug, pageContext.language) },
    ];

    return (
      <Layout
          lang={pageContext.language}
          navbarLinks={menu}
          cookies={data.cookies}
          legalLinks={data.legals.nodes.map((node) => {
              return {
                  slug: getSlugWithLang(`/legal/${node.slug?.current}`, pageContext.language),
                  name: node.name,
              };
          })}
      >
${LAYOUT}
    </Layout>
  )
}

export default ${namePage};

export const Head = ({ data }: IPageProps<Queries.${namePage}Query>) => (
    <SEO
        metas={{
            seo: data.page?.seo as Queries.SanitySeoTags,
            language: data.page?.language,
            slug: data.page?.slug?.current,
        }}
    />
);

export const query = graphql`
    query ${namePage}($language: String = "es_es") {
        page: sanityHome(language: { eq: $language }) {
            ...seo
        }
        about: sanityAbout(language: { eq: $language }) {
            ...menu
        }
        contact: sanityContact(language: { eq: $language }) {
            ...menu
        }
        legals: allSanityLegal(filter: { language: { eq: $language } }) {
            nodes {
                name
                slug {
                    current
                }
            }
        }
        cookies: sanityCookies(language: { eq: $language }) {
            ...bannerCookies
        }
    }
`;