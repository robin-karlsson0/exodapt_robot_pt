import textwrap
from datetime import datetime


def state_representation_pt(
    situation_assessment: str = '',
    current_context_summary: str = '',
    personality_static: str = '',
    personality_dynamic: str = '',
    retrieved_mem: str = '',
    state_chunks: str = '',
    running_actions: str = '',
) -> str:
    """Return the current robot and environment state as a structured string.

    State representation structure:

        State header
            - Situation assessment
            - Current context summary
            - Pesonality
                - Static profile
                - Dynamic profile (TBD ?)
            - State representation structure description

        Retrieved memory
            - Procedural memory (TBD ?)
            - Episodic memory (TBD ?)
            - Semantic memory (TBD ?)

        State chunks
            - Event queue
            - Continuous queue
            - Thoughts queue
            ==> All queues concatenated and sorted in temporal order.

        Running actions

        Robot state information
            - Current time, location, etc. (TBD ?)

    Design notes:
        - Role description is decoupled from the state representation.
        - Agency-related information is subsumed as Thoughts.
        - Presumes the meaning of the state is specified where it is used.

    Args:
        personality: Description of the robot's personality profile.
        retrieved_mem: Summary of task-relevant long-term memories.
        state_chunks: List of most recent state information including events,
            observations, and thoughts in temporal order.
        running_actions: Information about currently running actions.
    """
    state = ''

    ##################
    #  State header
    ##################
    state += textwrap.dedent(f"""
## Situation Assessment
{situation_assessment}

## Current Context Summary
{current_context_summary}

## Personality Profile
{personality_static}
{personality_dynamic}

## State Representation Structure Description
The reminder of the robot state represention is structured as follows:

1. Retrieved memory contains summaries of task-relevant long-term memories.

2. State chunks include the most recent events like robot observations (speech recognition, etc.), robot actions (replies, etc.), internal thoughts (self-reflection, etc.). All chunks are concatenated and sorted in temporal order.

Each chunk is structured as follows with comment explanations:
topic: TOPIC_NAME  # Name of ROS 2 topic publishing message
ts: TIMESTAMP  # Timestamp of message formatted as 'year-month-day hour:minute:second'
data: INFORMATION  # State chunk information content sent to the topic

The following is a list of topic names and their descriptions:
/asr: Automatic speech recognition. Talk robot hears from a microphone.
/keyboard_input: Messages the user wrote on a keyboard and sent to the robot.
/reply_action: What the robot has said to the user as a result of a reply action.

3. List of currently running actions.
Each running action is represented by the following format:
action_key: [action_name] action_description
Only one type of action (e.g. an action with the same action_key) can run at one time. Different types of actions (e.g. actions with different action_keys) can run in parallel.

4. Robot state information such as current time, location, battery level, etc.
""")

    ######################
    #  Retrieved memory
    ######################
    state += textwrap.dedent(f"""
## Retrieved Memory
{retrieved_mem}
""")

    ##################
    #  State chunks
    ##################
    state += textwrap.dedent(f"""
## State Chunks
{state_chunks}
""")

    ####################
    #  Running actions
    ####################
    state += textwrap.dedent(f"""
## Running Actions
{running_actions}
""")

    #######################
    #  Robot state
    #######################
    state += textwrap.dedent(f"""
## Robot state
Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Current location: TBD
""")

    return state.strip()  # Remove any leading/trailing whitespace.


if __name__ == '__main__':

    situation_assessment = 'DUMMY SITUATION ASSESSMENT\nDUMMY SITUATION ASSESSMENT\nDUMMY SITUATION ASSESSMENT'  # noqa: E501
    current_context_summary = 'DUMMY CONTEXT SUMMARY\nDUMMY CONTEXT SUMMARY\nDUMMY CONTEXT SUMMARY'  # noqa: E501
    personality_static = 'DUMMY PERSONALITY STATIC\nDUMMY PERSONALITY STATIC\nDUMMY PERSONALITY STATIC'  # noqa: E501
    personality_dynamic = 'DUMMY PERSONALITY DYNAMIC\nDUMMY PERSONALITY DYNAMIC\nDUMMY PERSONALITY DYNAMIC'  # noqa: E501
    retrieved_mem = 'DUMMY RETRIEVED MEMORY\nDUMMY RETRIEVED MEMORY\nDUMMY RETRIEVED MEMORY'  # noqa: E501
    state_chunks = 'DUMMY STATE CHUNKS\nDUMMY STATE CHUNKS\nDUMMY STATE CHUNKS'  # noqa: E501
    running_actions = 'DUMMY RUNNING ACTIONS\nDUMMY RUNNING ACTIONS\nDUMMY RUNNING ACTIONS'  # noqa: E501

    # Remove leading/trailing line breaks
    state = state_representation_pt(
        situation_assessment,
        current_context_summary,
        personality_static,
        personality_dynamic,
        retrieved_mem,
        state_chunks,
        running_actions,
    )

    print(state)
