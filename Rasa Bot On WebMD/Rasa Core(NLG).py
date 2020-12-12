# Not appreciated to use python script instead use Rasa commands through CLI 

# from rasa.core.policies import FallbackPolicy, MemoizationPolicy,KerasPolicy
# from rasa.core import Agent

# # Initialize the model with `domain.yml`
# agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])

# # loading our  training dialogues from `stories.yml` 
# training_data = agent.load_data('stories.yml')


# # Training the model
# agent.train(
#     training_data,
#     validation_split=0.0,
#     epochs=200
# )
