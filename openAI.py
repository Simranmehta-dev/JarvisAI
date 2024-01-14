
#from openai import OpenAI
import openai


openai.api_key = 'your open ai key'


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "user",
      "content": ""
    },
    {
      "role": "assistant",
      "content": "write an email to my boss for resignation"
    },
    {
      "role": "assistant",
      "content": "Dear [Boss's Name],\n\nI hope this email finds you well. I am writing to inform you of my decision to resign from my position at [Company Name], effective [last day of work, typically two weeks from the date of the email].\n\nIt has been an honor and a privilege to work at [Company Name] for the past [duration of employment]. I have learned a great deal during my tenure here and have had the opportunity to work with some truly amazing colleagues. I would like to express my sincere gratitude for all the support, guidance, and opportunities provided to me during my time at the company.\n\nAfter careful consideration, I have decided to pursue a new opportunity that aligns more closely with my long-term career goals. This was not an easy decision to make, as I have genuinely enjoyed my time at [Company Name]. I am grateful for the experiences and knowledge gained, and I will always value the relationships I have built along the way.\n\nIn order to facilitate a smooth transition, I am committed to completing all my outstanding tasks and ensuring that handover notes and documentation are provided to my replacement, should you require any assistance in finding a suitable candidate.\n\nI want to assure you that I am fully dedicated to making this transition period as seamless as possible. If there"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
  "id": "chatcmpl-8gQf1c9nj1a10i4O21yPqfawtlPEC",
  "object": "chat.completion",
  "created": 1705122951,
  "model": "gpt-3.5-turbo-16k-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "is any support or assistance that I can provide, please do not hesitate to let me know.\n\nLastly, I would like to express my gratitude to you for your leadership, guidance, and support throughout my time at [Company Name]. Your mentorship has played a significant role in my professional development, and I am truly grateful for the opportunities you have given me.\n\nPlease let me know if there are any further steps I need to take or if there are any exit procedures that need to be followed. I am happy to discuss these matters further if needed.\n\nThank you once again for everything. I wish you and the entire team at [Company Name] continued success in your endeavors.\n\nSincerely,\n\n[Your Name]"
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 288,
    "completion_tokens": 142,
    "total_tokens": 430
  },
  "system_fingerprint": null
}
'''
