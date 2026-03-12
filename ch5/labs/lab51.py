# import inspect

# SURROUND = ""
# SINGLE_TASK = ""


# class Singleton(type):
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]


# def get_user_prompt(func: callable) -> str:
#     ...


# if __name__ == "__main__":
#     from openai import OpenAI
#     from openai.types.chat import ChatCompletion

#     client: OpenAI = OpenAI()

#     completion: ChatCompletion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[],
#     )
#     print("Docstring:", completion.choices[0].message.content)
import inspect

SURROUND = "You are a senior Python developer. Generate a clear Python docstring for the following function."
SINGLE_TASK = "Write a Python docstring for this function:\n\n{code}"


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def get_user_prompt(func: callable) -> str:
    code = inspect.getsource(func)
    return SURROUND + "\n\n" + SINGLE_TASK.format(code=code)


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    prompt = get_user_prompt(add)

    print("Generated Prompt:")
    print(prompt)