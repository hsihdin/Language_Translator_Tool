import gradio as gr
import openai

api_key = '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'

def translate_text(text, source_lang, target_lang):
    if api_key is not None:
        openai.api_key = api_key
        prompt = f"translate the following text from {source_lang} to {target_lang}: {text}"

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=350,
            temperature=0.5
        )

        translated_text = response["choices"][0]["text"]
        return translated_text
    else:
        return "API key not provided."

iface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.inputs.Textbox(label="Input Text"),
        gr.inputs.Textbox(label="Source Language (e.g., English)"),
        gr.inputs.Textbox(label="Target Language (e.g., Hindi)")
    ],
    outputs=gr.outputs.Textbox(label="Translated Text"),
    title="Language Translation Tool",
    description="Translate text from one language to another using OpenAI.",
)

if __name__ == "__main__":
    iface.launch()
