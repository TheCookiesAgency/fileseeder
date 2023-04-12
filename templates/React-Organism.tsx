import * as React from "react";
import { PropsWithChildren } from "react";
#if (${translation} != "")import { useTranslation } from "react-i18next";#end 

type Props${NAME} = PropsWithChildren<{
    element: string;
}>

const ${NAME}: React.FC<Props${NAME}> = (props: Props${NAME}) => {
#if (${translation} != "")  const { t } = useTranslation("${className}");#end
  return (
    <section className={`o-${className}`}>
      <div className={`c-${className}`}>
          <h1>Hola! soy ${NAME},</h1>
          <p>
            Puedes encontrarme en ${DIR_PATH} como ${FILE_NAME}
          </p>
          #if (${translation} != "")<blockquote>{t("${className}.name")}</blockquote>#end
          <p>
            y mi flow parte de esta clase o-${className}, en el mismo dir :)
          </p>
      </div>
    </section>
  );
};

export default ${NAME};
