from transformers import LlamaTokenizer, LlamaForCausalLM, pipeline
from transformers.generation import GenerationConfig
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from transformers import BitsAndBytesConfig
quantization_config = BitsAndBytesConfig(llm_int8_enable_fp32_cpu_offload=True)


class MainModel:
    def __init__(self):
        self.base_model = LlamaForCausalLM.from_pretrained(
            "chavinlo/alpaca-native",
            load_in_8bit=True,
            device_map='cpu',
            quantization_config=quantization_config,
            offload_folder="offload"
        )
        self.tokenizer = LlamaTokenizer.from_pretrained("chavinlo/alpaca-native")
        self.pipe = pipeline(
            "text-generation",
            model=self.base_model,
            tokenizer=self.tokenizer,
            max_length=500,
            temperature=0.3,
            top_p=0.95,
            repetition_penalty=1.2
        )
        self.local_llm = HuggingFacePipeline(pipeline=self.pipe)
        self.template = """
        Write a SQL Query given the table name {Table} and columns as a list {Columns} for the given question : 
        {question}.
        """
        self.prompt = PromptTemplate(template=self.template, input_variables=["Table", "question", "Columns"])
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.local_llm)

    def get_llm_response(self, tble, question, cols):
        response = self.llm_chain.run({"Table": tble, "question": question, "Columns": cols})
        return response


if __name__ == '__main__':
    tble = "employee"
    cols = ["id", "name", "date_of_birth", "band", "manager_id"]
    question = "Query the count of employees in band L6 with 239045 as the manager ID"
    print(MainModel().get_llm_response(tble, question, cols))
