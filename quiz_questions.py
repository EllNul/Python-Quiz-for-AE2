
#15 databricks/ data modelling quesions that include:  
# - The quesion, 
# - Multiple choice options, 
# - Which is the correct option
# - Added an extra section that explains why that answer is correct/incorrect, gives explaination.

[
{
"question": "Q1: In Databricks, which layer should data analysts generally query for reporting?",
"options": ["Bronze", "Silver", "Gold", "Raw"],   
        "answer_index": 2,
        "explanation": "Gold contains curated, business-ready tables (facts/dimensions) designed for analytics and BI consumption."
},
{
"question": "Q2: What is the main purpose of the Gold layer in the Medallion Architecture?",
"options": ["Store raw data as-is", "Store cleaned, enriched, analytics-ready data", "Store machine learning features only", "Archive historical data"],
        "answer_index": 1,
        "explanation": "Gold tables are finalized, conformed datasets aligned to business logic—ready for dashboards and semantic models."
},
{
"question": "Q3: For Data Analysts, why is Delta Lake important?",
"options": ["It encrypts dashboards", "It is needed for machine learning only", "It enables ACID transactions, versioning, and reliable queries", "It automatically builds Power BI models"],
        "answer_index": 2,
        "explanation": "Delta Lake brings ACID reliability, schema enforcement, and time travel, which keeps analytics consistent and auditable."
},
{
"question": "Q4: What advantage does Databricks SQL offer to Data Analysts?",
"options": ["A SQL workspace with dashboards and a BI-friendly query editor", "Ability to train deep learning models", "Management of Kubernetes clusters", "Running RPA automations"],
        "answer_index": 0,
        "explanation": "Databricks SQL provides a familiar SQL editor, dashboards, and endpoints tailored to BI-style querying."
},
{
"question": "Q5: Which Medallion layer should contain conformed dimensions and fact tables?",
"options": ["JSON Archive", "Silver", "Bronze", "Gold"],
        "answer_index": 3,
        "explanation": "Conformed, business-aligned dimensions/facts belong in Gold for stable consumption by BI tools like Power BI."
},
{
"question": "Q6: In analytics modelling, what is a 'Fact Table'?",
"options": ["A table of unstructured files", "A table containing business events or measurements", "A table containing lookup values", "A table containing only binary data"],
        "answer_index": 1,
        "explanation": "Fact tables store measurable events (e.g. Provider_sk or Leaner_sk) that aggregate along related dimension attributes."
},
{
"question": "Q7: In a star schema, Dimension Tables usually contain:",
"options": ["System logs", "Descriptive attributes (e.g., product name)", "Only numeric fields", "Duplicate uncleaned fields"],
        "answer_index": 1,
        "explanation": "Dimensions provide descriptive context (attributes) for slicing and filtering fact measures in BI."
},
{
"question": "Q8: Why are surrogate keys important in a star schema?",
"options": ["They avoid dependency on unstable business keys", "They replace all primary keys", "They are faster for machine learning", "They are required for Power BI visuals to work"],
        "answer_index": 0,
        "explanation": "Surrogate keys decouple analytics from changing or non-unique business keys, keeping relationships stable."
},
{
"question": "Q9: Which Databricks feature is most useful for incremental ingestion into Bronze?",
"options": ["SQL Endpoints", "Jobs", "Auto Loader", "Delta Live Tables"],
        "answer_index": 2,
        "explanation": "Auto Loader efficiently discovers and incrementally ingests new files from cloud storage into Bronze."
},
{
"question": "Q10: What is the best layer to join tables for star schema modelling?",
"options": ["Gold", "None — joins shouldn’t be used", "Silver", "Bronze"],
        "answer_index": 2,
        "explanation": "Silver is where data is cleaned and standardized; preparing conformed joins here simplifies building Gold models."
},
{
"question": "Q11: Why shouldn’t Data Analysts query Bronze directly?",
"options": ["It requires Python", "It costs more", "Data is raw, unvalidated, and may contain duplicates", "It is stored in JSON format"],
        "answer_index": 2,
        "explanation": "Bronze is raw landing—may be incomplete, duplicated, or malformed. Analysts should use Silver/Gold instead."
},
{
"question": "Q12: What is a best practice for Power BI developers when using Databricks as a source?",
"options": ["Avoid star schemas", "Import only Gold tables to keep the model clean and stable", "Load data directly from Bronze for speed", "Build Power BI transformations in DAX, not Databricks"],
        "answer_index": 1,
        "explanation": "Gold tables reflect agreed business logic, minimizing Power BI model complexity and refresh issues."
},
{
"question": "Q13: What transformation typically happens in the Silver layer?",
"options": ["Aggregating business metrics", "Geo-spatial mapping", "KPI calculations for dashboards", "Data cleansing, removing duplicates, standardising fields"],
        "answer_index": 3,
        "explanation": "Silver standardizes and validates—deduplication, type casting, and conformance—so Gold can focus on business logic."
},
{
"question": "Q14: If a Power BI model connects to a Databricks Gold table, what is the main benefit?",
"options": ["It skips scheduled refresh", "It auto-generates ETL pipelines", "The data is already cleaned and model-friendly", "It creates measures automatically"],
        "answer_index": 2,
        "explanation": "Gold reduces downstream transformations—models are simpler, more consistent, and easier to maintain."
},
{
"question": "Q15: Which tool in Databricks can orchestrate ELT pipelines for analysts?",
"options": ["Git Repos", "Delta Live Tables", "Notebook Search", "The File Browser"],
        "answer_index": 1,
        "explanation": "Delta Live Tables (DLT) declaratively manages pipelines, quality, and dependencies for reliable ELT."
}
]