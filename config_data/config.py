from dataclasses import dataclass
from environs import Env

@dataclass()
class TgBot:
    token: str

@dataclass()
class Config:
    tg_bot: TgBot

def loadtoken(tokenpath: str | None = None) -> Config:
    env = Env()
    env.read_env(tokenpath)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
