from openai import AsyncOpenAI

from src.config import Config


class AiApiClient:

    def __init__(self, config: Config):
        self.client = AsyncOpenAI(
            api_key=config.ai_client.token,
        )

    async def completion(self, query: str, system_propmt: str = '',
                         temperature: float = 0.7, max_tokens: int = 256) -> str:
        response = await self.client.chat.completions.create(
            messages=[
                {
                    'role': 'system',
                    'content': system_propmt
                },
                {
                    'role': 'user',
                    'content': query
                }
            ],
            model='gpt-4o',
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
