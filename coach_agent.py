from llama_cpp import Llama

# Load the model
llm = Llama(
    model_path="models/mistral.gguf",
    n_ctx=2048,
    n_threads=4,       # You can change this based on your CPU
    n_batch=32,
    verbose=False
)

def generate_response(prompt: str) -> str:
    # Optional system prompt (can be customized)
    system_prompt = "You are a helpful self-coaching assistant."
    
    full_prompt = f"[INST] <<SYS>> {system_prompt} <</SYS>> {prompt} [/INST]"
    
    output = llm(full_prompt, max_tokens=512, stop=["</s>"])
    
    response = output["choices"][0]["text"].strip()
    return response
