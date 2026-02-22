from graph.builder import build_state_graph
from langgraph.graph import END
from routes import context_route,emergency_route,conversation_route


builder = build_state_graph()

def configure_conversation_graph(builder):    
    builder.set_entry_point("ConversationContextValidationAgent")
    
    builder.add_conditional_edges("ConversationContextValidationAgent",conversation_route,{"normal_conversation" : "GeneralDialogueHandlingAgent", 
                                                                          "emergency_conversation" : "DynamicQuestionAgent"
                                                                         })
    
    builder.add_edge("DynamicQuestionAgent","ContextFullFillAgent")

    builder.add_conditional_edges("ContextFullFillAgent",context_route,{"full_context_not_given" : "DynamicQuestionAgent",
                                                            "full_context_given":"EmergecyDetectionAgent"
                                                           })
    
    builder.add_conditional_edges("EmergecyDetectionAgent",emergency_route,{"is_emergency" : "RespondAgent",
                                                            "not_emergency" : "HelpingProcessAgent"})
    
    builder.add_edge("RespondAgent","RespondConversationAgent")

    return builder
