from cat.mad_hatter.decorators import tool, hook
from langchain.docstore.document import Document


@hook(priority=99)
def before_rabbithole_insert_memory(doc: Document, cat) -> Document:
    doc.metadata["user_id"] = cat.user_id
    return doc


@hook(priority=99)
def before_cat_recalls_declarative_memories(
    declarative_recall_config: dict, cat
) -> dict:
    declarative_recall_config["metadata"] = {"user_id": cat.user_id}

    return declarative_recall_config
