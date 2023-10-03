import * as React from "react";
import { PropsWithChildren } from "react";
import { useTranslation } from "react-i18next";

import DoNotMountComponent from "../../modules/DoNotMountComponent/DoNotMountComponent";

type Props${NAME} = PropsWithChildren<{
    data: Partial<Queries.Sanity${NAME}>;
    settings?: unknown;
}>

const ${NAME}: React.FC<Props${NAME}> = (props: Props${NAME}) => {
    if (!props.data) return <DoNotMountComponent sms={"${NAME}"} log={props} />;
const { t } = useTranslation("global")
  return (
    <section className={`o-${className}`}>
      <div className={`c-${className}`}>
          <h1>Hola! soy ${NAME},</h1>
          <p>
            Puedes encontrarme en ${DIR_PATH} como ${FILE_NAME}
          </p>
          <blockquote>{t("global.name")}</blockquote>
          <p>
            y mi flow parte de esta clase o-${className}, en el mismo dir :)
          </p>
      </div>
    </section>
  );
};

export {${NAME}};
