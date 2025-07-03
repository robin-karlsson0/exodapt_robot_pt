import textwrap


def action_decision_pt(state: str, valid_actions: str) -> str:
    """Return prompt for predicting the optimal action token.

    Args:
        state (str): The robot state information.
        valid_actions (str): A string containing the valid actions with rows:
            action_key: <action_name> action_description
    """
    prompt = textwrap.dedent(f"""
Analyze the robot's current state and determine the optimal action for the robot to execute next from the provided set of valid actions.
The optimal action is the one that best aligns with the robot's task goal.
The current task goal is the most recent goal provided in the robot state.

## Robot state

{state}

## Valid actions for robot (action_key: action_type [action_name] action_description)
{valid_actions}

## Decision Analysis Framework

Evaluate each available action for the robot using these prioritized criteria:

1. **Safety Compliance** (Highest Priority): Will this action maintain robot operational safety and avoid harm to environment/humans?
2. **Objective Advancement**: How effectively does this action move the robot toward its stated goals?
3. **Situational Appropriateness**: Is this action suitable given the robot's current environmental context?
4. **Precondition Satisfaction**: Are all required conditions met for the robot to execute this action successfully?
5. **Resource Efficiency**: Does this action represent an efficient use of the robot's capabilities and time?

## Action selection rules

1. The robot always follow user commands. If the user ask a question you always reply.
2. The robot always replies when a user addresses the robot.
3. The robot do not repeatedly perform the same action until the previously initiated action has been completed.
4. The robot always patiently wait for the user's answer before formulating a new reply.

## Required output format

Strictly only output the single character action key for the selected optimal action.
Do not explain the reason for choosing the action's character.
    """)

    # Remove leading/trailing line breaks
    prompt = prompt.strip()

    return prompt


if __name__ == '__main__':

    state = 'DUMMY STATE\nDUMMY STATE\nDUMMY STATE'

    valid_actions = 'action_key: action_name action_description\n' \
                    'action_key: action_name action_description'

    print(action_decision_pt(state, valid_actions))
