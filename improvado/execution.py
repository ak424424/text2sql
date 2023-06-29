import chat_part
from main import MainModel
from clickhouse_connection import client
main_model = MainModel()

def text2sql_prototype():
    q, t, cols = chat_part.chat_like_part()
    sql_draft = main_model.llm_chain.run({"Table": t, "question": q, "Columns": cols})
    return sql_draft, client.execute(sql_draft)

if __name__ == '__main__':
    print(text2sql_prototype())
