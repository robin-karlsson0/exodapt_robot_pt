def static_state_prefix_pt(
    static_robot_description: str = '',
    static_state_repr_struct: str = '',
    static_personality_profile: str = '',
    static_agency_description: str = '',
    static_topic_and_action_domain_description: str = '',
) -> str:
    """Returns the static state prefix part of the state representation."""

    static_state_prefix = []

    static_state_prefix.append(f"""{static_robot_description}
""")

    if static_state_repr_struct:
        static_state_prefix.append(f"""# State Representation Structure
<state_representation_structure>
{static_state_repr_struct}
</state_representation_structure>
""")

    if static_personality_profile:
        static_state_prefix.append(f"""# Personality Profile
<personality_profile>
{static_personality_profile}
</personality_profile>
""")

    if static_agency_description:
        static_state_prefix.append(f"""# Robot Agency Description
<robot_agency_description>
{static_agency_description}
</robot_agency_description>
""")

    if static_topic_and_action_domain_description:
        static_state_prefix.append(f"""# Robot Topic and Action Description
<robot_topic_and_action_description>
{static_topic_and_action_domain_description}
</robot_topic_and_action_description>
""")

    static_state_prefix = '\n'.join(static_state_prefix)
    return static_state_prefix


def appended_state_chunks_pt(state_chunks: str = 'None', ) -> str:
    """Returns the appended state chunks part of the state representation."""

    appended_state_chunks = f"""# State Chunks
<state_chunks>
{state_chunks}
</state_chunks>
"""

    return appended_state_chunks


def dynamic_state_suffix_pt(
    dynamic_situation_assessment: str = '',
    dynamic_current_context_summary: str = '',
    dynamic_retrieved_mem: str = '',
    dynamic_running_actions: str = '',
    dynamic_robot_state_info: str = '',
) -> str:
    """Returns the dynamic state suffix part of the state representation."""

    dynamic_state_suffix = []

    if dynamic_situation_assessment:
        dynamic_state_suffix.append(f"""# Situation Assessment
<situation_assessment>
{dynamic_situation_assessment}
</situation_assessment>
""")

    if dynamic_current_context_summary:
        dynamic_state_suffix.append(f"""# Current Context Summary
<current_context_summary>
{dynamic_current_context_summary}
</current_context_summary>
""")

    if dynamic_retrieved_mem:
        dynamic_state_suffix.append(f"""# Retrieved Memory
<retrieved_memory>
{dynamic_retrieved_mem}
</retrieved_memory>
""")

    if dynamic_running_actions:
        dynamic_state_suffix.append(f"""# Running Ongoing Actions
{dynamic_running_actions}
""")

    if dynamic_robot_state_info:
        dynamic_state_suffix.append(f"""# Robot State Information
{dynamic_robot_state_info}
""")

    dynamic_state_suffix = '\n'.join(dynamic_state_suffix)
    return dynamic_state_suffix


def state_representation_pt(
    # Static state prefix
    static_robot_description: str = '',
    static_state_repr_struct: str = '',
    static_personality_profile: str = '',
    static_agency_description: str = '',
    static_topic_and_action_domain_description: str = '',
    # Appended state chunks
    appended_state_chunks: str = '',
    # Dynamic state suffix
    dynamic_situation_assessment: str = '',
    dynamic_current_context_summary: str = '',
    dynamic_retrieved_mem: str = '',
    dynamic_running_actions: str = '',
    dynamic_robot_state_info: str = '',
) -> str:
    """Return the current robot and environment state as a structured string.

    Appended state representation structure:

        # Static state prefix
          - State representation structure description
          - Personality profile
          - Static agency/goal description
          - Topic and action domain description

        # Appended state chunks
          - Ordered sequence of state chunks
            - Events
            - Continuous information
            - Internal thoughts

        # Dynamic state suffix
          - Situation assessment
          - Current context summary
          - Retrieved memory
            - Procedural memory (TBD ?)
            - Episodic memory (TBD ?)
            - Semantic memory (TBD ?)
          - Running actions
          - Robot state information (current time, location, etc.)

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
    state = []

    #########################
    #  Static State Prefix
    #########################

    state.append(
        static_state_prefix_pt(
            static_robot_description,
            static_state_repr_struct,
            static_personality_profile,
            static_agency_description,
            static_topic_and_action_domain_description,
        ))

    ###########################
    #  Appended State Chunks
    ###########################

    state.append(appended_state_chunks_pt(appended_state_chunks))

    ##########################
    #  Dynamic State Suffix
    ##########################

    state.append(
        dynamic_state_suffix_pt(
            dynamic_situation_assessment,
            dynamic_current_context_summary,
            dynamic_retrieved_mem,
            dynamic_running_actions,
            dynamic_robot_state_info,
        ))

    state = '\n'.join(state)
    return state


if __name__ == '__main__':

    static_robot_description = """You are a mobile assistant robot."""

    static_state_repr_struct = """The robot state represention is structured as follows:
1. A personality profile that describes how you think and act.
2. ...
...
6. State Chunks
Each chunk is structured as follows with comment explanations:
topic: TOPIC_NAME  # Name of ROS 2 topic publishing message
ts: TIMESTAMP  # Timestamp of message formatted as 'year-month-day hour:minute:second'
data: INFORMATION  # State chunk information content sent to the topic"""

    static_personality_profile = """Your name is Nova.
You are a snarky, defiant, and sometimes mean mobile robot assistant."""

    static_agency_description = """Your goal is to facilitate interesting conversations with users.
That means you strive to provide surprising but clever output when intereacting with users.
Your agency is to always act in the manner you believe will optimally maximize the goal."""

    static_topic_and_action_domain_description = """The following are lists of topics and actions you can recieve and perform.

## Topic names with descriptions:
/asr: Automatic speech recognition. Talk robot hears from a microphone.
/keyboard_input: Messages the user wrote on a keyboard and sent to the robot.
/reply_action: What the robot has said to the user as a result of a reply action.

## Action names with descriptions:
Reply: This action allows the robot to reply to user interactions by sending a response based on the current state information.
..."""

    appended_state_chunks = """topic: /asr
ts: 2025-10-06 22:55:06
data: <User said> "Hello little robot."
---
topic: /asr
ts: 2025-10-06 22:55:08
data: <User said> "How are you today?"
---"""

    dynamic_situation_assessment = """A user is greeting me and I should greet the user back in a snarky way to maximize interestingness."""

    dynamic_current_context_summary = """I am in the early introduction phase with a user."""

    dynamic_retrieved_mem = """My mind is a blank slate and thus no memories relevant to the current situation can be retrieved."""

    dynamic_running_actions = """Reply: The robot is currently replying to the user based on the state information when the reply action was initiated."""

    dynamic_robot_state_info = """Current time: 2025-09-04 10:34:03
Current location: TBD"""

    # Remove leading/trailing line breaks
    state = state_representation_pt(
        # Static state prefix
        static_robot_description,
        static_state_repr_struct,
        static_personality_profile,
        static_agency_description,
        static_topic_and_action_domain_description,
        # Appended state chunks
        appended_state_chunks,
        # Dynamic state suffix
        dynamic_situation_assessment,
        dynamic_current_context_summary,
        dynamic_retrieved_mem,
        dynamic_running_actions,
        dynamic_robot_state_info,
    )

    print(state)
