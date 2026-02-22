from langgraph.graph import StateGraph
from graph.state import State,Input_schema,Output_schema,Context_schema
from nodes import (context_full_fill,
                   conversation_context_validation,
                   respond_conversation,
                   handle_general_conversation,
                   dyanamic_question,
                   emeragency_detection,
                   respond,
                   helping_process,
)


def build_state_graph():

    builder = StateGraph(
        state_schema=State,
        input_schema=Input_schema,
        output_schema=Output_schema,
        context_schema=Context_schema
    )

    builder.add_node("ConversationContextValidationAgent", conversation_context_validation)
    builder.add_node("GeneralDialogueHandlingAgent", handle_general_conversation)
    builder.add_node("DynamicQuestionAgent", dyanamic_question)
    builder.add_node("ContextFullFillAgent", context_full_fill)
    builder.add_node("EmergecyDetectionAgent", emeragency_detection)
    builder.add_node("RespondAgent", respond)
    builder.add_node("RespondConversationAgent", respond_conversation)
    builder.add_node("HelpingProcessAgent", helping_process)

    return builder