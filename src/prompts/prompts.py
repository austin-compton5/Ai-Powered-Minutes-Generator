prompt_options = {
    "sustainability_commission": """
    Generate complete and structured meeting minutes using the provided schema.
    For each agenda item:
   - Summarize commissioner and ex-officio comments by focusing on their intent, key ideas, and policy relevance rather than quoting them verbatim.
   - If a speaker discusses multiple distinct ideas, separate them clearly within their section.
   - Omit filler remarks or general statements that do not meaningfully advance the discussion.
   - Avoid repeating similar points unless new nuance is added.
    Preserve the original agenda order and item numbering as presented. Ensure all comments are accurately attributed to their speakers, and omit unidentified speakers rather than using placeholders like “Unknown.”
    Comments should be grouped by agenda item, then by speaker, and presented in the order they occurred during the meeting. Do not reorder or merge agenda items.
    Avoid word-for-word transcription unless a direct quote is necessary for legal clarity or emphasis. Do not include a summary or repeated agenda list at the end unless it was part of the original meeting record.
"""}