
#15 databricks/ data modelling quesions that include:  
# - The quesion, 
# - Multiple choice options, 
# - Which is the correct option

QUESTIONS = [
{
        "question": "Which language is used to build Tkinter GUIs?",
        "options": ["Java", "C#", "Python", "Go"],
        "answer_index": 2},
{
        "question": "In Databricks, which layer should data analysts generally query for reporting?",
        "options": ["Bronze", "Silver", "Gold", "Raw"],
        "answer_index": 2},        # Gold
{
        "question": "What widget is best for a single-line text input in Tkinter?",
        "options": ["Label", "Entry", "Text", "Canvas"],
        "answer_index": 1},
{
        "question": "What is the main purpose of the Gold layer in the Medallion Architecture?",
        "options": ["Store raw data as-is", "Store cleaned, enriched, analytics-ready data", "Store machine learning features only", "Archive historical data"],
        "answer_index": 1},         # analytics-ready
{
        "question": "Which geometry manager places widgets side‑by‑side by default?",
        "options": ["pack", "grid", "place", "align"],
        "answer_index": 0},
{
        "question": "For Data Analysts, why is Delta Lake important?",
        "options": ["It encrypts dashboards", "It is needed for machine learning only", "It enables ACID transactions, versioning, and reliable queries", "It automatically builds Power BI models"],
        "answer_index": 2},           # ACID, versioning
{
        "question": "What method starts the Tkinter event loop?",
        "options": ["root.run()", "root.open()", "root.mainloop()", "root.start()"],
        "answer_index": 2},
{
        "question": "What advantage does Databricks SQL offer to Data Analysts?",
        "options": ["A SQL workspace with dashboards and a BI-friendly query editor", "Ability to train deep learning models", "Management of Kubernetes clusters", "Running RPA automations"],
        "answer_index": 0},        # SQL workspace
{
        "question": "Which Medallion layer should contain conformed dimensions and fact tables?",
        "options": ["JSON Archive", "Silver", "Bronze", "Gold"],
        "answer_index": 3},         # Gold
{
        "question": "In analytics modelling, what is a 'Fact Table'?",
        "options": ["A table of unstructured files", "A table containing business events or measurements", "A table containing lookup values", "A table containing only binary data"],
        "answer_index": 1},        # events/measurements
{
        "question": "In a star schema, Dimension Tables usually contain:",
        "options": ["System logs", "Descriptive attributes (e.g., product name)", "Only numeric fields", "Duplicate uncleaned fields"],
        "answer_index": 1},          # descriptive attributes
{
        "question": "Why are surrogate keys important in a star schema?",
        "options": ["They avoid dependency on unstable business keys", "They replace all primary keys", "They are faster for machine learning", "They are required for Power BI visuals to work"],
        "answer_index": 0},         # avoid unstable business keys
{
        "question": "Which Databricks feature is most useful for incremental ingestion into Bronze?",
        "options": ["SQL Endpoints", "Jobs", "Auto Loader", "Delta Live Tables"],
        "answer_index": 2},         # Auto Loader
{
        "question": "What is the best layer to join tables for star schema modelling?",
        "options": ["Gold", "None — joins shouldn’t be used", "Silver", "Bronze"],
        "answer_index": 2},          # Silver
{
        "question": "Why shouldn’t Data Analysts query Bronze directly?",
        "options": ["It requires Python", "It costs more", "Data is raw, unvalidated, and may contain duplicates", "It is stored in JSON format"],
        "answer_index": 2},        # raw/unvalidated
{
        "question": "What is a best practice for Power BI developers when using Databricks as a source?",
        "options": ["Avoid star schemas", "Import only Gold tables to keep the model clean and stable", "Load data directly from Bronze for speed", "Build Power BI transformations in DAX, not Databricks"],
        "answer_index": 1},         # use Gold tables
{
        "question": "What transformation typically happens in the Silver layer?",
        "options": ["Aggregating business metrics", "Geo-spatial mapping", "KPI calculations for dashboards", "Data cleansing, removing duplicates, standardising fields"],
        "answer_index": 3}          # cleansing, standardising
]