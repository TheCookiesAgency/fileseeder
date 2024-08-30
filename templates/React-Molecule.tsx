
type Props${NAME} = {
    data: unknown;
}

const ${NAME}: React.FC<${NAME}> = (props: Props${NAME}) => {
  return (
    <div className={`m-${className}`}>
      <h2>Hola! soy ${NAME}, una molécula</h2>
      <p>
        Puedes encontrarme en <code>${DIR_PATH}</code> como {" "}
        <pre>${FILE_NAME}</pre>
      </p>
      <p>y mi flow parte de esta clase m-${className}, en el mismo dir :) </p>
    </div>
  );
};

export default ${NAME};
