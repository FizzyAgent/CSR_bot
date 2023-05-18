from api.driver.parser import parse_gpt_output
from api.gpt.gpt_service import get_chat_response
from models.messages import Message
from models.settings import ChatSettings


def run(messages: list[Message], settings: ChatSettings):
    gpt_output = get_chat_response(
        messages=messages,
        company=settings.company,
        location=settings.location,
    )
    commands = parse_gpt_output(output=gpt_output, settings=settings)
    for command in commands:
        command.run()
