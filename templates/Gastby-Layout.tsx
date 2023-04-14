import { graphql, PageProps } from "gatsby";
import React from "react";

import Layout from "../modules/Layout/Layout";
import { SEO } from "../modules/SEO/SEO";

const ${namePage} = ({ data }: PageProps<Queries.${namePage}Query>) => {
  return (
    <Layout>
      <div className="container">
          <h1>${NAME}</h1>
      </div>
    </Layout>
  )
}

export default ${namePage};

export const Head = () => <SEO />;

export const query = graphql`
    query ${namePage}{
    
    }
`