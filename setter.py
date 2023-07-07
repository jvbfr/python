class MakeDataset:
    def __init__(self,root):
        self.root = root
        self.__dataframe = None

    @property #Isso vai fazer com que o dataframe seja tratado como um atributo da classe("propriedade") e não um método
    def dataframe(self) -> pyspark.sql.DataFrame:
        """
        Retorna o dataframe blablabla ... 
        """
        if not self.__dataframe:

            df = (
                # operações 
            )
            
            return df
        return self.__dataframe

    @dataframe.setter 
    def dataframe(self, df:pyspark.sql.DataFrame):
        self.__dataframe = df


make_dataset = MakeDataset(root)

df = make_dataset.dataframe # Vai carregar e fazer as operações

df_again = make_dataset.dataframe # não vai carregar denovo.

make_dataset.dataframe = outro_df # O setter vai mudar o valor de __dataframe e não vai reprocessar. 
